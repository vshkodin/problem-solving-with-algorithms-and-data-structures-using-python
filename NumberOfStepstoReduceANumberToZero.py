def func(num):
    output=0
    while True:
        if num==0:
            break
        else:
            if num % 2 ==0:
                output+=1
                num=num//2
            else:
                output+=1
                num=num-1
    return output
print('6 = ',func(14))
print('4 = ',func(8))
print('12 = ',func(123))
