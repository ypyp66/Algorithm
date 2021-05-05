'''
큰 수 부터 작은 수의 순서로 정렬하기
'''

n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)

print(*array)