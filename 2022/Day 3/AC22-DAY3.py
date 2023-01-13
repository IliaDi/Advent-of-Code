# -*- coding: utf-8 -*-
import string
with open('input.txt') as f:
    data = f.readlines()
priorities = dict(zip(string.ascii_letters, range(1,53)))
#part one
result = 0
for rucksack in data:
	compartment1, compartment2 = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
	common_list = set(compartment1).intersection(compartment2)
	for item_type in common_list:
		result += priorities[item_type]
print(result)

#part two
result = 0
def divide_groups(l, n):
	for i in range(0, len(l), n):
		yield l[i:i + n]
n = 3
groups = list(divide_groups(data, n))

for group in groups:
	s1 = set(group[0].strip())
	s2 = set(group[1].strip())
	s3 = set(group[2].strip())
	set1 = set(s1).intersection(s2)
	set2 = set1.intersection(s3)
	common_list = list(set2)
	for item_type in common_list:
		result += priorities[item_type]
print(result)