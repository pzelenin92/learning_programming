n, k = map(int, input().split())
def cnk(n,k):
    if k==0:
        c=1
        return c    
    elif k>n:
        c=0
        return c    
    else:
        c=cnk(n-1,k)+cnk(n-1,k-1)
        return c    
n,k=map(int,input().split())
a=cnk(n,k)
print(a)
