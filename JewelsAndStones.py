def func(j,s):
    output=0
    for i in s:
        if i in j:
            output+=1
    return output
print(3,func('aA','aAAbbbb'))
print(0,func('z','ZZ'))
