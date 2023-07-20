import numpy as np
# validator function
def issafe(a,row,col,num):
    for i in range(9):
        if (a[row][i] == num):
            return 0
    for i in range(9):
        if (a[i][col]==num):
            return 0
    start_row = row - (row % 3)
    start_column = col - (col % 3)
    for i in range(3):
        for j in range(3):
            if (a[i + start_row][j + start_column] == num):
                return 0;
    return 1

# solution function
def solve_sudoku(a,row,col):
    if (row == 8 and col == 9):
        return 1
    if (col == 9):
        row+=1
        col = 0
    if (a[row][col] > 0):
        return solve_sudoku(a, row, col + 1)
    for i in range(1,10):
        if (issafe(a, row, col, i) == 1):
            a[row][col] = i
            if (solve_sudoku(a, row, col + 1)==1):
                return 1
        a[row][col] = 0
    return 0


# display function

def display(a):
    for i in range(9):
        for j in range(9):
            print(f'{a[i][j]:4}',end="")
        print("")
    print("")\



# Driver function

if(__name__=="__main__"):
    # puzzle= np.array([[3, 0, 6, 5, 0, 8, 4, 0, 0],
    #                   [5, 2, 0, 0, 0, 0, 0, 0, 0],
    #                   [0, 8, 7, 0, 0, 0, 0, 3, 1],
    #                   [0, 0, 3, 0, 1, 0, 0, 8, 0],
    #                   [9, 0, 0, 8, 6, 3, 0, 0, 5],
    #                   [0, 5, 0, 0, 9, 0, 6, 0, 0],
    #                   [1, 3, 0, 0, 0, 0, 2, 5, 0],
    #                   [0, 0, 0, 0, 0, 0, 0, 7, 4],
    #                   [0, 0, 5, 2, 0, 6, 3, 0, 0]])
    puzzle= np.array([[1, 1, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0]])
    if (solve_sudoku(puzzle, 0, 0)==1):
        display(puzzle)
    else:
       printf("\n No Solution for your puzzle,maybe it's wrong.")