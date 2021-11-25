class LL:
    def __init__(self,val):
        self.val = val
        self.next = None

    def selection_sort(self,head):
        t = head
        temp_node = None
        while t.next != None:
            next = t.next
            minn = t.val
            Found = False
            while next != None:
                if next.val < t.val:
                    if next.val < minn:                        
                        minn = next.val
                        temp_node = next
                        Found = True
                next = next.next
            if Found:
                temp = t.val
                t.val = minn
                temp_node.val = temp
            t=t.next                        
        return head
        
    def print_nodes(self,head):
        t = head
        while t != None:
            print(t.val,end=" ")
            t = t.next
L = LL(5)
head = L
t = head
for val in [6,1,7,-1,3]:
    temp = LL(val)
    t.next = temp
    t = t.next
head = L.selection_sort(head)
L.print_nodes(head)