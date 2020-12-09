import sys
from launchmodes import QuietPortableLauncher

numclients = 8
def start(cmdline):
    QuietPortableLauncher(cmdline, cmdline)()

# start('echo-server.py')

args = ' '.join(sys.argv[1:])
for i in range(numclients):
    start('echo-client.py %s' % args)
