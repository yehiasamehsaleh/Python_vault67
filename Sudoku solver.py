grid = [[0,0,0,2,0,7,1,3,0],
        [5,4,0,0,6,0,0,8,0],
        [0,1,0,9,0,0,0,5,2],
        [9,5,0,0,8,2,0,0,6],
        [0,0,6,0,0,0,7,0,0],
        [3,0,0,5,9,0,0,4,8],
        [8,2,0,0,0,4,0,7,0],
        [0,3,0,0,2,0,0,6,9],
        [0,6,5,1,0,9,0,0,0]]

print (grid[4][2])
print (grid[3][4])
print (grid[5][4])
def print_grid():   
    for line in grid:
        for point in line:
            if point == 0:
                print(".",end=" ")
            else :
                print (point,end=" ")
        print()

print_grid()


def possible(y,x,n):
    global grid
    for i in range(0,9):
        if grid[y][i]==n:
            return False
    for i in range(0,9):
        if grid[i][x]==n:
            return False
    x0=(x//3)*3
    y0=(y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j]==n:
                return False
    return True

print(possible(4,7,2))

def solution():
    global grid
    for y in range (0,9):
        for x in range (0,9):
            if grid[y][x]==0:
                for n in range(1,10):
                    if possible (y,x,n):
                        grid[y][x]=n
                        solution()
                        grid[y][x]=0
                return
    print_grid()
    input("Try again?")
print(solution())


