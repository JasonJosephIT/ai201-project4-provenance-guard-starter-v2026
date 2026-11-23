import csv,json,glob,sys
sys.path.insert(0,".")
import detector,stylometry,scoring
rows=[]
for r in csv.DictReader(open("attack_set/attacks.csv",encoding="utf-8")):
    rows.append((r["id"],r["family"],r["text"]))
for f in sorted(glob.glob("eval_inputs/own/*.txt")): rows.append(("own:"+f.split("/")[-1][:-4],"own",open(f).read()))
for f in sorted(glob.glob("eval_inputs/*.txt")):
    n=f.split("/")[-1][:-4]
    if n.startswith(("ai_","human_","borderline_","essay")): rows.append(("ev:"+n,"eval",open(f).read()))
out=[]
for i,fam,t in rows:
    try: m=detector.model_signal(t)
    except Exception as e: continue
    s=stylometry.style_signal(t); w=stylometry.ai_word_rate(t)
    out.append(dict(id=i,fam=fam,m=m,s=s,w=w,c=scoring.combine_signals(m,s),n=len(stylometry.words(t))))
json.dump(out,open(sys.argv[1],"w"))
for o in out: print(f"{o['id']:<26}{o['fam']:<16} m={o['m']:.3f} s={o['s']:.3f} c={o['c']:.3f} aiw={o['w']:.2f} n={o['n']}")
