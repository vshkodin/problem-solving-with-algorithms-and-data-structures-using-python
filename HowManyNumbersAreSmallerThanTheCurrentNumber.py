def func(array):
    output=[]
    for i in array:
        smallerCount=0
        for k in array:
            if i > k:
                smallerCount+=1
        output.append(smallerCount)
    return output
print([2,1,0,3],func([6,5,4,8]))
print([0,0,0,0],func([7,7,7,7]))
print([4,0,1,1,3],func([8,1,2,2,3]))
