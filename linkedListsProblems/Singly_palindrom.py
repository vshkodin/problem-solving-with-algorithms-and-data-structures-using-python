#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


a=ListNode(1)
b=ListNode(2)
c=ListNode(2)
d=ListNode(1)

a.next=b
b.next=c
c.next=d


class Solution:
    def isPalindrome(self, head):
        lst = []
        curr = head
        while curr:
            lst.append(curr.val)
            curr = curr.next
        print(lst)
        print(lst[::-1])

        output=[]
        counter=0
        for _ in lst:
            counter-=1
            output.append(lst[counter])
        return lst==output

        #return lst == lst[::-1]

s=Solution()
print(s.isPalindrome(a))
