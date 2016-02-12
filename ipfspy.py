import subprocess
import sys
import json

for line in sys.stdin:
    line = json.loads(line)

    if 'event' not in line:
        continue

    if line['event'] != 'handleAddProvider':
        continue

    print('.', end='')
    sys.stdout.flush()

    try:
        f = subprocess.check_output('ipfs cat %s | file -' % line['key'], shell=True, timeout=10)
    except subprocess.TimeoutExpired:
        continue
    f = ':'.join(f.decode('ascii').split(':')[1:]).strip()

    if f not in ('data', 'empty', 'no read permission'):
        print('\n%s: %s' % (line['key'], f))
