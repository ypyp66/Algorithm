def binary_search(array, target, start, end):
    while start <= end: #시작인덱스가 끝인덱스보다 작거나 같으면 반복
        mid = (start + end) // 2 #중간인덱스 설정
        if array[mid] == target: #중간인덱스 값이 타켓값이면
            return mid #인덱스를 return
        elif array[mid] > target: #중간인덱스 값이 타겟값보다 크면 (오른쪽에 있으면)
            end = mid - 1 #끝 인덱스를 줄여줌
        else: #중간인덱스 값이 타겟값보다 작으면
            start = mid + 1 #시작인덱스를 늘려줌
    return None #반복문이 끝나면 해당되는 값이 없으므로 return

n, target = map(int, input().split())
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print('값이 없음')
else:
    print(f'{result+1}번째에 있음')

'''
탐색 범위가 2000만을 넘어가면 이진탐색으로 문제에 접근해보자
'''