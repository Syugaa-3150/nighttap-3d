import asyncio,sys
from playwright.async_api import async_playwright
exec(open('t7.py').read().split('async def main')[0])
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader'])
        pg=await b.new_page(viewport={'width':1280,'height':720})
        errs=[];pg.on('pageerror',lambda e:errs.append(str(e)+(e.stack or '')[:300]))
        pg.on('console',lambda m:errs.append('C:'+m.text[:300]) if m.type=='error' else None)
        await pg.route('**/*',route)
        await pg.goto('file:///home/claude/v2/index.html'); await pg.wait_for_timeout(2000)
        await pg.evaluate("__dbg.renderer.setPixelRatio(0.3);__dbg.renderer.shadowMap.enabled=false")
        await pg.click('#tNew'); await pg.click('[data-sn="1"]'); await pg.click('[data-diff="%s"]'%sys.argv[1]); await pg.wait_for_timeout(200); await pg.click('#tY'); await pg.wait_for_timeout(800)
        await pg.click('#tutBtn')
        await pg.evaluate("(()=>{"+HELP+"})()")
        S="const S=()=>o.push('st '+d.TUTST+' '+(document.querySelector('#tut .tgoals')||{innerText:''}).innerText.replace(/\\n/g,' | '));const up=()=>{d.FPS.on=true;d.camera.rotation.set(-.15,0,0);d.camera.updateMatrixWorld()},dn=()=>{d.FPS.on=true;d.camera.rotation.set(-.7,0,0);d.camera.updateMatrixWorld()};"
        r=await pg.evaluate("""(()=>{const d=__dbg,V=d.V,o=[];"""+S+"""try{
        d.G.lookAcc=2;T.tick(1);S();dn();T.click(d.ST.rack.pint.g.position.clone().add(V(0,.06,-.19)));T.tick(1);d.returnHand();T.tick(1);S();
        T.tick(80);up();const c=d.G.customers[0];T.click(c.m.g.position.clone().add(V(0,1.4,0)));T.tick(2);dn();
        T.click(d.ST.rack.pint.g.position.clone().add(V(0,.06,-.19)));T.click(d.SLOTS.find(s=>s.id==='T0').pos.clone());T.tick(1);d.G.tilt=.8;T.tick(1);
        T.down(d.ST.taps[0].piv.position.clone().add(V(0,.1,0)));T.moveBy(0,80);let i=0;const gl=T.glassOn('T0');while(d.P.act&&gl.fill()<.65&&i++<600)T.tick(1);d.G.tilt=0;while(d.P.act&&i++<900)T.tick(1);T.up();T.tick(2);
        up();T.click(c.m.g.position.clone().add(V(0,1.4,0)));T.tick(2);S();T.tick(200);const s=d.G.seats.find(s=>s.money);T.click(V(0.13+[-.45,0,.45,.9,-.9,1.35,-1.35][s.i],1.13,-.72));T.tick(2);S();
        }catch(e){o.push('ERR '+e.stack)}return o.join('\\n')})()""")
        print(r)
        print('lesson modal:', await pg.evaluate("document.querySelector('#ov').innerText.slice(0,40).replace(/\\n/g,' ')"))
        await pg.click('#lcNext'); await pg.wait_for_timeout(500)
        r=await pg.evaluate("""(()=>{const d=__dbg,V=d.V,o=[];"""+S+"""try{
        T.tick(80);up();const c2=d.G.customers.find(x=>x.status==='waiting');T.click(c2.m.g.position.clone().add(V(0,1.4,0)));T.tick(2);dn();
        T.click(d.ST.garn.g_lemon.position.clone().add(V(0,.03,0)));T.tick(1);for(let n=0;n<2;n++){T.down(d.ST.board.g.position.clone().add(V(0,.03,0)));for(let k=0;k<6;k++)T.moveBy(0,12);T.up();}T.tick(1);S();d.returnHand();
        let n=0;while(d.TUTST===6&&n++<20){d.autoStep();T.tick(1)}S();
        T.down(d.ST.sink.g.position.clone());for(let k=0;k<30;k++)T.moveBy(k%2?-90:90,0);T.up();T.tick(1);
        T.click(d.ST.towel.position.clone().add(V(0,.02,0)));T.tick(1);T.down(V(1.52,.95,-.54));for(let a=0;a<12*Math.PI*2&&d.P.act;a+=.4){const nx=640+Math.cos(a)*60,ny=400+Math.sin(a)*60;d.P.dx=nx-d.P.x;d.P.dy=ny-d.P.y;d.P.x=nx;d.P.y=ny;d.onDrag(Math.hypot(d.P.dx,d.P.dy))}T.up();T.tick(2);S();d.returnHand();
        }catch(e){o.push('ERR '+e.stack)}return o.join('\\n')})()""")
        print(r)
        print('lesson modal:', await pg.evaluate("document.querySelector('#ov').innerText.slice(0,40).replace(/\\n/g,' ')"))
        await pg.click('#lcNext'); await pg.wait_for_timeout(500)
        r=await pg.evaluate("""(()=>{const d=__dbg,V=d.V,o=[];"""+S+"""try{S();
        T.down(d.ST.ri.g.position.clone().add(V(0,.04,0)));for(let a=0;a<20*Math.PI*2&&d.P.act;a+=.4){const nx=640+Math.cos(a)*50,ny=400+Math.sin(a)*50;d.P.dx=nx-d.P.x;d.P.dy=ny-d.P.y;d.P.x=nx;d.P.y=ny;d.onDrag(Math.hypot(d.P.dx,d.P.dy))}T.up();T.tick(2);S();
        T.tick(80);document.querySelector('#tutAct')&&0;const s9=d.TUT[d.TUTST];s9.act.f();T.tick(5);const dc=d.G.customers.find(c=>c.status==='drinking');o.push('drinking '+!!dc);if(dc){d.openTalk(dc);d.answerTalk(0)}T.tick(2);S();
        d.showMood();document.querySelector('[data-li="neon"]').click();document.querySelector('#mClose').click();T.tick(2);S();
        }catch(e){o.push('ERR '+e.stack)}return o.join('\\n')})()""")
        print(r)
        await pg.click('#tutBtn'); await pg.wait_for_timeout(400); await pg.click('#tutBtn'); await pg.wait_for_timeout(1500)
        print(await pg.evaluate("__dbg.S.phase+' day '+__dbg.S.day+' tut '+!!__dbg.G.tutorial+' lessons '+JSON.stringify(__dbg.S.lessons)"))
        print(errs[:5]); await b.close()
asyncio.run(main())
