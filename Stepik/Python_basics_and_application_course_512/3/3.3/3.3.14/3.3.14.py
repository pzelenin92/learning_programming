import re
import sys

pattern=r'\b((\w)(\w))'
substitute=r'\3\2'

for line in sys.stdin:
    line = line.rstrip()
    sub_obj=re.sub(pattern,substitute,line)
    if sub_obj:
        print(sub_obj)
