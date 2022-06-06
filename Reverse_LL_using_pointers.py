class LL:
    def __init__(self, val):
        self.next = None
        self.val = val

    def insert_node(self, val, head):
        t = head
        while t.next != None:
            t = t.next
        t.next = LL(val)

    def reverse_LL(self, head):
        p, c, n = head, head, head
        for _ in range(2):
            n = n.next
        for _ in range(1):
            c = c.next
        p.next = None
        while n != None:
            c.next = p
            p = c
            c = n
            n = n.next
        c.next = p
        return c

    def print_nodes(self, head):
        t = head
        while t != None:
            print(t.val, end=" ")
            t = t.next


L = ['0', 'R', 'E', 'Z']
L1 = LL(L[0])
head = L1
for v in L[1:]:
    L1.insert_node(v, head)
head = L1.reverse_LL(head)
L1.print_nodes(head)