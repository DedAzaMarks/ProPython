import asyncio
import aiohttp
import aiofiles
import os
import sys
from bs4 import BeautifulSoup
from urllib.parse import urljoin

async def fetch_html(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def download_image(session, url, folder, filename):
    async with session.get(url) as response:
        filepath = os.path.join(folder, filename)
        async with aiofiles.open(filepath, 'wb') as f:
            while True:
                chunk = await response.content.read(1024)
                if not chunk:
                    break
                await f.write(chunk)
        print(f"Downloaded {filename}")

async def extract_image_urls(html):
    soup = BeautifulSoup(html, 'html.parser')
    img_tag = soup.find_all('img')
    return img_tag[0]['src']

async def download_images(num_images, folder):
    url = 'https://www.thiswaifudoesnotexist.net/'
    async with aiohttp.ClientSession() as session:
        html = await fetch_html(url)
        image_url = await extract_image_urls(html)
        image_url = urljoin(url, image_url)
        tasks = []
        for i in range(num_images):
            filename = f'{i}.jpg'
            task = asyncio.create_task(download_image(session, image_url, folder, filename))
            tasks.append(task)
        await asyncio.gather(*tasks)

async def main():
    num_images = 5
    if len(sys.argv) == 2:
        num_images = int(sys.argv[1])
    folder = 'artifacts'
    if not os.path.exists(folder):
        os.makedirs(folder)
    await download_images(num_images, folder)

if __name__ == '__main__':
    asyncio.run(main())
