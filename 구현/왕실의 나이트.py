'''
나이트는 8x8 좌표 평면에서 L자 형태로만 이동할 수 있다.
  a b c d
1
2
3
4
의 형태다

1. 수평으로 2칸 이동, 수직으로 1칸 이동
2. 수직으로 2칸 이동, 수평으로 1칸 이동

가능한 경우의 수 출력
'''

current = input()
row = int(current[1]) #행이 숫자이므로 int형태로 바꿔준다
col = int(ord(current[0])) - int(ord('a')) + 1 #만약 a에서 a값인 97을 빼주면 0이므로 +1을 해주어야 1~8사이 숫자가 된다.

steps = [(-1,2), (1,2), (-1,-2), (1,-2), (2,1), (2,-1), (-2,-1), (-2,1)] # 가능한 경우의 수

cnt = 0 #경우의 수를 받을 변수

for step in steps:
    new_row = row + step[1]
    new_col = col + step[0]

    if new_row <= 8 and new_row >=1 and new_col >=1 and new_col <=8:
        cnt += 1
print(cnt) 