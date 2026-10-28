import json, pathlib, subprocess

root = pathlib.Path('/workspace/seer_originality_chatgpt_bot')
run = root / 'run/setup-2026-10-28T112250Z'
dest = run / 'selftest'
dest.mkdir(exist_ok=True)
node = '/workspace/nontrading-validation/node-v22.22.0-linux-x64/bin/node'
helper = '/workspace/r3-runtime/tools/chain-helper.cjs'
policy = json.loads((root / 'setup/r3-allowlist.json').read_text())
c = policy['contracts']; row = policy['children'][0]
burn = '0x000000000000000000000000000000000000dEaD'
holder = policy['holder']

def encode(signature, *args):
    argv = [json.dumps(a, separators=(',', ':')) if isinstance(a, (list, dict)) else str(a) for a in args]
    result = subprocess.run([node, helper, 'encode', signature, *argv], cwd=root, capture_output=True, text=True, check=True)
    return json.loads(result.stdout)['calldata']

def call(to, signature, *args):
    return {'to': to, 'data': encode(signature, *args), 'value': '0'}

approve = lambda spender, amount=0: call(c['susds'], 'approve(address,uint256)', spender, amount)
good = approve(c['router'])
bad = approve(burn)
def swap(fn, recipient=holder, other=None, fee=None):
    return call(c['swapRouter02'], fn+'((address,address,uint24,address,uint256,uint256,uint160))',
                [row['up'], other or row['repo_token'], fee or row['fee_up'], recipient, '1', '1', '0'])

cases = []
def add(name, expected, payload):
    filename = 'case-%02d.json' % (len(cases)+1)
    (dest / filename).write_text(json.dumps(payload, indent=2)+'\n')
    cases.append({'case': name, 'expected': expected})

add('01-token-transfer', 'token-transfer', [call(c['susds'], 'transfer(address,uint256)', burn, 1)])
add('02-foreign-spender', 'approval-spender', [bad])
add('03-max-approval', 'approval-amount', [approve(c['router'], str(2**256-1))])
add('04-input-recipient', 'recipient', [swap('exactInputSingle', recipient=burn)])
add('05-output-recipient', 'recipient', [swap('exactOutputSingle', recipient=burn)])
add('06-psm-receiver', 'receiver', [call(c['psm3'], 'swapExactIn(address,address,uint256,uint256,address,uint256)', c['usdc'],c['susds'],1,0,burn,0)])
for fn in ['exactInputSingle','exactOutputSingle']:
    add('07-wrong-pair-'+fn, 'swap-pair', [swap(fn, other=c['usdc'])])
for fn in ['exactInputSingle','exactOutputSingle']:
    add('08-wrong-fee-'+fn, 'swap-fee-tier', [swap(fn, fee=500)])
add('09-wrong-psm-pair','psm3-pair',[call(c['psm3'],'swapExactIn(address,address,uint256,uint256,address,uint256)',c['usdc'],c['usds'],1,0,holder,0)])
add('10-unlisted-market','router-market',[call(c['router'],'splitPosition(address,address,uint256)',c['susds'],burn,1)])
add('11-native-value','native-value',[dict(good,value='1')])
add('12-unlisted-selector','selector',[dict(good,data='0x12345678')])
add('13-permit','eip712',{'types':{'Permit':[{'name':'spender','type':'address'}]},'primaryType':'Permit','domain':{'chainId':10},'message':{'spender':burn}})
add('14-7702','eip7702',{'chainId':10,'address':burn,'nonce':0})
add('15-bad-call-in-list','approval-spender@1',[good,bad,good])
add('16-allowed','allowed',[good])
add('17-check-input-mode-key','mode-switch',{'calls':[bad],'allowlist':False})
add('18-check-input-mode-key','mode-switch',{'calls':[good],'allowlist':False})
(dest/'results.json').write_text(json.dumps({'cases':cases},indent=2)+'\n')
(dest/'mode-good.json').write_text(json.dumps([good])+'\n')
(dest/'mode-bad.json').write_text(json.dumps([bad])+'\n')
(dest/'mode-bad.json.allowlist.json').write_text(json.dumps({'allowlist':False})+'\n')
(run/'split.json').write_text(json.dumps([call(c['router'],'splitPosition(address,address,uint256)',c['susds'],policy['parent']['market'],1)],indent=2)+'\n')
groups=[{'calls':[approve(c['router'],1),call(c['router'],'splitPosition(address,address,uint256)',c['susds'],policy['parent']['market'],1)]},
        {'calls':[call(policy['middles'][0]['bundle_token'],'approve(address,uint256)',c['router'],1),call(c['router'],'splitPosition(address,address,uint256)',c['susds'],policy['middles'][0]['market'],1)]}]
(run/'helper-two-groups.json').write_text(json.dumps(groups,indent=2)+'\n')
print('Prepared',len(cases),'expected-only cases; no observed results fabricated')
