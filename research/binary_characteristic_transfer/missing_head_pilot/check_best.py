import p2_nonfield as f,json
from pathlib import Path
u,v,k=f.out[0]['head_line'];m=f.M[u][f.inv[v]];b=f.M[k][f.inv[v]]
receipts=[]
for rec in f.G[(u,v,k)]:
 E,C,B,A,_=rec['locator'];t=(f.pw(A,4),1); vv=(b^f.pw(B,4)^f.pw(A,6),m^f.pw(A,2))
 coeff=[]
 for j in range(7):
  a0=a1=0
  if j>=2:a0^=f.pw(rec['locator'][j-2],4)
  if 1<=j<=5:
   c=f.pw(rec['locator'][j-1],2);a0^=f.M[t[0]][c];a1^=f.M[t[1]][c]
  if j<=4:
   c=rec['locator'][j];a0^=f.M[vv[0]][c];a1^=f.M[vv[1]][c]
  coeff.append((a0,a1))
 assert coeff[2]==(0,0) and coeff[4]==(b,m) and coeff[5]==(0,1) and coeff[6]==(1,0)
 support=[]
 for x in range(128):
  if x==0: value=coeff[0]
  else:
   v0=v1=0;y=x
   for c0,c1 in coeff:v0^=f.M[c0][y];v1^=f.M[c1][y];y=f.M[y][y]
   value=(v0,v1)
  if value==(0,0):support.append(x)
 assert len(support)==15
 receipts.append({'locator':rec['locator'],'label_pair':coeff[3],'witness_constant_pair':coeff[0],'witness_X_pair':coeff[1],'support':support})
assert len({tuple(r['label_pair']) for r in receipts})==16
Path(__file__).with_suffix('.json').write_text(json.dumps({'head_theta1':'theta outside F256','head_theta2':[b,m],'N':128,'degree_cap':1,'agreements':15,'labels':16,'receipts':receipts},indent=2))
print('Exact best group: 16 distinct labels, each exactly15 matches, degree<=1 witnesses.')
