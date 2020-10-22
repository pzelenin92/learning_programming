import re
import sys

pattern=r'.*\\.*'

for line in sys.stdin:
    line = line.rstrip()
    match_obj=re.match(pattern,line)
    if match_obj:
        print(line)
