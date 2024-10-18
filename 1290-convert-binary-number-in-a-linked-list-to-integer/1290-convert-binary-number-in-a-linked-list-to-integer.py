# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        temp = head
        summ = 0
        length = 0
        while temp:
            length += 1
            temp = temp.next
            
        temp = head
        length -= 1
        while temp:
            summ += temp.val * (2 ** length)
            temp = temp.next
            length -= 1
        return summ