f = open("input.txt", "r")
lines = [line.rstrip('\n').replace('L', '-').replace('R', '+') for line in f]

dial = 50
count = 0

for i in lines:
	dial = ((dial + int(i)) % 100)
	if dial == 0:
		count += 1
	
print(count)
