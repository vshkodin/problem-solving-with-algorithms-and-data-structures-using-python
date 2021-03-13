#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
        self.previous = next


a=ListNode(1)
b=ListNode(2)
c=ListNode(2)
d=ListNode(1)

#head
a.next=b
b.next=c
b.previous=a
c.next=d
c.previous=b
#tail
d.previous=c




class Solution:
    def isPalindrome(self, head, tail):
        #head
        lst_forvard = []
        curr = head
        while curr:
            lst_forvard.append(curr.val)
            curr = curr.next
        print("lst_forvard : ",lst_forvard)

        # tail
        lst_backwards = []
        last=tail
        while last:
            lst_backwards.append(last.val)
            last = last.previous
        print("lst_backwards : ",lst_backwards)
        return lst_forvard == lst_backwards

        #return lst == lst[::-1]

s=Solution()
print(s.isPalindrome(a,d))
