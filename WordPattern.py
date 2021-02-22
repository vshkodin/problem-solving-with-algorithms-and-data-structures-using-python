def func(pattern, s):
    word=""
    sparsed=[]
    for i in s:
        if i==' ':
            sparsed.append(word)
            word = ""
        else:
            word+=i
    sparsed.append(word)
    print(sparsed)

    s = sparsed
    print(s)
    d = {}
    d1 = {}
    counter = 0
    compareOne = []
    compareTwo = []
    for i in pattern:
        if i not in d:
            d[i] = counter
            counter += 1
    counter=0
    for i in pattern:
        compareOne.append(d[i])
    for i in s:
        if i not in d1:
            d1[i] = counter
            counter += 1
    for i in s:
        compareTwo.append(d1[i])
    print(compareOne)
    print(compareTwo)
    if compareOne==compareTwo:
        return True
    else:False


print(func("abba", s = "dog cat cat dog"))
