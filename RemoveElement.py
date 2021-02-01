def func(l,target):
	output=[]
	for i in l:
		if i !=target:
			output.append(i)
	return len(output), output
print(func([3,2,2,3],3))#2, nums = [2,2]
print(func([0,1,2,2,3,0,4,2],2))# 5, nums = [0,1,4,0,3]		
