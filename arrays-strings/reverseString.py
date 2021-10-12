def reverseString(word):
    output=""
    for i in word:
        output=i + output
    return output


print(reverseString("hello"))


def reverseString(array):
    output=[]
    for i in array:
        output.insert(0, i)
    return output


print(reverseString([1,2,3,4]))

def reverseString(array):
    output=[]
    for i in range(1, len(array)+1):
        output.append(array[-i])
    return output


print(reverseString([1,2,3,4]))

def reverseString(array):
    return array[::-1]

print(reverseString([1,2,3,4]))

def reverseString(array):
    output = []
    counter= 0
    for i in array:
        counter-=1
        output.append(array[counter])
    return output

print(reverseString([1,2,3,4]))