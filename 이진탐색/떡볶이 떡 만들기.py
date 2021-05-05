'''
높이 H보다 길면 잘리고 낮으면 잘리지 않는다.
잘리고 남은 떡을 가져간다
떡의 갯수 = n, 떡의 길이 = m
출력은 최대 높이값
'''

n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

start = 0 #탐색 시작값
end = max(array) #탐색 끝값 (초기는 array의 최댓값으로)
result = 0

while(start <= end):
    total = 0 #남은 떡의 총 길이
    mid = (start + end) // 2 #자를 길이

    for i in array: #array값을 하나씩 반복
        if i > mid: #i가 자를 길이보다 길면
            total += i - mid #자르고 남은 길이를 더함
    
    if total >= m: #가져가야할 길이보다 길거나 같으면
        result = mid
        start = mid + 1 #중간값+1 을 시작값으로 바꾸면 중간값은 커지므로 더 짧게 남길 수 있다.
    else: #작으면
        end = mid - 1 #중간값-11 을 끝값으로 바꾸면 중간값은 작아지므로 더 길게 남길 수 있다.
print(result)