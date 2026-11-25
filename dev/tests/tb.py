import asyncio
from playwright.async_api import async_playwright
exec(open('t7.py').read().split('async def main')[0])
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader'])
        pg=await b.new_page(viewport={'width':1280,'height':720})
        errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.route('**/*',route)
        await pg.goto('file:///home/claude/site/index.html'); await pg.wait_for_timeout(3000)
        await pg.click('#tNew'); await pg.click('[data-sn="1"]'); await pg.click('[data-diff="easy"]'); await pg.click('#tN'); await pg.wait_for_timeout(4000)
        print('errs',errs[:3]); await b.close()
asyncio.run(main())
