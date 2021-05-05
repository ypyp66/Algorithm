array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)): # 0~9, 전체반복
    min_index = i #가장 작은 원소의 인덱스
    for j in range(i+1, len(array)): 
        if array[min_index] > array[j]: #비교값이 더 작은값으면
            min_index = j #min_index를 비교값 인덱스로 설정(더 작은값이 됨)
    #타겟값과 전체 원소의 비교가 끝나면 min_index = array[최솟값]
    array[i], array[min_index] = array[min_index], array[i] #타겟값과 자리바꿈
print(array)