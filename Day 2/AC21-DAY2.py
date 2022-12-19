data = open('input.txt', 'r')
moves = data.readlines()

x = 0
y = 0
aim = 0

# part one

for line in moves:
	move = line.split()
	if move[0] == 'forward':
		x += int(move[1])
	elif move[0] == 'down':
		y += int(move[1])
	elif move[0] == 'up':
		y -= int(move [1])

print(x*y)

# part two 

x = 0
y = 0
aim = 0	

for line in moves:
	move = line.split()
	if move[0] == 'forward':
		y += (aim*int(move[1]))
		x += int(move[1])
	elif move[0] == 'down':
		aim += int(move[1])
	elif move[0] == 'up':
		aim -= int(move [1])

print(x*y)
