from aiohttp import web

async def handle(request):
    return web.FileResponse('index.html')

async def web_server():
    app = web.Application()
    app.router.add.get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.getenv("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()




