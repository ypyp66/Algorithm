def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end) // 2 #중간값

    if array[mid] == target: #중간값이랑 타겟이랑 같으면
        return mid
    elif array[mid] > target: #중간값이 타켓값보다 크면(오른쪽에 있으면)
        return binary_search(array, target, start, mid-1) #end를 중간값의 바로 왼쪽 값으로 설정 후 함수호출
    else: #타겟값이 더 크면
        return binary_search(array, target, mid+1, end)

n, target = map(int, input().split()) #n=원소갯수
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1) #start, end는 인덱스
if result == None:
    print("원소가 없음")
else:
    print(result+1)