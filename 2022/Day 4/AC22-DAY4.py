with open('input.txt') as f:
    data = f.readlines()

counter1 = 0
counter2 = 0
for pair in data:
	s1, s2 = pair.split(",")
	s1_start, s1_end = s1.split("-")
	s2_start, s2_end = s2.split("-")
	if ((int(s1_start) <= int(s2_start) and int(s1_end) >= int(s2_end)) or (int(s2_start) <= int(s1_start) and int(s2_end) >= int(s1_end))):
		counter1 += 1

	list1 = range(int(s1_start), int(s1_end)+1)
	list2 = range(int(s2_start), int(s2_end)+1)

	check1 =  any(item in list1 for item in list2)
	check2 =  any(item in list2 for item in list1)
	if (check1 or check2):
		counter2 += 1

print counter1, counter2

