""" Asynchronously download a list of webpages and time it

Dependencies: Make sure you instanll aiohttp

pip install aiohttp aiodns

"""
import asyncio
import aiohttp
from time import time

sites = [
        "http://news.ycombinator.com/",
        "https://www.yahoo.com/",
        "http://www.aliexpress.com/",
        "http://deelay.me/5000/http://deelay.me/",
]

async def find_size(session, url):
    async with session.get(url) as response:
        page = await response.read()
        return len(page)

async def show_size(session, url):
    size = await find_size(session, url)
    print("Read {:8d} chars from {}".format(size, url))

async def main(loop):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for site in sites:
            tasks.append(loop.create_task(show_size(session, site)))
        await asincio.wait(tasks)

if __name__ == '__main__':
    start_time = time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    print("Ran in {:6.3f} secs".format(time() - start_time))
