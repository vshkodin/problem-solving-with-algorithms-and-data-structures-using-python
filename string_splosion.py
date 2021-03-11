def func(s):
    output=''
    counter=0
    for i in s:
        counter+=1
        output+=s[:counter]
    return output
print(func("Code"))

def func(s):
    output=''
    counter = 0
    for _ in s:
        counter+=1
        for i in range(counter):
            output+= s[i]
    return output
print(func("Code"))