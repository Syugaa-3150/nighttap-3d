import asyncio
from playwright.async_api import async_playwright
exec(open('t7.py').read().split('async def main')[0])
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader'])
        pg=await b.new_page(viewport={'width':1280,'height':720})
        errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.route('**/*',route)
        await pg.goto('file:///home/claude/v2/index.html')
        await pg.wait_for_timeout(2500)
        await pg.evaluate("__dbg.renderer.setPixelRatio(0.3);__dbg.renderer.shadowMap.enabled=false")
        await pg.click('#tNew'); await pg.click('[data-sn="1"]'); await pg.click('[data-diff="easy"]'); await pg.click('#tN')
        await pg.evaluate("(()=>{"+HELP+"})()")
        await pg.evaluate("for(const k in __dbg.RECIPES)__dbg.S.unlocked[k]=1;for(const k in __dbg.S.stock)__dbg.S.stock[k]=5000")
        r=await pg.evaluate("""(()=>{const d=__dbg,out=[];try{for(const rid of ['pale','ikoi','margarita','tsunrise','umesoda','umerock','ginbuck','highball','stout']){const c=T.order(rid);c.eff=null;let n=0;while(c.status==='ordered'&&n++<15){d.autoStep();T.tick(1)}out.push(rid+' -> '+c.status+' '+JSON.stringify(d.G.lastEval&&[d.G.lastEval.score,d.G.lastEval.notes]));d.G.customers.forEach(x=>{x.m.g.parent&&x.m.g.parent.remove(x.m.g);x.bub.remove()});d.G.customers=[];d.G.seats.forEach(s=>{s.cust=null;s.glasses=[];s.money=0})}}catch(e){out.push('ERR '+e.stack)}return out.join('\\n')})()""")
        print(r);print(errs)
        await b.close()
asyncio.run(main())
