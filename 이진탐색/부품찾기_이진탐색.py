def binary_search(array, target, start, end): #target은 찾아야하는 값
    while start <= end:
        mid = (start+end) # 2
        if array[mid] == target: # 타겟값과 같으면 yes
            return 'yes'
        if array[mid] > target: # 타겟값보다 크면 중간값의 왼쪽만 찾으면 됨
            end = mid-1
        else: #타겟값보다 작으면 중간값의 오른쪽만 찾으면 됨
            start = mid+1 
    return 'no'

n = int(input())
stocks = list(map(int, input().split()))
stocks.sort() # 이진탐색을 수행해야하기 때문에 정렬을 미리 해놓는다
m = int(input())
checks = list(map(int, input().split()))


for check in checks:
    result = binary_search(stocks, check, 0, n-1)
    print(result, end=" ")

