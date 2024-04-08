import asyncio
import aiohttp
import aiofiles
import os
import sys
import hashlib
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin


async def fetch_html(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def download_image(session, url):
    async with session.get(url) as response:
        return await response.read()

async def extract_image_urls(html):
    soup = BeautifulSoup(html, 'html.parser')
    img_tags = soup.find_all('img')
    return [tag['src'] for tag in img_tags]

async def calculate_hash(image):
    hasher = hashlib.sha256()
    hasher.update(image)
    return hasher.hexdigest()

async def download_images(num_images, folder):
    url = 'https://www.thiswaifudoesnotexist.net/'
    async with aiohttp.ClientSession() as session:
        downloaded_hashes = set()
        for i in range(num_images):
            for attempt in range(5):
                html = await fetch_html(url)
                image_urls = await extract_image_urls(html)
                image_url = image_urls[0]
                image_url = urljoin(url, image_url)
                print(f'Try {attempt} for {image_url}')
                filename = f'{i}.jpg'
                filepath = os.path.join(folder, filename)
                image = await download_image(session, image_url)
                image_hash = await calculate_hash(image)
                if image_hash not in downloaded_hashes:
                    downloaded_hashes.add(image_hash)
                    async with aiofiles.open(filepath, 'wb') as f:
                            await f.write(image)
                    print(f"Downloaded {filename}")
                    break
                else:
                    print(f"Duplicate image found. Waiting for 1 second...")
                    await asyncio.sleep(1)

async def main():
    num_images = 5
    if len(sys.argv) == 2:
        num_images = int(sys.argv[1])
    folder = 'artifacts'
    if not os.path.exists(folder):
        os.makedirs(folder)
    await download_images(num_images, folder)

asyncio.run(main())
