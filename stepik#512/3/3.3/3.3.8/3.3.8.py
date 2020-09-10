import re
import sys

pattern=r'\bcat\b'

for line in sys.stdin:
    line = line.rstrip()
    findall_obj=re.findall(pattern,line)
    if len(findall_obj)>=1:
        print(line)
