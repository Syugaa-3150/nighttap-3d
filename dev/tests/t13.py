import asyncio,sys
from playwright.async_api import async_playwright
exec(open('t7.py').read().split('async def main')[0])
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader'])
        pg=await b.new_page(viewport={'width':1280,'height':720})
        errs=[];pg.on('pageerror',lambda e:errs.append(str(e)+(e.stack or '')[:400]))
        await pg.add_init_script("localStorage.setItem('nighttap3d_settings',JSON.stringify({viewMode:'cursor'}))")
        await pg.route('**/*',route)
        await pg.goto('file:///home/claude/v2/index.html'); await pg.wait_for_timeout(2500)
        await pg.evaluate("__dbg.renderer.setPixelRatio(0.3);__dbg.renderer.shadowMap.enabled=false")
        await pg.click('#tNew'); await pg.click('[data-sn="1"]'); await pg.click('[data-diff="easy"]'); await pg.click('#tN'); await pg.wait_for_timeout(800)
        await pg.evaluate("(()=>{"+HELP+"})()")
        await pg.evaluate("(()=>{const d=__dbg;for(const k in d.RECIPES)d.S.unlocked[k]=1;for(const k in d.S.stock)d.S.stock[k]=5000;d.S.money=500000;for(const s of d.SKILLS)d.S.skills[s.id]=1;d.S.glasses.rock=6;d.G.clean.rock=6})()")
        # layer recipes + combo + shaped ice via autoStep
        r=await pg.evaluate("""(()=>{const d=__dbg,out=[];try{for(const rid of []){const c=T.order(rid);c.eff=null;let n=0;while(c.status==='ordered'&&n++<20){d.autoStep();T.tick(1)}out.push(rid+' -> '+c.status+' '+JSON.stringify(d.G.lastEval&&[d.G.lastEval.score,d.G.lastEval.notes]));d.G.customers.forEach(x=>{x.m.g.parent&&x.m.g.parent.remove(x.m.g);x.bub.remove()});d.G.customers=[];d.G.seats.forEach(s=>{s.cust=null;s.glasses=[];s.money=0});Object.assign(d.G.clean,{pint:6,highball:6,cocktail:6,mug:6})}}catch(e){out.push('ERR '+e.stack)}return out.join('\\n')})()""")
        print(r)
        # long slide direct + combo
        r=await pg.evaluate("""(()=>{const d=__dbg;try{const c=T.order('highball');c.eff=null;let n=0;while(c.status==='ordered'&&n++<8){const st=d.steps(d.RC?d.RC(c):c.order);const nx=st.find(x=>!x.d);if(!nx||nx.ak==='serve')break;d.autoStep();T.tick(1)}
          const w=d.SLOTS.find(s=>s.glass&&s.glass.type==='highball').glass;w.c.tricks=['ダブルスピン','ロングポア'];d.SLOTS.forEach(s=>{if(s.glass===w)s.glass=null});w.loc={kind:'hand'};d.H={kind:'glass',glass:w};
          const q=d.toScreen(c.m.g.position.clone());d.P.x=q.x;d.P.y=500;d.trySlide({},1200);T.tick(30);return 'slide -> '+c.status+' tricks '+JSON.stringify(c.served&&c.served.c.tricks)+' lastEval '+JSON.stringify(d.G.lastEval&&d.G.lastEval.score)+' hl '+JSON.stringify(d.G.hl.tricks)}catch(e){return 'ERR '+e.stack}})()""")
        print(r)
        # shop-phase practice start/end
        r=await pg.evaluate("""(()=>{const d=__dbg;d.S.phase='shop';d.openShop('skill');const n=document.querySelectorAll('[data-prac]').length;const a0=1;const a='prac from shop: phase='+d.S.phase+' G.prac='+d.G.prac+' btns='+n;return a+' | after: phase='+d.S.phase+' ov='+document.querySelector('#ov').classList.contains('show')+' txt='+document.querySelector('#ov').innerText.slice(0,30).replace(/\\n/g,' ')})()""")
        print(r)
        await pg.screenshot(path='/home/claude/skilltab.png',timeout=120000)
        r=await pg.evaluate("""(()=>{const d=__dbg;d.pracStart('flip');d.goTitle();return 'goTitle: prac='+!!d.PRAC+' phase='+d.S.phase})()""")
        print(r)
        print('errs',errs[:6]); await b.close()
asyncio.run(main())
