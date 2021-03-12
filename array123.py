def func(array):
    string=''
    ck=''
    for i in array:
        ck+=str(i)
        if ck == '123' or ck == '1' or ck == '12':
            string+=ck
        else:
            ck=''
    if '123' in string:return True
    else: return False

print(func([1,2,4,5,3]))
print(func([1,2,3,5,3]))

