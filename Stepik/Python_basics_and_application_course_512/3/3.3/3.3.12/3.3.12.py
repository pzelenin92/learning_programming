import re
import sys

pattern=r'human'
substitute=r'computer'

for line in sys.stdin:
    line = line.rstrip()
    sub_obj=re.sub(pattern,substitute,line)
    if sub_obj:
        print(sub_obj)
