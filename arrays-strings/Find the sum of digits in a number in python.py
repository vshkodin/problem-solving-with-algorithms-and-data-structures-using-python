def digitsInANumber(num):
	output=0
	for i in str(num):
		output += int(i)
	return output

print(digitsInANumber(12))