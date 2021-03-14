def func(s):
    if len(s)==0:
        return s
    else:
        return func(s[1:])+s[0]

print(func("Home"))

