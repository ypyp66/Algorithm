array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)): #첫번째는 정렬되어있다 판단 (비교할 값이 없으므로), 2번째 원소부터 시작
    for j in range(i,0,-1): #array[i]부터 시작해서 왼쪽으로
        if array[j] < array[j-1]: #왼쪽값이 나보다 작으면
            array[j], array[j-1] = array[j-1], array[j] #서로 바꿈
        else:
            break
print(array)