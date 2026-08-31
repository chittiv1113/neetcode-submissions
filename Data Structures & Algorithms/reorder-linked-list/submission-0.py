# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head 
        cur = head

        while fast and fast.next:
            if not fast.next.next:
                fast = fast.next 
            else:
                slow = slow.next 
                fast = fast.next.next 
        
        #slow = last of the first sll 
        
        mid = slow.next
        slow.next = None 

        prev = None
        while mid: 
            nxt = mid.next 
            mid.next = prev 
            prev = mid 
            mid = nxt 
        
        while prev:
            nxt1 = cur.next 
            nxt2 = prev.next 
            cur.next = prev 
            prev.next = nxt1
            cur = nxt1
            prev = nxt2 

             

            




