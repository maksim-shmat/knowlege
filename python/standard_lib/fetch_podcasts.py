"""Show queue in a job.

Read RSS-chanels and make stack with 5 last episodes.
"""

from queue import Queue
import threading
import time
import urllib
from urllib.parse import urlparse

import feedparser  # pip3 install feedparser

# global values
num_fetch_threads = 2
enclosure_queue = Queue()

# hardcode not good
feed_urls = [
        'http://talkpython.fm/episodes/rss',
]

def message(s):
    print('{}: {}'.format(theading.current_thread().name, s))

def download_enclosures(q):
    """Function of work theread.
    Handle elements step by step.
    It's daemon without end cycle
    and end with main thread.
    """
    while True:
        message('looking for the next enclosure')
        url = q.get()
        filename = url.rpartition('/')[-1]
        message('downloading {}'.format(filename))
        response = urllib.request.urlopen(url)
        data = response.read()
        # Save how downloaded into current dir
        message('writing to {}'.format(filename))
        with open(filename, 'wb') as outfile:
            outfile.write(data)
        q.task_done()

for i in range(num_fetch_threads):
    worker = threading.Thread(
            target=download_enclosures,
            args=(enclosure_queue,),
            name='worker-{}'.format(i),
    )
    worker.setDaemon(True)
    worker.start()

# download chanels and put URLs on the stack
for url in feed_urls:
    response = feedparser.parse(url, agent='fetch_podcasts.py')
    for entry in response['entries'][:5]:
        for enclosure in entry.get('enclosures', []):
            parsed_url = urlparse(enclosure['url'])
            message('queuing {}'.format(
                parsed_url.path.rpartition('/')[-1]))
            enclosure_queue.put(enclosure['url'])

# wait what stack is over
message('*** main threa waiting')
enclosure_queue.join()
message('*** done')

'''RESULTS:
worker-0: looking for the next enclosure
worker-1: looking for the next enclosure
MainThread: queuing turbogears-and-the-future-of-python-web-frameworks.mp3
MainThread: queuing continuum-scintific-python-and-the-business-of-open-source.mp3
MainThread: queuing openstack-cloud-computing-built-on-python.mp3
MainThread: queuing pypy.js-pypy-python-in-your-browser.mp3
MainThread: queuing machine-learningi-with-python-and-scikit-learn.mp3
MainThread: *** main thread waiting
worker-0: downloading turbogears-and-the-future-of-python-web-frameworks.mp3
worker-1: downloading continuum-scientific-python-and-the-business-of-open-source.mp3
worker-0: looking for the next enclosure
worker-0: downloading openstack-cloud-computing-built-on-python.mp3
worker-1: looking for the next enclosure
worker-1: downloading pypy.js-pypy-python-in-your-browser.mp3
worker-0: looking for the next enclosure
worker-0: downloading machine-learning-with-python-and-scikit-learn.mp3
worker-1: looking for the next enclosure
worker-0: looking for the next enclosure
MainThread: *** done
'''
