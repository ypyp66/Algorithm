N = int(input())

changes = [500, 100, 50, 10]
cnt = 0

for change in changes:
    cnt += N // change
    N %= change
print(cnt)
