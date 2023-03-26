

def nextMove(n,r,c,grid):
    NotChanged = True
    for i in range(len(grid)):
        for j in range(n):
            if grid[i][j] == "p":
                pric_pos_r = i
                pric_pos_c = j

    while(NotChanged):
        if [r, c] == [pric_pos_r,pric_pos_c]:
            NotChanged = False

        if r < pric_pos_r:
            r += 1
            print("bot position - ", r,c)
            if pric_pos_r-r == 1 and c==pric_pos_c:
                return "DOWN"


        elif r > pric_pos_r:
            r -= 1
            print("bot position - ", r, c)
            if r - pric_pos_r == 1 and c==pric_pos_c:
                return "UP"


        if c > pric_pos_c:
            c -= 1
            print("bot position - ", r, c)
            if c - pric_pos_c == 1 and r == pric_pos_r:
                return "LEFT"


        elif c < pric_pos_c:
            c += 1
            print("bot position - ", r, c)
            if pric_pos_c -c == 1 and r == pric_pos_r:
               return "RIGHT"



n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))

