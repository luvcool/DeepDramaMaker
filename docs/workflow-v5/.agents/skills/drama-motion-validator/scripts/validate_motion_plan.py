#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from pathlib import Path

REQ = [
    "scene_id","shot_id","target_duration_sec","cut_reason","primary_motion",
    "motion_priority","frame_staging","start_state","end_state","micro_beats",
    "gaze","expression_transition","life_motion","camera_motion","contact_topology",
    "visibility_constraints","result","complexity","continuity_from_previous"
]

ALLOWED_BUDGET={"safe","dense_but_controlled","high_risk_split_recommended"}

def err(errors, path, msg): errors.append(f"{path}: {msg}")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("work_dir", type=Path)
    args=ap.parse_args()
    mdir=args.work_dir/"09_motion"
    files=sorted(mdir.glob("ep??-motion.json"))
    if not files:
        print("BLOCKED: no 09_motion/epXX-motion.json files found")
        return 2
    errors=[]; warnings=[]; ids=set(); total=0
    prev_end={}
    for f in files:
        try: data=json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:
            err(errors,f.name,f"invalid JSON: {e}"); continue
        shots=data.get("shots")
        if not isinstance(shots,list):
            err(errors,f.name,"shots must be a list"); continue
        for i,s in enumerate(shots,1):
            total+=1; p=f"{f.name} shot#{i}"
            if not isinstance(s,dict): err(errors,p,"shot must be object"); continue
            for k in REQ:
                if k not in s: err(errors,p,f"missing required key {k}")
            sid=s.get("shot_id")
            if sid in ids: err(errors,p,f"duplicate shot_id {sid}")
            elif sid: ids.add(sid)
            dur=s.get("target_duration_sec")
            if not isinstance(dur,(int,float)) or dur<=0: err(errors,p,"target_duration_sec must be > 0")
            if not str(s.get("primary_motion","")).strip(): err(errors,p,"primary_motion empty")
            mp=s.get("motion_priority",{})
            if not isinstance(mp,dict) or not mp.get("primary"): err(errors,p,"motion_priority.primary required")
            life=s.get("life_motion",[])
            if not isinstance(life,list): err(errors,p,"life_motion must be list")
            elif len(life)<2: warnings.append(f"{p}: fewer than 2 life_motion items")
            if not s.get("gaze"): warnings.append(f"{p}: gaze empty")
            if not s.get("expression_transition"): warnings.append(f"{p}: expression_transition empty")
            comp=s.get("complexity",{})
            if not isinstance(comp,dict): err(errors,p,"complexity must be object")
            else:
                score=comp.get("score")
                if not isinstance(score,int) or score<0: err(errors,p,"complexity.score must be nonnegative int")
                split=comp.get("split_recommended")
                if not isinstance(split,bool): err(errors,p,"complexity.split_recommended must be bool")
                if isinstance(score,int) and score>=4 and split is False:
                    warnings.append(f"{p}: complexity score {score} but split_recommended=false")
                budget=comp.get("motion_budget")
                if budget not in ALLOWED_BUDGET: err(errors,p,f"invalid motion_budget {budget!r}")
            # Contact heuristic: if primary mentions transfer/touch/grab/hold/pull, topology should exist
            pm=str(s.get("primary_motion","")).lower()
            contact_words=("transfer","touch","grab","grip","hold","pull","push","hand","contact","hug","kiss","brace")
            topo=s.get("contact_topology",[])
            if any(w in pm for w in contact_words) and not topo:
                warnings.append(f"{p}: likely contact interaction but contact_topology empty")
            if not s.get("start_state"): err(errors,p,"start_state empty")
            if not s.get("end_state"): err(errors,p,"end_state empty")
    print(f"checked {total} shots across {len(files)} episode files")
    for w in warnings: print("WARN",w)
    for e in errors: print("ERROR",e)
    if errors:
        print(f"BLOCKED: {len(errors)} errors, {len(warnings)} warnings")
        return 2
    if warnings:
        print(f"CONDITIONAL: 0 errors, {len(warnings)} warnings")
        return 1
    print("READY: 0 errors, 0 warnings")
    return 0

if __name__=="__main__":
    sys.exit(main())
