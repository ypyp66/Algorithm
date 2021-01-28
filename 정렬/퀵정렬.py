array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: #원소가 1개인 경우 종료
        return
    pivot = start #기준은 1번째 원소
    left = start + 1
    right = end

    while left <= right: #left와 right가 같아질때까지 반복
        while left <= end and array[left] <= array[pivot]: #기준원소보다 작거나 같으면 정상이므로
            left += 1 #left는 다음원소의 인덱스로 지정
        
        while right > start and array[right] >= array[pivot]: #기준원소보다 크거나 같으면 정상이므로
            right -= 1 #right도 다음원소의 인덱스로 지정

        if left > right: #엇갈렸다면
            array[right], array[pivot] = array[pivot], array[right] #작은 데이터와 피봇(기준)을 교체
        else: #left가 기준보다 크거나 right가 기준보다 작다면 서로 위치를 바꿈
            array[left], array[right] = array[right], array[left]
    
    #분할 이후 왼쪽부분과 오른쪽부분을 나눠서 각각 정렬함, 기준은 각 부분의 1번째 원소
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)