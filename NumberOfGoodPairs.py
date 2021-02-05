def func(l):
    output=[]
    for i in range(len(l)-1):
        for k in range(1,len(l)):
            if k > i:
                #print(l[i],l[k])
                if l[i]==l[k]:
                    output.append((i,k))
    return len(output)
print('4',func([1,2,3,1,1,3]))
print('6',func([1,1,1,1]))
print('0',func([1,2,3]))
#https://leetcode.com/problems/number-of-good-pairs/
