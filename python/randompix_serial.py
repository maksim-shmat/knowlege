"""Download random picture."""


import os
from secrets import token_hex
from concurrent.futures import ProcessPoolExecutor, as_completed  # for multiprocesses
import requests


PICS_FOLDER = 'pics'
URL = 'https://www.instagram.com/explore/'

def download(url):
    resp = requests.get(URL)
    return save_image(resp.content)

def save_image(content):
    filename = '{}.jpg'.format(token_hex(4))
    path = os.path.join(PICS_FOLDER, filename)
    with open(path, 'wb') as stream:
        stream.write(content)
    return filename

#def batch_download(url, n):
#    return [download(url) for _ in range(n)]

def batch_download(url, n, workers=4):
    """For multiprocesses."""
    with ProcessPoolExecutor(max_workers=workers) as executor:
        futures = (executor.submit(download, url) for _ in range(n))
        return [future.result() for future in as_completed(futures)]

if __name__ == '__main__':
    saved = batch_download(URL, 10)  # ten images
    print(saved)


