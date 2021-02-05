def func(s):
    output=0
    balanced=[]
    word=''
    R=0
    L=0
    for i in s:
        word+=i
        if i == "R":
            R+=1
        else:
            L+=1
        if R == L:
           output+=1
           balanced.append(word)
           word=''
           R=0
           L=0
    return output, balanced
print(4,func("RLRRLLRLRL"))
print(3,func("RLLLLRRRLR"))
print(1,func("LLLLRRRR"))
print(2,func("RLRRRLLRLL"))
#https://leetcode.com/problems/split-a-string-in-balanced-strings/
