class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:        
        cnt = 0
        t = head
        while t!= None:
            t = t.next
            cnt+=1
        pos = cnt - k
        if pos == 0:
            head = head.next
            return head
        cnt = 0
        t = head
        prev = t
        while t != None:
            prev = t
            t = t.next
            cnt += 1
            if cnt == pos:
                prev.next = t.next
                break
        return head