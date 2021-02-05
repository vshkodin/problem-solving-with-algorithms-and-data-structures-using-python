#Input: command = "G()(al)"
#Output: "Goal"
#Explanation: The Goal Parser interprets the command as follows:
#https://leetcode.com/problems/goal-parser-interpretation/
def func(s):
    output=''
    word=''
    for i in s:
        word=word+i
        if word =='G':
            output+='G'
            word=''
        if word == '()':
            output+='o'
            word=''
        if word =='(al)':
            output+='al'
            word=''
    return output
print("Goal",func('G()(al)'))
print("Gooooal",func('G()()()()(al)'))
print("alGalooG",func('(al)G(al)()()G'))
    
