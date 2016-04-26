def multiples(max):
	threeSum = 0
	fiveSum = 0
	finalSum = 0
	threes = max/3
	if max%3 != 0:
		threes+=1
	fives = max/5
	if max%5 != 0:
		fives+=1
	for i in range(threes):
		threeSum+=3*i
	for  i in range(fives):
		fiveSum+=5*i
	finalSum = threeSum + fiveSum
	return finalSum
print(multiples(1000))
