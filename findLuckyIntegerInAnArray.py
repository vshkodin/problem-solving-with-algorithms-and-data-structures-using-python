def func(array):
	array=sorted(array)
	unique={}
	lucky=[]
	
	for i in array:
		if i not in unique:
			unique[i]=1
		else:
			unique[i]+=1
	for i in unique:
		if int(i) == unique[i]:
			lucky.append(i)
	
	if lucky !=[]:
		return lucky[-1]
	else:
		return -1

print(func([1,2,2,3,3,3]))
print(func([2,2,2,3,3]))
print(func([5]))
print(func([7,7,7,7,7,7,7]))
print(func([4,3,2,2,4,1,3,4,3]))#expected 3


#class Solution:
#    def findLucky(self, arr: List[int]) -> int:
#        array=sorted(arr)
#        unique={}
#        lucky=[]
#        for i in array:
#                if i not in unique:
#                        unique[i]=1
#                else:
#                        unique[i]+=1
#        for i in unique:
#                if int(i) == unique[i]:
#                        lucky.append(i)
#        if lucky !=[]:
#                return lucky[-1]
#        else:
#                return -1
