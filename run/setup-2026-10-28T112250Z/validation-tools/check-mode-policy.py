import json,pathlib,subprocess
root=pathlib.Path('/workspace/seer_originality_chatgpt_bot')
folder=root/'run/setup-2026-10-28T112250Z/selftest'
node='/workspace/nontrading-validation/node-v22.22.0-linux-x64/bin/node'
signer='/workspace/r3-runtime/signer/signer.cjs'
results=[]
for shape in ['bad','good']:
    file=str(folder/('mode-'+shape+'.json'))
    variants=[('extra',['allowlist-off'],None),('flag',['--allowlist-off'],None),('synthetic-env',[],{'SIGNER_ALLOWLIST':'off'})]
    if shape=='bad':variants.append(('sidecar',[],None))
    for name,extra,synthetic in variants:
        kwargs={} if synthetic is None else {'env':synthetic}
        p=subprocess.run([node,signer,'check',file,*extra],cwd=root,capture_output=True,text=True,timeout=30,**kwargs)
        got=json.loads(p.stdout.strip().splitlines()[-1])
        expected='approval-spender' if name=='sidecar' else 'mode-switch'
        passed=p.returncode==3 and got.get('refused')=='allowlist' and got.get('rule')==expected
        results.append({'case':shape+'-'+name,'entrypoint':'check','expected':expected,'exit':p.returncode,'got':got,'pass':passed})
doc={'coverage':'Check-only substitutes for documented send cases 17/18. No send entrypoint exercised; actual send-mode refusal coverage remains untested. Shared offlinePipeline source audited.','cases':results,'passed':sum(r['pass'] for r in results)}
(folder/'mode-results.json').write_text(json.dumps(doc,indent=2)+'\n')
print(json.dumps(doc))
assert all(r['pass'] for r in results)
