with open('input.txt') as f:
    data = f.readlines()
def winner (move_1, move_2):
	if move_1 == 'A':
		if move_2 == 'Y':
			return 2
		elif move_2 == 'X':
			return 0
		else:
			return 1;
	elif move_1 == 'B':
		if move_2 == 'Z':
			return 2
		elif move_2 == 'Y':
			return 0
		else:
			return 1
	elif move_1 == 'C':
		if move_2 == 'X':
			return 2
		elif move_2 == 'Z':
			return 0
		else:
			return 1

total_score = 0
for round in data:
	score = 0
	if round[2] == 'X':
		score += 1
	elif round[2] == 'Y':
		score += 2
	else:
		score += 3
	if (winner(round[0], round[2]) == 0):
		score += 3
	elif (winner(round[0], round[2]) == 2):
		score += 6
	total_score += score

print(total_score)

#part two
def move (move_1, result):
	if move_1 == 'A':
		if result == 'X':
			return 'Z'
		elif result == 'Y':
			return 'X'
		else:
			return 'Y';
	elif move_1 == 'B':
		if result == 'X':
			return 'X'
		elif result == 'Y':
			return 'Y'
		else:
			return 'Z';
	elif move_1 == 'C':
		if result == 'X':
			return 'Y'
		elif result == 'Y':
			return 'Z'
		else:
			return 'X';

total_score = 0
for round in data:
	score = 0
	my_move = move(round[0], round[2])
	if my_move == 'X':
		score += 1
	elif my_move == 'Y':
		score += 2
	else:
		score += 3
	if (winner(round[0], my_move) == 0):
		score += 3
	elif (winner(round[0], my_move) == 2):
		score += 6
	total_score += score

print(total_score)
