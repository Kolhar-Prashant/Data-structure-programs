def Heapify(L):
    T=['None']
    T.extend(L)
    L = T
    indx = len(L)-1
    while indx > 0:
        mid = indx
        init_indx = indx
        while mid > 1:
            mid = indx//2
            if L[indx] > L[mid]:
                t = L[mid]
                L[mid] = L[indx]
                L[indx] = t
            indx = mid
        indx = init_indx - 1
    L.pop(0)
    return L

class Heap:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self,val,side):
        temp = Heap(val)
        if side == 1:
            root.left = temp
        else:
            root.right = temp
        Queue.append(temp)


L = [5,10,30,20,35,40,15]
L = Heapify(L)
Queue1 = []
Queue = []
H = Heap(L[0])
mem = []
const_root = H
root = H
max_val = []
Queue.append(root)
Side = 1
for ele in L[1:]:
    if ele != -1:
        H.insert(ele,Side)
    Side+=1
    if Side > 2:
        Queue.pop(0)
        root = Queue[0]
        Side = 1
