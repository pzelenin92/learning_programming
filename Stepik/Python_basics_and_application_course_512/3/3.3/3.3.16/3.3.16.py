import re
import sys

pattern=r'(0|11|10(00|1)*01)*'

for line in sys.stdin:
    line = line.strip()
    if re.search(r'\A[01]+\Z',line):
         if re.fullmatch(pattern,line):
             print(line)
