with open('input.txt') as f:
    data = f.readlines()

#part one
max_calories = int(data[0])
calorie_sum = 0

for calories in data:
	if calories == "\n":
		if calorie_sum > max_calories:
			max_calories = calorie_sum
		calorie_sum = 0
	else:
		calorie_sum += int(calories)
print(max_calories)

#part two
i = 0
elf_calories = []
elf_calories.append(0)
for calories in data:
	if calories == "\n":
		i+=1
		elf_calories.append(0)
	else:
		elf_calories[i] += int(calories)
elf_calories.sort(reverse = True)
print(elf_calories[0]+elf_calories[1]+elf_calories[2])