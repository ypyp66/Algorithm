array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count = [0] * (max(array)+1) #갯수를 체크할 배열 선언

for i in range(len(array)): #count배열에 array[i]의 값에 해당하는 인덱스의 값을 +1
    count[array[i]] += 1

for i in range(len(count)): #count인덱스의 값만큼 인덱스번호 출력
    for j in range(count[i]):
        print(i, end=' ')

'''
시간복잡도는 O(n+k), (n= 데이터 갯수, k= 최댓값)
데이터의 크기가 한정되어있고 데이터의 크기가 많이 중복되어 있을수록 유리함
'''