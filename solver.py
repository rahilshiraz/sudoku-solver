def isValid(bo,num,pos):
    row, col = pos

    #Check row
    for i in range(len(bo)):
        if bo[row][i] == num and col != i:
            return False
        
    #Check column
    for i in range(len(bo)):
        if bo[i][col] == num and row != i:
            return False
    
    #Check box
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and pos != (i,j):
                return False

    return True

def printBoard(bo):
    for i in range(len(bo)):
        if i%3 == 0 and i != 0:
            print('- '*10)

        for j in range(len(bo[i])):
            if j%3 == 0 and j != 0:
                print('|', end='')

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + ' ', end='')

def findEmpty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if bo[i][j] == 0:
                return (i,j)
    return None

def solve(bo):

    empty = findEmpty(bo)
    if not empty:
        return True
    else:
        row, col = empty

    for i in range(1,10):
        if isValid(bo,i,empty):
            bo[row][col] = i

            if solve(bo):
                return True
            
            bo[row][col] = 0
    return False
