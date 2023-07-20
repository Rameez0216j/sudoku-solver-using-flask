import numpy as np
def notInRow(arr, row):
	st = set()
	for i in range(0, 9):
		if arr[row][i] in st:
			return False
		if arr[row][i] != 0:
			st.add(arr[row][i])
	return True
	
def notInCol(arr, col):
	st = set()
	for i in range(0, 9):
		if arr[i][col] in st:
			return False
		if arr[i][col] != 0:
			st.add(arr[i][col])
	return True
	
def notInBox(arr, startRow, startCol):
	st = set()
	for row in range(0, 3):
		for col in range(0, 3):
			curr = arr[row + startRow][col + startCol]
			if curr in st:
				return False
			if curr != 0:
				st.add(curr)
	return True


def isValid(arr, row, col):
	return (notInRow(arr, row) and notInCol(arr, col) and
			notInBox(arr, row - row % 3, col - col % 3))

def isValidConfig(arr, n):
	for i in range(0, n):
		for j in range(0, n):
			if not isValid(arr, i, j):
				return False
	return True


# Driver's code
if __name__ == "__main__":
	board = np.array([['0' for i in range(9)] for j in range(9)])
	board[0][1]=1
	if isValidConfig(board, 9):
		print("YES")
	else:
		print("NO")

