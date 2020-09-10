import re

pattern=r'\bcat\b'
string='catapult and cat'

match_obj=re.match(pattern, string)
print(match_obj)

search_obj=re.search(pattern,string)
print(search_obj)

findall_obj=re.findall(pattern,string)
print(findall_obj)
