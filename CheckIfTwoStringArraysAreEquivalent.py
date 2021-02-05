def func(l1,l2):
    s1c=''
    s2c=''
    for i in l1:
        s1c+=i
    for i in l2:
        s2c+=i
    if s1c==s2c:
        return True
    else:
        return False
print("False",func(l1 = ["a", "cb"], l2 = ["ab", "c"]))
print("True",func(l1 = ["ab", "c"], l2 = ["a", "bc"]))
print("True",func(l1 = ["abc", "d", "defg"], l2 = ["abcddefg"]))
#https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
