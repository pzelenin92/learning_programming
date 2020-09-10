import re

pattern=r'\b[aA]+\b'
substitute=r'argh'
string='this is a text'

match_obj=re.match(pattern, string)
print(match_obj)

search_obj=re.search(pattern,string)
print(search_obj)

findall_obj=re.findall(pattern,string)
print(findall_obj)

sub_obj=re.sub(pattern,substitute,string,1)
print(sub_obj)
