n = int(input())
array = list(map(int, input().split()))

dp = [0] * 100

dp[0] = array[0] #array의 0번째원소
dp[1] = max(array[0], array[1]) #array의 0번째와 1번째 중 큰 값을 선택

for i in range(2, n):
    dp[i] = max(array[i]+dp[i-2], dp[i-1])

print(dp[n-1])

'''
DP배열은 해당 array배열에서 i번째 까지의 최댓값을 저장한 배열이다.

DP[0]은 array[0]이고, DP[1]은 (array[0], array[1])중 큰 값이다.
DP[2]부터는 array[i]번째를 선택한다면 이전원소는 선택하지 못하므로 
i-2번째까지의 합 + array[i]이거나 array[i]를 선택하지 않는다면 DP[i-1]을 최댓값으로 가질것이다.
'''