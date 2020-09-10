import re

pattern='cat'
string='caat and cat'
match_obj=re.match(pattern, string)
print(match_obj)

search_obj=re.search(pattern,string)

findall_obj=re.findall(pattern,string)
print(findall_obj,search_obj)
