# 開発版 /home/claude/v2/index.html → 公開版（リポジトリ直下の index.html）
import os,re
here=os.path.dirname(os.path.abspath(__file__))
s=open('/home/claude/v2/index.html',encoding='utf-8').read()
s=re.sub(r'\nwindow\.__dbg=\{.*\};$','',s,count=1,flags=re.M)
s=s.replace(' ws://127.0.0.1:8765','')
assert '__dbg' not in s and '8765' not in s
assert 'connect-src wss://0.peerjs.com;' in s
open(os.path.join(here,'..','index.html'),'w',encoding='utf-8').write(s)
print('ok index.html')
