
d = [0] * 100
def fibo(x):
    
    if x == 1 or x == 2:
        return 1
    if d[x] !=0:
        return d[x]
    
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(4))

d = [0] * 100
def pibo(x):
    print(f'f({x})', end="")

    if x==1 or x==2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = pibo(x-1) + pibo(x-2)
    return d[x]
pibo(6)