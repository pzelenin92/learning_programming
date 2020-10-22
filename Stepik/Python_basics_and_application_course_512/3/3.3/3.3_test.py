import re

#pattern=r'\b((\w)(\w))'
pattern=r'(0|11|10(00|1)*01)*'
#substitute=r'\3\2'
string='0011'

match_obj=re.match(pattern, string)
print('match_obj=',match_obj)

search_obj=re.search(pattern,string)
print('search_obj=',search_obj)

findall_obj=re.findall(pattern,string)
print('findall_obj=',findall_obj)

# sub_obj=re.sub(pattern,substitute,string)
# print('sub_obj=',sub_obj)

fullmatch_obj=re.fullmatch(pattern,string)
print('fullmatch_obj=',fullmatch_obj)

