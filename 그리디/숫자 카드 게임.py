n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    if result <= min(data): result = min(data)
print(result)

'''
각 행 마다 가장 작은 숫자를 뽑고 그 중 가장 큰 숫자를 최종적으로 출력한다.

n = 행의 갯수
m = 열의 갯수

최종 값을 보여줄 result를 선언한다.

data에 각 행에 들어갈 숫자를 입력한다.
만약 각 행마다 가장 작은 숫자가 result보다 크거나 같다면 result에 저장한다.
'''