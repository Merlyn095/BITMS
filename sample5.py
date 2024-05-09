'''def fun(n):
    if n==0:
        return 1
    return n*fun(n-1)
n=int(input())
print(fun(n))'''

def fun(n,i):
    if i>10:
        return n
    print(n*i)
    return fun(n,i+1)
fun(5,1)



