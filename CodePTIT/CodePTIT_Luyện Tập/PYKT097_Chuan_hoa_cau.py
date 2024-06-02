import re
from sys import stdin

for line in stdin.readlines():
    s = re.split('\\s+', line.lower().strip())
    if re.match('^.*[\\.\\?\\!]$', s[-1]):
        if len(s[-1]) > 1:
            print(' '.join(s).capitalize())
        else:
            print(' '.join(s[:-1]).capitalize() + s[-1])
    else:
        print(' '.join(s).capitalize() + '.')
