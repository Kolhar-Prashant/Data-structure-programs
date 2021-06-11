class Tree:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None

    def create(self,val,side):
        temp = Tree(val)
        Queue.append(temp)
        if side == 1:
            root.left = temp
        else:
            root.right = temp

L = [1,2,3,4,-1,-1,10,-1,-1,5,15,6,-1,-1,-1,-1,12]
Queue = []
T = Tree(L[0])
root = T
side = 1

for val in L[1:]:
    if val != -1:
        T.create(val,side)
    side+=1
    if side > 2:
        side = 1
        root = Queue[0]
        Queue.pop(0)
