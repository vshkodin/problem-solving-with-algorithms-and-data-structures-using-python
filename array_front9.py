def func(array):
    for i in range(4):
        if array[i]==9:
            return True
    return False
print(func([1,2,3,9,1]))
print(func([1,2,3,6,1]))

def func(array):
    if [x for x in range(4) if array[x] == 9]: return True
    else: return False
print(func([1,2,3,9,1]))
print(func([1,2,3,6,1]))
print(func([1,9,3,6,1]))



def func(array):
    counter=0
    for i in array:
        if counter==4:
            break
        if i == 9:
            return True
    return False

print(func([1,2,3,9,1]))
print(func([1,2,3,6,1]))
print(func([1,9,3,6,1]))
print(func([9]))