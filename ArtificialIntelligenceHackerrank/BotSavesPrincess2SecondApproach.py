

def nextMove(n,r,c,grid):
    NotChanged = True
    for i in range(len(grid)):
        for j in range(n):
            if grid[i][j] == "p":
                pos_row_p = i
                pos_col_p = j

    # Verify the positions of the bot with the princess
    if r < pos_row_p:
        r = r + 1
        return 'DOWN'
    elif r > pos_row_p:
        r = r - 1
        return 'UP'

    if c < pos_col_p:
        c = c + 1
        return 'RIGHT'
    elif c > pos_col_p:
        c = c - 1
        return 'LEFT'



n = 5
r,c = 2,2
grid = ['-----','-----','p-m--','-----','-----']
# for i in range(0, n):
#     grid.append(input())

print(nextMove(n,r,c,grid))

