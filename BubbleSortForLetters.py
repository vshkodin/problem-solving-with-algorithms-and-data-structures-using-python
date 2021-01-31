def non_rep(s):
    swap = True
    s = list(s)
    alph = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    while swap:
        swap = False
        for i in range(len(s) - 1):
            if alph[s[i]] > alph[s[i + 1]]:
                s[i], s[i + 1] = s[i + 1], s[i]
                swap = True
    return "".join(s)


print(non_rep(s="bbaddccaa"))
