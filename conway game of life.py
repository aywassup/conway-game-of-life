import time

#create the grid
def create_grid():
	grid = []
	for i in range(10):
		row = []
		for x in range(10):
			row.append(0)
		grid.append(row)
	return grid
#prints the grid
def print_grid(grid):
	for row in grid:
		for item in row:
			if item == 0:
				print(" -", end="")
			else:
				print(" *", end="")
		print()
#takes in a file name and creates a grid with the virus specified by the file
def virus_grid(file):
	grid = create_grid()
	with open(file, 'r') as f:
		for line in f.readlines():
			x = line.split(',')[0]
			y = line.split(',')[1]
			grid[int(y)][int(x)] = 1
	return grid
#print_grid(virus_grid('square.in'))

# function countNeighbors that takes in a grid, i, j -> return the number of neighbors around the i,j point. 
def countNeighbors(grid, x, y):
	adjacent_spots = 0
	#-1 because this solution counts the square it starts on as adjacent
	for i in range(-1, 2):
		for b in range(-1, 2):
			x_2 = x + b 
			y_2 = y + i
			if (x_2 > 9 or x_2 < 0) or (y_2 > 9 or y_2 < 0):
				continue
			if i == 0 and b == 0:
				continue
			if grid[int(y)+i][int(x)+b] == 1:
				adjacent_spots += 1
	return adjacent_spots
# function isalive takes in a grid,i,j -> returns True if the i,j position in the grid will be alive or dead on the next turn of the simulation

def isAlive(grid, x,y):
	neighbors = countNeighbors(grid, x, y)

	if grid[int(y)][int(x)] == 1:
		if neighbors <= 1:
			return 0
		elif neighbors >= 4:
			return 0
		else:
			return 1
	else:
		if neighbors == 3:
			return 1
		else:
			return 0

#this will take in grid and will return then next grid
def next_frame(grid):
	new_grid = create_grid()
	for x in range(10):
		for y in range(10):
			new_grid[y][x] = isAlive(grid, x, y)
	return new_grid
#print_grid(virus_grid('square.in'))
#print()
#print_grid(next_frame(virus_grid('square.in')))
	
#print(isAlive(1,2))

file = input("What file has the starting positions?")

grid = virus_grid(file)

while True:
	print_grid(next_frame(grid))
	print()
	grid = next_frame(grid)
	time.sleep(1) 
