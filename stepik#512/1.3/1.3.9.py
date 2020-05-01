"""~]апи~Hи~Bе ~@еализа~Fи~N ~D~Cнк~Fии closest_mod_5, п~@инима~N~I~C~N в ка~Gе~A~Bве един~A~Bвенного а~@г~Cмен~Bа ~Fелое ~Gи~Aло x и возв~@а~Iа~N~I~C~N ~Aамое мален~Lко
 ~Fелое ~Gи~Aло y, ~Bакое ~G~Bо:

y бол~L~Hе или ~@авно x
y дели~B~A~O на~Fело на 5"""

def closest_mod_5(x):
    y=x
    while y>=x:
        if y % 5 == 0:
            return y
        else:
            y+=1
