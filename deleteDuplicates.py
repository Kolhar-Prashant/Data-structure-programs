# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stk,dict,t = [],{},head        
        while t != None:
            if t.val not in dict:
                dict[t.val] = 1
            else:
                dict[t.val] += 1
            t = t.next
        t = None
        cnt = 0
        for val, freq in dict.items():
            if freq == 1:
                temp = ListNode(val)
                if cnt == 0:
                    t = temp
                    head = t
                    cnt = 1
                    continue
                t.next = temp
                t = t.next
        if t != None:
            t = head
            while t != None:
                t = t.next   
            return head
        return t

                    
                