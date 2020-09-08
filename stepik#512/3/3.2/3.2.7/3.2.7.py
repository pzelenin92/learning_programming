# s = "aaaaa"
# t = "a"
s, t = (str(input()) for i in range(2))
def findovrlp (s,t):
    xs=set()
    for i in range(len(s)):
        try:
            xs.add(s.index(t,i))
        except ValueError:
            break
    return len(xs)

print(findovrlp(s,t))
