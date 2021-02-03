# input: 38
# Output: 2
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
#              Since 2 has only one digit, return it.
def func(integ):
    sum = 0
    sum2 = 0
    for d in str(integ):
        sum=sum+int(d)
    for d in str(sum):
        sum2=sum2+int(d)
    return sum2
print('38=3+8=11=1+1=',func(38))
