import asyncio,sys
from playwright.async_api import async_playwright
exec(open('t7.py').read().split('async def main')[0])
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader'])
        pg=await b.new_page(viewport={'width':1280,'height':720})
        errs=[];pg.on('pageerror',lambda e:errs.append(str(e)+(e.stack or '')[:400]))
        pg.on('console',lambda m:errs.append('C:'+m.text[:400]) if m.type=='error' else None)
        await pg.route('**/*',route)
        await pg.goto('file:///home/claude/v2/index.html'); await pg.wait_for_timeout(2000)
        await pg.evaluate("__dbg.renderer.setPixelRatio(0.2);__dbg.renderer.shadowMap.enabled=false")
        await pg.click('#tNew'); await pg.click('[data-sn="1"]'); await pg.click('[data-diff="%s"]'%sys.argv[1]); await pg.click('#tN'); await pg.wait_for_timeout(1000)
        await pg.evaluate("for(const k in __dbg.RECIPES)__dbg.S.unlocked[k]=1;for(const k in __dbg.S.stock)__dbg.S.stock[k]=50000;__dbg.S.day=6;__dbg.S.up.seats=7")
        await pg.evaluate("(()=>{"+HELP+"})()")
        r=await pg.evaluate("""(()=>{const d=__dbg,o=[];const G=()=>d.G;d.newDay();T.tick(1);G().special={k:'critic',t:.05};G().partyAt=.1;let served=0,stuck=[];
          for(let step=0;step<3000;step++){T.tick(1);
            for(const c of G().customers){if(c.status==='waiting'&&Math.random()<.3)d.clickCust(c);if(c.status==='drinking'&&!c.talked&&Math.random()<.01){d.openTalk(c);d.answerTalk(Math.floor(Math.random()*3))}if(c.quarrel&&Math.random()<.05)d.calmQuarrel(c)}
            if(d.activeCust()&&Math.random()<.5){d.autoStep()}
            for(const s of G().seats){if((s.money||s.glasses.length)&&Math.random()<.05)d.collect(s)}
            if(G().dirty.length&&Math.random()<.05){d.washOne&&d.washOne()}
            if(G().ended)break}
          // consistency checks
          const servedGl=d.GLASSOBJS?d.GLASSOBJS.filter(g=>g.loc&&g.loc.kind==='served'):[];
          for(const g of servedGl){if(!G().customers.some(c=>c.served===g))stuck.push('orphan served glass '+g.type)}
          for(const c of G().customers){if(c.status==='drinking'&&!c.served)stuck.push('drinking w/o glass '+c.id)}
          return 'served '+G().stats.served+' custs '+G().customers.map(c=>c.status).join(',')+' time '+G().time.toFixed(0)+'/'+G().dayLen+' stuck '+JSON.stringify(stuck)})()""")
        print(r)
        print('\n'.join(errs[:8]))
        await b.close()
asyncio.run(main())
