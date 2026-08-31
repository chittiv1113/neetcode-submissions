# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head    
        length = 0 
        cur = head
        while cur:
            length += 1
            cur = cur.next 
        print(length)

        idx = length-n 

        cur = dummy
        for i in range(idx):
            cur = cur.next 
        
        print(cur.val)
        cur.next = cur.next.next 

        return dummy.next  
        


        



