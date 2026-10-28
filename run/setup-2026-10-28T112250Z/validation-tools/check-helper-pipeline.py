import json,pathlib,subprocess,hashlib,datetime
root=pathlib.Path('/workspace/seer_originality_chatgpt_bot')
run=root/'run/setup-2026-10-28T112250Z'
node='/workspace/nontrading-validation/node-v22.22.0-linux-x64/bin/node'
helper='/workspace/r3-runtime/tools/chain-helper.cjs'
policy=json.loads((root/'setup/r3-allowlist.json').read_text())
def H(*args):
    p=subprocess.run([node,'--use-env-proxy','--use-system-ca',helper,*args],cwd=root,capture_output=True,text=True,timeout=150)
    d=json.loads(p.stdout)
    if p.returncode:raise RuntimeError(json.dumps(d))
    return d
def rpc(to,data,block):
    payload={'jsonrpc':'2.0','id':1,'method':'eth_call','params':[{'to':to,'data':data},hex(block)]}
    p=subprocess.run(['curl','--fail','--silent','--show-error','--max-time','30','--header','Content-Type: application/json','--data',json.dumps(payload),'https://mainnet.optimism.io/'],capture_output=True,text=True,timeout=33,check=True)
    return json.loads(p.stdout)['result']
pool=policy['children'][0]['pool_up']
slot=H('slot0',pool)
data=H('encode','slot0()(uint160,int24,uint16,uint16,uint16,uint8,bool)')['calldata']
raw=rpc(pool,data,slot['block'])[2:]
sqrt=int(raw[:64],16);tick=int(raw[64:128],16)
if tick>=2**255:tick-=2**256
assert str(sqrt)==slot['sqrt_price_x96'] and tick==slot['tick']
condition=H('call',policy['parent']['market'],'conditionId()(bytes32)')['result'][0]
denom=H('call',policy['contracts']['ctf'],'payoutDenominator(bytes32)(uint256)',condition)
data=H('encode','payoutDenominator(bytes32)(uint256)',condition)['calldata']
independent=int(rpc(policy['contracts']['ctf'],data,denom['block']),16)
assert str(independent)==denom['result'][0]
split=subprocess.run([node,'/workspace/r3-runtime/signer/signer.cjs','check',str(run/'split.json')],cwd=root,capture_output=True,text=True,timeout=30)
assert split.returncode==0 and json.loads(split.stdout).get('allowed') is True
sim=H('simulate',str(run.relative_to(root)/'helper-two-groups.json'))
assert sim['all_success'] and sim['count']==4 and sim['entries']==2
assert all(c[2]=='0x1' and c[4] is not None for c in sim['calls'])
report={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'helper_sha256':hashlib.sha256(pathlib.Path(helper).read_bytes()).hexdigest(),'slot0':slot,'independent_slot0_match':True,'payout_denominator':denom,'independent_payout_denominator_match':True,'split_check':json.loads(split.stdout),'two_group_simulation':sim,'no_max_used_gas':False,'independent_read_scope':'Independent curl eth_call at matching block via the same approved public endpoint; no second provider accessed'}
(run/'helper-validation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
