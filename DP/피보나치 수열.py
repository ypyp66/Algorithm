#재귀(탑다운)
d = [0] * 100
def fibo(x):
    # print(f'f({str(x)} + )', end=" ")
    if x == 1 or x == 2:
        return 1
    if d[x] !=0:
        return d[x]
    
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(6))

d = [0] * 100
def pibo(x):
    print(f'f({x})', end=" ")

    if x==1 or x==2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = pibo(x-1) + pibo(x-2)
    return d[x]
print(d)
pibo(6)

#반복문(바텀업)
d = [0] * 100
d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-2] + d[i-1]
print(d)