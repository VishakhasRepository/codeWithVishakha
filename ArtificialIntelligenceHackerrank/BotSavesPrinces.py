def displayPathtoPrincess(n, grid):
    pos_col = {}
    pos_row = {}
    not_find = True

    for i in range(n):
        line = len(grid[i])
        #print(line)   #5
        for j in range(line):
            if grid[i][j] == 'm':
                botr = i
                botc = j
                print(i) #2
                print(j) #2
            elif grid[i][j] == 'p':
                prir = i  #4
                pric = j  #0
                print(i)
                print(j)

    while (not_find):
        if botr < prir:
            botr = botr + 1
            print('DOWN')
        elif botr > prir:
            botr = botr - 1
            print('UP')

        if botc < pric:
            botc = botc + 1
            print('RIGHT')
        elif botc > pric:
            botc = botc - 1
            print('LEFT')

        if botc == pric and botr == botr:
            not_find = False


# print all the moves here
m = int(input())
grid = ['-----', '-----', '--m--', '-----', 'p----']
# for i in range(0, m):
#     grid.append(input().strip())

displayPathtoPrincess(m, grid)
