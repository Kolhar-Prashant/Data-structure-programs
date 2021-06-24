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

    def pre_order(self,root):
        if root != None:
            print(root.val)
            if root.left == None and root.right == None:
                mem[0]+=1
            Tree.pre_order(self,root.left)
            Tree.pre_order(self,root.right)

L = [1,2,3,4,-1,6,7]
Queue = []
T = Tree(L[0])
const_root = T
root = T
side = 1
mem = [0]
for val in L[1:]:
    if val != -1:
        T.create(val,side)
    side+=1
    if side > 2:
        side = 1
        root = Queue[0]
        Queue.pop(0)
Queue.clear()
T.pre_order(const_root)
print("Leaf nodes in this Binary tree",mem[0])
