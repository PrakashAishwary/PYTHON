import asyncio
import aiohttp
import os

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

urls = [
    "https://example.com/file1.jpg",
    "https://example.com/file2.pdf",
    "https://example.com/file3.png",
]

async def download_file(session, url):
    filename = os.path.join(DOWNLOAD_DIR, url.split('/')[-1])
    try:
        async with session.get(url) as response:
            if response.status == 200:
                with open(filename, 'wb') as f: 
                    while True:
                        chunk = await response.content.read(1024)
                        if not chunk:
                            break
                        f.write(chunk) 
                print("File downloaded")
            else:
                print(f"Failed to download {url} (Status: {response.status})") 
    except Exception as e:
        print(f"Error downloading {url}: {e}")


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [download_file(session, url) for url in urls]
        await asyncio.gather(*tasks) 

asyncio.run(main())