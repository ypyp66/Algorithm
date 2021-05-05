'''
단순히 특정 수가 한 번이라도 등장했는지 검사하면 되기때문에 set을 이용해도 된다.
'''

n = int(input())
stocks = set(map(int, input().split()))

m = int(input())
customers = list(map(int, input().split()))

for i in customers:
    if i in stocks:
        print('yes', end=" ")
    else:
        print('no', end=" ")