'''
모든 원소의 번호를 포함할 수 있는 크기의 리스트를 만든 후,
리스트의 인덱스에 직접 접근하여 확인
'''
    

n = int(input()) #가게의 총 부품 수
stockArrs = [0] * 100001 #대충 크게 잡음

for i in input().split():
    stockArrs[int(i)] = 1 #부품번호 인덱스는 1로 바뀜

m = int(input()) #손님이 요청한 부품 수
customerArrs = list(map(int, input().split())) #손님이 요청한 부품 번호

for customer in customerArrs:
    if stockArrs[customer] == 1:
        print('yes', end=" ")
    else:
        print('no', end=" ")
