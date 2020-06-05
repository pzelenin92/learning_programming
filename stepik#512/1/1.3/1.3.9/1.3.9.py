def closest_mod_5(x):
    y=x
    while y>=x:
        if y % 5 == 0:
            return y
        else:
            y+=1
