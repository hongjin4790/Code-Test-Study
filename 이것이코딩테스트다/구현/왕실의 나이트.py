# 왕실의 나이트
pos = input()
row = int(pos[1])
column = int(ord(pos[0])) - int(ord('a'))+1
move_case = [(-2,-1),(-2,1),(1,-2),(1,2),(2,1),(2,-1),(-1,2),(-1,-2)]

result = 0
for i in move_case:
    next_row = row + i[0]
    next_column = column + i[1]

    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        result += 1

print(result)
