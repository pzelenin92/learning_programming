import re

pattern=r'\b((\w)(\w))'
substitute=r'\3\2'
string='this is a text'

match_obj=re.match(pattern, string)
print(match_obj)

search_obj=re.search(pattern,string)
print(search_obj)

findall_obj=re.findall(pattern,string)
print(findall_obj)

sub_obj=re.sub(pattern,substitute,string)
print(sub_obj)
