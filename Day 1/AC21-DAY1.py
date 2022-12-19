from numpy import loadtxt
data = loadtxt('input.txt')
counter = 0
prev_measurement = data[0]

#part one
for measurement in data:
	if prev_measurement < measurement:	
		counter+=1
	prev_measurement = measurement

#part two
c = 0
prev_measurement = data[0] + data[1] + data[2]
counter = 0

while c+2 < len(data):
	current_measurement = data[c] + data[c+1] + data[c+2];
	if prev_measurement < current_measurement:
		counter+=1
	c+=1
	prev_measurement = current_measurement;


print(counter)