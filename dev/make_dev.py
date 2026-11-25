# 公開版 index.html から開発版（__dbg 入り）を作る。
# 使い方: python3 dev/make_dev.py  → /home/claude/v2/index.html
import os
here=os.path.dirname(os.path.abspath(__file__))
s=open(os.path.join(here,'..','index.html'),encoding='utf-8').read()
dbg=open(os.path.join(here,'dbg_line.js'),encoding='utf-8').read().strip()
assert '__dbg' not in s
k='\n</script>'
i=s.rindex(k)  # 最後のモジュールスクリプトの閉じタグ直前に差し込む
os.makedirs('/home/claude/v2',exist_ok=True)
open('/home/claude/v2/index.html','w',encoding='utf-8').write(s[:i]+'\n'+dbg+s[i:])
print('ok /home/claude/v2/index.html')
