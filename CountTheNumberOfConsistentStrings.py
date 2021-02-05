def func(a,words):
    output=0
    for i in words:
        checker=True
        for k in i:
            if k not in a:
                checker=False
        if checker==True:
            output+=1
    return output
print(2,func(a='ab',words=["ad","bd","aaab","baa","badab"]))
print(7,func(a='abc',words=["a","b","c","ab","ac","bc","abc"]))
print(4,func(a='cad',words=["cc","acd","b","ba","bac","bad","ac","d"]))
#https://leetcode.com/problems/count-the-number-of-consistent-strings/
