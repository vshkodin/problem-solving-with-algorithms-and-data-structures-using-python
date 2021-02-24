class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        d={}
        max=0
        maxKey=0
        for i in A:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d:
            if d[i]>max:
                max=d[i]
                maxKey=i
        return maxKey
#https://leetcode.com/problems/n-repeated-element-in-size-2n-array/submissions/