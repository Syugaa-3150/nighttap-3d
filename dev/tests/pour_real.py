import asyncio,json
from playwright.async_api import async_playwright
exec(open('t7.py').read().split('async def main')[0])
KS="tomato,pine,grapefruit,oolong,coconut,grenadine,redwine,whitewine,sparkling,peachl,lychee,blue,campari,orange,gin".split(',')
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader'])
        pg=await b.new_page(viewport={'width':1280,'height':720})
        errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.add_init_script("localStorage.setItem('nighttap3d_settings',JSON.stringify({viewMode:'cursor'}))")
        await pg.route('**/*',route)
        await pg.goto('file:///home/claude/v2/index.html'); await pg.wait_for_timeout(2500)
        await pg.evaluate("__dbg.renderer.setPixelRatio(0.3)")
        await pg.click('#tNew'); await pg.click('[data-sn="1"]'); await pg.click('[data-diff="normal"]'); await pg.click('#tN'); await pg.wait_for_timeout(800)
        await pg.evaluate("(()=>{"+HELP+"})()")
        await pg.evaluate("(()=>{const d=__dbg;for(const k in d.RECIPES)d.S.unlocked[k]=1;for(const k in d.S.stock)d.S.stock[k]=5000;d.S.money=500000;for(const k in d.S.glassOwn||{})d.S.glassOwn[k]=1})()")
        res={}
        for k in KS:
            r=await pg.evaluate("""(k)=>{const d=__dbg,V=d.V;try{
              d.returnHand();T.tick(1);
              // glass on mat A
              const A=d.SLOTS.find(s=>s.id==='A');
              if(!A.glass){T.click(d.ST.rack.highball.g.position.clone().add(V(0,.06,-.19)));T.click(A.pos.clone());T.tick(1)}
              const gl=A.glass;if(!gl)return 'no glass';for(const q in gl.c.ings)delete gl.c.ings[q];
              const bt=d.ST.bottles[k];const yaw=bt.position.x<-1.2?0:1;d.cvSet(1,bt.position.x<-1.2?0:(bt.position.x>1?2:1));
              d.camera.rotation.set(-.55,bt.position.x<-1.2?.75:0,0);d.scene.updateMatrixWorld();d.camera.updateMatrixWorld();
              T.click(bt.position.clone().add(V(0,.1,0)));T.tick(1);
              const held=d.H&&d.H.kind==='bottle'&&d.H.k===k;
              d.camera.rotation.set(-.6,0,0);d.camera.updateMatrixWorld();
              T.down(gl.m?gl.m.position.clone().add(V(0,.15,0)):A.pos.clone().add(V(0,.15,0)));T.moveBy(40,0);
              let i=0;while(d.P.down&&i++<30)T.tick(1);T.up();T.tick(1);
              return JSON.stringify({held,ml:Math.round(gl.c.ings[k]||0),act:!!d.P.act})}catch(e){return 'ERR '+e.message}}""",k)
            res[k]=r;print(k,r,flush=True)
        print(errs[:3]); await b.close()
asyncio.run(main())
