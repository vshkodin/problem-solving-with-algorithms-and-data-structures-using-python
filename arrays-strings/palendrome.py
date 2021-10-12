def palindrome(word):
    rev=""
    for i in word:
        rev= i + rev
    if rev== word:
        return True
    else:
        return False
print(palindrome("tattarrattat"))
print(palindrome("race"))
print(palindrome("lol"))