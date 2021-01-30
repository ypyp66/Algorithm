array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <=1:
        return array

    pivot = array[0] #기준은 첫번째 원소
    tail = array[1:] #기준을 제외한 원소들

    left_side = [x for x in tail if x <= pivot] #왼쪽부분
    right_side = [x for x in tail if x > pivot] #오른쪽부분

    # 왼쪽 부분 + 기준 + 오른쪽 부분
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))