def factorial(n):
    result = 1
    for i in range(1,n+1): #1~n
        result *= i
    return result

def factorial_recursive_(i):
    if i == 100:
        print(f'{i}번째 재귀함수 종료')
        return
    print(f'{i}번째 재귀함수 -> {i+1}번째 재귀함수')
    factorial_recursive(i+1)
    print(f'{i}번째 재귀함수 종료')

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n* factorial_recursive(n-1)

print('반복문: ', factorial(10))
print('재귀문: ', factorial_recursive(10))