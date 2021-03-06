n = int(input())

dp = [0]*n

dp[0] = 1
dp[1] = 3

for i in range(2,n):
    dp[i] = (dp[i-1] + dp[i-2] * 2) % 796796

print(dp[n-1])

'''
i-1번째까지 채워져있으면 2x1 1개를 사용하는 1가지 경우,
i-2번째까지 채워져있으면 2x2 1개, 1x2 2개를 사용하는 2가지 경우다.
(1x2 2개의 경우는 i-1번째까지 채워져 있을때 만족하므로 pass)

i-3번째 부터 고려하지 않는 이유는 덮개 최대크기가 2x2이기 때문이다.
따라서 a(i) = a(i-1) + a(i-2) * 2 이다.
'''