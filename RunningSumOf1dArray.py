def func(array):
    output=[]
    counter=0
    for i in array:
        counter+=1
        sum=0
        for k in range(counter):
            sum = sum +array[k]
        output.append(sum)
    return output
print([1,2,3,4,5],'=',func([1,1,1,1,1]))
print([1,3,6,10],'=',func([1,2,3,4]))
print([3,4,6,16,17],'=',func([3,1,2,10,1]))
#https://leetcode.com/problems/running-sum-of-1d-array/
