#!/usr/bin/env python3
# -*- coding: utf-8 -8-

__author__ = 'hzzdaxia'

'''
This is a async web application
'''


import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web, web_runner

def index(request):
    return web.Response(body='<h1>Awesome</h>'.encode(), content_type='text/html')

async def init(loop):
    app = web.Application(loop=loop)
    app = web_runner.AppRunner(app=app).app()
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app._make_handler(), '127.0.0.1', 9000)
    logging.info('Server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()