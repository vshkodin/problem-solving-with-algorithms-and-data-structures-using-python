def func(array):
    swap=True
    l=len(array)
    counter=0
    while True:
        if counter==l-1:
            if swap==False:
                break
            else:
                counter=0
                swap=False
                continue
        else:
            a=array[counter]
            b=array[counter+1]
            if a > b:
                swap=True
                array[counter]=b
                array[counter+1]=a
        counter+=1
    print(array)
    listOfMaxs=[]
    maxnum=0
    for i in array:
        if i>maxnum:
            maxnum=i
            listOfMaxs.append(maxnum)
    return listOfMaxs[-2]
print('6 = ',func([1,2,3,4,5,6,7]))# 6
print('8 = ',func([9,7,2,3,4,8,5,6,7]))# 8
print('7 = ',func([8,7,6,2,3,4,5,6,7]))# 7
print('7 = ',func([0,8,7,6,2,3,4,5,6,7]))# 7
#print('-2 = ',func([0,-8,-7,-6,-2,-3,-4,-5,-6,-7]))# -2 cannot solve nevgative
