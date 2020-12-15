x, y = 1, 1
n = int(input())
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0] # D U L R
move_type = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_type)):
        if plan == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx>n or nx<1 or ny>n or ny<1:
        continue
    x = nx
    y = ny

print(x, y)