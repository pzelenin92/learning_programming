import re
import sys

pattern=r'(\w)\1+'
substitute=r'\1'

for line in sys.stdin:
    line = line.rstrip()
    sub_obj=re.sub(pattern,substitute,line)
    if sub_obj:
        print(sub_obj)
