def removeDublicate(l):
	output = []
	for i in l:
		if i not in output:
			output.append(i)
	return output

print(removeDublicate([1,2,3,4,1]))


def removeDublicate(l):
	output = ''
	for i in l:
		if i not in output:
			output+=i
	return output

print(removeDublicate('112334'))
