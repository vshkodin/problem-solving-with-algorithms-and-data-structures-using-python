def func(s):
    output=''
    word=''
    for i in s:
        if i == ' ':
            output+=word+" "
            word=''
        else:
            word=i+word
    return output+word


print("s'teL ekat edoCteeL tsetnoc",func("Let's take LeetCode contest"))
assert "s'teL ekat edoCteeL tsetnoc"==func("Let's take LeetCode contest")
#https://leetcode.com/problems/reverse-words-in-a-string-iii/
