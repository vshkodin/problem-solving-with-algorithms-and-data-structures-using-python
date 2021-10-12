class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


a=ListNode(1)
b=ListNode(0)
c=ListNode(1)


a.next=b
b.next=c

class Solution:
    def getDecimalValue(self, head):
        lst=[]
        curr=head
        while curr:
            lst.append(curr.val)
            curr=curr.next
        output=0
        l=len(lst)-1
        for i in range(len(lst)):
            output+=lst[i]*(2**l)
            l-=1
        return output

s=Solution()
print(s.getDecimalValue(a))















#[1,0,1]=5
#5=[1,0,1]
def func(num):

    lst=[]
    while True:
        if num==0:
            break

        else:
            if num % 2 == 0:
                lst.append(0)
                num=num//2
            else:
                if num < 0:
                    num = num + 1
                else:
                    num= num - 1
                lst.append(1)
                num = num // 2
    #p='jopa'
    return lst[::-1]#,p[::-1]

print(func(5))
print(func(7))
print(func(122))
print(func(-122))
#
#
# def bin2num(bin):
#     output = 0
#     leng = len(bin) - 1
#     for i in range(len(bin)):
#         output += bin[i] * (2**leng)
#         leng -= 1
#     return output
#
# print(bin2num([1, 0, 1]))
# print(bin2num([1, 1, 1, 1, 0, 1, 0]))
# print(bin2num([1, 0, 1, 0, 1, 1, 1, 0]))
#
#
# #
# # print(2**2)
# # print(4**2)