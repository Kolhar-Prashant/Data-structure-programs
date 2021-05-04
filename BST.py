
def check_if_deadend_node(indx):
    temp = List[:indx+1]
    if List[indx] == 1:
        if List[indx]+1 in temp:
            return List[indx]
    if List[indx]-1 in temp and List[indx]+1 in temp:
        return List[indx]
    else:
        return -1


class BST:
    def __init__(self,num):
        self.val = num
        self.left = None
        self.right = None

    def insert(self,num,root):
        if num < root.val:
            if root.left == None:
                t = BST(num)
                root.left = t
            else:
                root = root.left
                BST.insert(self,num,root)
        else:
            if root.right == None:
                t = BST(num)
                root.right = t
            else:
                root = root.right
                BST.insert(self,num,root)

List = [8,5,9,2,7,11]
indx = 0
Tree = ""
root = ""
Dead_end = False
while indx != len(List):
    if indx == 0:
        Tree = BST(List[indx])
        root = Tree
    else:
        if check_if_deadend_node(indx) == -1:
            Tree.insert(List[indx],root)
        else:
            print("Node",str(List[indx]),"will be the Dead-end node")
            Dead_end = True
    indx+=1
if Dead_end == False:
    print("This list won't have any Dead-end node")

