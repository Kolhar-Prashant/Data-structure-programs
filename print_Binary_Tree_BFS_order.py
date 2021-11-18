class Tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    
    def insert_node(self,val,side,root):
        temp = Tree(val)
        Stack.append(temp)
        if side == 1:
            root.left = temp
        else:
            root.right = temp
    
    def print_BFS_order(self,root):        
        if root.left != None:
            Queue.append(root.left)
        if root.right != None:
            Queue.append(root.right)
        print(Queue[0].val)
        Queue.pop(0)
        if len(Queue) > 0:
            Tree.print_BFS_order(self,Queue[0])
        
T = Tree(1) # root node
Stack = []
root = T
const_root = root
Stack.append(root)
L = [2,3,-1,5,6,-1]
side = 1
for val in L:
    if val != -1:
        T.insert_node(val,side,root)
    side+=1
    if side > 2:
        side = 1
        Stack.pop(0)
        root = Stack[0]
Queue = []
Queue.append(const_root)
T.print_BFS_order(const_root)        