import re
import sys

pattern=r'\b[aA]+\b'
substitute=r'argh'

for line in sys.stdin:
    line = line.rstrip()
    sub_obj=re.sub(pattern,substitute,line,1)
    if sub_obj:
        print(sub_obj)
