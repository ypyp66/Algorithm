array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)): # 0~9
    for j in range(i+1, len(array)): 
        if array[i] > array[j]:
            array[j], array[i] = array[i], array[j]
print(array)