"""Check where thread blocking."""

import sys
import threading
import time


io_lock = threading.Lock()
blocker = threading.Lock()


def block(i):
    t = threading.current_thread()
    with io_lock:
        print('{} with ident {} going to sleep'.format(
            t.name, t.ident))
    if i:
        blocker.acquire()

        time.sleep(0.2)
    with io_lock:
        print(t.name, 'finishing')
    return

threads = [
        threading.Thread(target=block, args=(i,))
        for i in range(3)
]
for t in threads:
    t.setDaemon(True)
    t.start()

threads_by_ident = dict((t.ident, t) for t in threads)

time.sleep(0.01)
with io_lock:
    for ident, frame in sys._current_frames().items():
        t = threads_by_ident.get(ident)
        if not t:
            continue
        print('{} stopped in {} at line {} of {}'.format(
            t.name, frame.f_code.co_name,
            frame.f_lineno, frame.f_code.co_filename))
'''
RESULTS:
<stdin>:30: DeprecationWarning: setDaemon() is deprecated, set the daemon attribute instead
Thread-1 (block) with ident 139713131599424 going to sleep
Thread-1 (block) finishing
Thread-2 (block) with ident 139713131599424 going to sleep
Thread-3 (block) with ident 139713123206720 going to sleep
Thread-3 (block) stopped in block at line 18 of <stdin>
Thread-2 (block) stopped in block at line 20 of <stdin>
'''
