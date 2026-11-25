import asyncio,sys,json
from playwright.async_api import async_playwright
exec(open('t7.py').read().split('async def main')[0])
IDS=sys.argv[1].split(',') if len(sys.argv)>1 else "flip,high,double,back,roll,juggle,juggle3,tin,icetoss,shake,dshake,freepour,longpour,layer,icecarve,art2,longslide".split(',')
SHOT=sys.argv[2].split(',') if len(sys.argv)>2 else []
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader'])
        pg=await b.new_page(viewport={'width':1280,'height':720})
        errs=[];pg.on('pageerror',lambda e:errs.append(str(e)+(e.stack or '')[:400]))
        await pg.add_init_script("localStorage.setItem('nighttap3d_settings',JSON.stringify({viewMode:'cursor'}))")
        await pg.route('**/*',route)
        await pg.goto('file:///home/claude/v2/index.html'); await pg.wait_for_timeout(2500)
        await pg.evaluate("__dbg.renderer.setPixelRatio(0.3);__dbg.renderer.shadowMap.enabled=false")
        await pg.click('#tNew'); await pg.click('[data-sn="1"]'); await pg.click('[data-diff="normal"]'); await pg.click('#tN'); await pg.wait_for_timeout(800)
        await pg.evaluate("(()=>{const d=__dbg;for(const k in d.RECIPES)d.S.unlocked[k]=1;for(const k in d.S.stock)d.S.stock[k]=5000;d.S.money=500000;})()")
        print(await pg.evaluate("__dbg.S.phase+' tut '+!!__dbg.G.tutorial"))
        for sid in IDS:
            r=await pg.evaluate("""(sid)=>{const d=__dbg;d.S.skills[sid]=1;const m0=d.S.money,st0=d.S.stock.gin;d.pracStart(sid);return 'start '+sid+' demo='+(d.PRAC&&d.PRAC.demo)}""",sid)
            print(r,flush=True)
            shot = sid in SHOT
            for i in range(60):
                busy=await pg.evaluate('''(n)=>{const d=__dbg;for(let i=0;i<n;i++){if(!d.PRAC||!(d.PRAC.demo||d.PRAC.drive))break;d.pracTick(.05);if(d.S.phase==='service'&&!d.G.paused)d.update(.05*(d.PRAC?d.PRAC.spd:1));d.computeHand()}return !!(d.PRAC&&(d.PRAC.demo||d.PRAC.drive))}''',25)
                if shot and i==3: await pg.screenshot(path=f'/home/claude/pr_{sid}.png',timeout=120000)
                if not busy: break
            print('  demo done after',i,'state',await pg.evaluate("JSON.stringify({ng:__dbg.PRAC&&__dbg.PRAC.ngMsg,txt:document.querySelector('#pracBox').innerText.slice(0,80)})"))
            res=[]
            for stg in (1,2):
                await pg.evaluate(f"__dbg.pracStage({stg})")
                for tries in range(4):
                    ok0=await pg.evaluate("__dbg.PRAC?__dbg.PRAC.ok:-1")
                    st=await pg.evaluate("__dbg.PRAC?__dbg.PRAC.stage:-1")
                    if st!=stg or await pg.evaluate("!!(__dbg.PRAC&&__dbg.PRAC.cleared)"): break
                    await pg.evaluate("__dbg.pracDrive()")
                    for i in range(60):
                        busy=await pg.evaluate('''(n)=>{const d=__dbg;for(let i=0;i<n;i++){if(!d.PRAC||!(d.PRAC.demo||d.PRAC.drive))break;d.pracTick(.05);if(d.S.phase==='service'&&!d.G.paused)d.update(.05*(d.PRAC?d.PRAC.spd:1));d.computeHand()}return !!(d.PRAC&&(d.PRAC.demo||d.PRAC.drive))}''',25)
                        if not busy: break
                    await pg.evaluate("(()=>{const d=__dbg;for(let i=0;i<30;i++){d.update(.05);d.pracTick(.05)}})()")
                    await pg.wait_for_timeout(1500)
                    res.append((stg,await pg.evaluate("__dbg.PRAC?[__dbg.PRAC.stage,__dbg.PRAC.ok,!!__dbg.PRAC.cleared,__dbg.PRAC.ngMsg||'']:null")))
            print('  ',res,flush=True)
            r=await pg.evaluate("""(()=>{const d=__dbg;const cl=d.PRAC&&d.PRAC.cleared;d.pracEnd();return 'cleared='+cl+' after end: prac='+!!d.PRAC+' G.prac='+d.G.prac+' phase='+d.S.phase+' glasses='+d.GLASSOBJS.length+' gin='+Math.round(d.S.stock.gin)+' money='+d.S.money})()""")
            print('  ',r,flush=True)
            await pg.wait_for_timeout(600)
        print('errs',errs[:6]); await b.close()
asyncio.run(main())
