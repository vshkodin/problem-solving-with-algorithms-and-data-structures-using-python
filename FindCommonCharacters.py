def func(A):
    output=[]
    start=A[0]
    for i in range(len(start)):
        checker=True
        for k in range(len(A)):
            if start[i] not in A[k]:
                checker=False
            else:
                r=A[k]
                #print("before replace r=",r)
                r=r.replace(start[i],'',1)
                #print("after replace r= ",r)
                A[k]=r
                #print("after replace A[k]= ",A[k])
        if checker==True:
            output.append(start[i])
    return output
print(["e","l","l"],func(["bella","label","roller"]))
print(["c","o"],func(["cool","lock","cook"]))
#https://leetcode.com/problems/find-common-characters/
