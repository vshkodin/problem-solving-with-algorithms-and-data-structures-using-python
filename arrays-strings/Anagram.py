#1 dictionaries count letters and compere is the same need 2 dictionaries
#def isAnagram(word1, word2):
#    w1=


# 1st loop  dictionaries count letters +
# 2sd loop minus letters if all 0 to it is true
def isAnagram(word1, word2):
    d={}
    for i in word1:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1

    for i in word2:
        if i not in d:
            d[i]=1
        else:
            d[i]-=1
    for i in d:
        if d[i] != 0:
            return False
    return True


print(isAnagram("earth", "heart"))  # Output: Yes
print(isAnagram("earthh", "heart"))  # Output: Yes