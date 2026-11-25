import asyncio,sys,json
from playwright.async_api import async_playwright
ROOT='/home/claude/v2/node_modules/three/'
async def route(r):
    u=r.request.url
    if 'cdn.jsdelivr.net/npm/three@0.160.0/' in u:
        await r.fulfill(path=ROOT+u.split('three@0.160.0/')[1],content_type='application/javascript')
    elif 'fonts.g' in u: await r.abort()
    else: await r.continue_()
HELP="""
window.T={};const d=__dbg,V=d.V;
T.at=v=>{d.scene.updateMatrixWorld();const p=d.toScreen(v);d.P.x=p.x;d.P.y=p.y};
T.down=v=>{T.at(v);d.P.down=true;d.P.moved=0;d.computeHand();d.onDown()};
T.up=()=>{d.P.down=false;d.onUp()};
T.click=v=>{T.down(v);T.up()};
T.moveBy=(dx,dy)=>{d.P.x+=dx;d.P.y+=dy;d.P.dx=dx;d.P.dy=dy;d.computeHand();d.onDrag(Math.hypot(dx,dy))};
T.tick=n=>{for(let i=0;i<n;i++)d.update(0.05)};
T.st=()=>{const c=d.activeCust();return c?d.steps(c.order).map(s=>(s.d?'✓':'·')+s.t+(s.amt?'('+s.amt+')':'')).join(' | '):'none'};
T.hand=()=>d.H?d.H.kind+(d.H.k||'')+(d.H.glass?d.H.glass.type:''):'-';
T.cust=()=>d.G.customers.find(c=>c.status==='waiting'||c.status==='ordered');
T.order=(rid)=>{let c=T.cust();if(!c){d.spawnCustomer(true);T.tick(80);c=T.cust()}c.status='waiting';d.clickCust(c);c.order=rid;c.pat=c.patMax=999;d.G.active=c.id;return c};
T.glassOn=id=>d.SLOTS.find(s=>s.id===id).glass;
"""
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader'])
        pg=await b.new_page(viewport={'width':1280,'height':720})
        errs=[]
        pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.route('**/*',route)
        await pg.goto('file:///home/claude/v2/index.html')
        await pg.wait_for_timeout(2000)
        await pg.evaluate("__dbg.renderer.setPixelRatio(0.3);__dbg.renderer.shadowMap.enabled=false")
        await pg.click('#tNew'); await pg.click('#hGo')
        await pg.evaluate("for(const k in __dbg.RECIPES)__dbg.S.unlocked[k]=1;for(const k in __dbg.S.stock)__dbg.S.stock[k]=5000")
        await pg.mouse.move(640,500); await pg.wait_for_timeout(1500)
        await pg.evaluate("(()=>{"+HELP+"})()")
        r=await pg.evaluate("""(()=>{const d=__dbg,V=d.V,out=[];try{
          const c=T.order('pale');out.push(T.st());
          T.click(d.ST.rack.pint.g.position.clone().add(V(0,.06,-.19)));out.push('hand '+T.hand());
          T.click(d.SLOTS.find(s=>s.id==='T0').pos.clone());out.push('T0 '+!!T.glassOn('T0')+' hand '+T.hand());
          T.down(d.ST.taps[0].piv.position.clone().add(V(0,.1,0)));T.moveBy(0,70);
          let gl=T.glassOn('T0');let i=0;while(gl.fill()<.78&&i++<400)T.tick(1);T.moveBy(0,45);i=0;while(gl.fill()<.93&&i++<400)T.tick(1);T.up();T.tick(10);
          out.push('fill '+gl.fill().toFixed(2)+' foam '+(gl.c.foam/(gl.liquid()+gl.c.foam)).toFixed(2));
          out.push(T.st());
          T.click(gl.g.position.clone().add(V(0,.07,0)));out.push('hand '+T.hand());
          T.click(c.m.g.position.clone().add(V(0,1.35,0)));out.push(JSON.stringify(d.G.lastEval));
          }catch(e){out.push('ERR '+e.message)}return out.join('\\n')})()""")
        print(r)
        r=await pg.evaluate("""(()=>{const d=__dbg,V=d.V,out=[];try{
          const c=T.order('highball');
          T.click(d.ST.rack.highball.g.position.clone().add(V(0,.06,-.19)));T.click(d.SLOTS.find(s=>s.id==='A').pos.clone());out.push('A '+!!T.glassOn('A'));
          const gl=T.glassOn('A');
          T.click(d.ST.ice.position.clone().add(V(0,.06,0)));out.push('hand '+T.hand());T.click(gl.g.position.clone().add(V(0,.1,0)));out.push('ice '+gl.c.ice);
          T.click(d.ST.bottles.whisky.position.clone().add(V(0,.12,0)));out.push('hand '+T.hand());
          T.down(gl.g.position.clone().add(V(0,.1,0)));let i=0;while((gl.c.ings.whisky||0)<29&&i++<400)T.tick(1);T.up();out.push('whisky '+gl.c.ings.whisky);
          T.click(d.ST.bottles.soda.position.clone().add(V(0,.12,0)));out.push('hand '+T.hand());
          T.down(gl.g.position.clone().add(V(0,.1,0)));T.moveBy(0,60);i=0;while(gl.fill()<.88&&i++<400)T.tick(1);T.up();out.push('fill '+gl.fill().toFixed(2));
          d.H=null;T.click(d.ST.spoon.position.clone().add(V(0,.15,0)));out.push('hand '+T.hand());
          const cs=d.toScreen(gl.g.position.clone().add(V(0,.1,0)));T.down(gl.g.position.clone().add(V(0,.1,0)));
          for(let a=0;a<6.2*Math.PI*2;a+=.3){d.P.x=cs.x+Math.cos(a)*40;d.P.y=cs.y+Math.sin(a)*40;d.onDrag(5)}T.up();out.push('stir '+gl.c.stirred);
          d.H=null;T.click(d.ST.garn.g_lemon.position.clone().add(V(0,.03,0)));out.push('hand '+T.hand());T.click(gl.g.position.clone().add(V(0,.1,0)));out.push('garn '+gl.c.garnish);
          out.push(T.st());
          T.click(gl.g.position.clone().add(V(0,.07,0)));T.click(c.m.g.position.clone().add(V(0,1.35,0)));out.push(JSON.stringify(d.G.lastEval));
          }catch(e){out.push('ERR '+e.message)}return out.join('\\n')})()""")
        print(r)
        r=await pg.evaluate("""(()=>{const d=__dbg,V=d.V,out=[];try{
          const c=T.order('daiquiri');const sh=d.G.shaker;
          T.click(sh.g.position.clone().add(V(0,.08,0)));out.push('hand '+T.hand());
          T.click(d.SLOTS.find(s=>s.id==='B').pos.clone());out.push('B '+(T.glassOn('B')===sh));
          T.click(d.ST.ice.position.clone().add(V(0,.06,0)));T.click(sh.g.position.clone().add(V(0,.1,0)));out.push('ice '+sh.c.ice);
          for(const [k,t] of [['rum',45],['limej',15],['syrup',10]]){T.click(d.ST.bottles[k].position.clone().add(V(0,.22,0)));T.down(sh.g.position.clone().add(V(0,.1,0)));let i=0;while((sh.c.ings[k]||0)<t-0.6&&i++<500)T.tick(1);T.up();out.push(k+' '+(sh.c.ings[k]||0).toFixed(1))}
          d.H=null;T.click(sh.g.position.clone().add(V(0,.08,0)));out.push('hand '+T.hand());
          T.down(V(-.6,1.0,-.2));for(let i=0;i<70;i++){T.moveBy(i%2?-80:80,0)}T.up();out.push('shaken '+sh.c.shaken);
          T.click(d.SLOTS.find(s=>s.id==='B').pos.clone());
          out.push('hand after '+T.hand()+' shloc '+JSON.stringify(sh.loc.kind));
          if(d.H&&d.H.glass===sh){d.H=null;d.SLOTS.find(s=>s.id==='B').glass=sh;sh.loc={kind:'slot',slot:d.SLOTS.find(s=>s.id==='B')}}
          T.click(d.ST.rack.cocktail.g.position.clone().add(V(0,.06,-.19)));T.click(d.SLOTS.find(s=>s.id==='A').pos.clone());const gl=T.glassOn('A');out.push('A '+(gl&&gl.type));
          T.click(sh.g.position.clone().add(V(0,.08,0)));out.push('hand '+T.hand());
          T.down(gl.g.position.clone().add(V(0,.1,0)));out.push('act '+(d.P.act&&d.P.act.kind));T.tick(60);T.up();
          out.push('gl '+JSON.stringify(gl.c));
          out.push(T.st());
          d.H=null;T.click(gl.g.position.clone().add(V(0,.1,0)));T.click(c.m.g.position.clone().add(V(0,1.35,0)));out.push(JSON.stringify(d.G.lastEval));
          }catch(e){out.push('ERR '+e.message)}return out.join('\\n')})()""")
        print(r)
        await pg.wait_for_timeout(2500)
        await pg.screenshot(path='/home/claude/u7.png')
        print(errs)
        await b.close()
asyncio.run(main())
