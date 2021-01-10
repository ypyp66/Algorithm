'''
n이 입력되면 00시 00분 00초 ~ n시 59분 59초까지의 모든 시각 중에서 
3이 하나라도 포함되는 모든 경우의 수를 구하라.
'''

n = int(input())
cnt = 0

for hour in range(n+1):
    for minutes in range(60):
        for second in range(60):
            if '3' in str(hour)+str(minutes)+str(second):
                cnt += 1
print(cnt)

'''
3중 for문을 이용하면된다.

시간을 입력받는다.
경우의 수를 저장할 cnt를 선언 및 초기화를 한다.

hour > minutes > second 순으로 반복문을 실행해준 후
문자열로 반환시켜 더해준 후 '3'이 포함되면 cnt +=1 을 한다.
ex) 3시20분35초일 경우 032035이므로 cnt += 1이 실행된다.
'''