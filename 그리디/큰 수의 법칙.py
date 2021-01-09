n, m, k = map(int, input().split()) #n= 데이터 갯수, m= 덧셈횟수, k=사용 최대 횟수
data = list(map(int, input().split()))

data.sort() # 입력받은 수 정렬
first = data[n-1] #가장 큰 수
second = data[n-2] #2번째로 큰 수

#result = 0 #결과값을 담을 변수

count = m // (k+1)
rest = m % (k+1)

result = ((first) * k + second) * count
result += first * rest
print(result)

'''
n = data 갯수
m = 총 덧셈 횟수
k = 한 숫자당 사용 최대 횟수
----------------------------
먼저 입력받은 수들을 정렬한다 ->  data.sort()
가장 큰 수(first) = data의 마지막, 2번째로 큰 수(second) = data의 마지막-1 번째 이다.

first * k + second 를 m번 반복해주므로
(first * k + second) * (k + 1)을 해주면 되는데

k+1 이 m과 다를 경우가 있을 수 있기 때문에
이 경우, (first값 * 나머지 갯수) 를 더해주면 된다
'''