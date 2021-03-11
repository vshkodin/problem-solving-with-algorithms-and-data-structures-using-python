def fun(s):
    output=""
    counter=1
    for i in s:
        if counter%2!=0:
            output+=i
        counter+=1
    return output
print(fun("HELLO"))

def fun(s):
    output=""
    for i in range(len(s)):
        if (i+1)%2!=0:
            output+=s[i]
    return output
print(fun("HELLO"))

def fun(s): return "".join([s[x] for x in range(len(s)) if (x+1)%2!=0])
print(fun("HELLO"))