class LL:
    def __init__(self,val):
        self.val = val
        self.next = None

    def insert(self,val,head):
        temp = LL(val)
        t = head
        while t.next != None:
            t = t.next
        t.next = temp
    
    def reverse(self,head):
        tail = head
        while tail.next != None: # taking tail to end of LL           
            stack.append(tail)
            tail = tail.next
        t = tail
        while t != head:  
            t.next = stack[-1] #pointing node to it's prev node using top element in stack
            t = t.next
            stack.pop(-1)  # poping top element 
        t.next = None  # making head node point to None
        head = tail
        return head  # returning new head node
    
    def print(self,head,msg):
        print(msg,end=": ")
        t = head
        while t != None:
            print(t.val,end=" ")
            t = t.next
        print("\n")
Arr = list(range(10,15))
L = LL(Arr[0])
head = L
tail = L
stack = []
for val in Arr[1:]:
    L.insert(val,head)
L.print(head,msg="Before reversing")
head = L.reverse(head)
L.print(head,msg="After  reversing")
head = L.reverse(head)
L.print(head,msg="After  reversing")