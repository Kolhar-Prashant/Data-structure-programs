def print_ajacency_list():
    col = 1
    for row in mat[1:]:
        indx = 0
        print("Col",col,":",end=" ")
        for val in row:
            if val == 1:
                print(indx,end=" ")
            indx+=1
        col+=1
        print("")

def DFS(row):
    indx = 0
    for val in mat[row]:
        if val == 1:
            if indx not in explored_nodes:
                mem.append(indx)
                Stack.append(indx)
                explored_nodes.append(indx)
                DFS(indx)
        indx+=1
    val = Stack[-1]
    if val not in explored_nodes:
        DFS(val)

mat = [[-1,-1,-1,-1,-1,-1,-1,-1],
       [-1,0,1,1,1,0,0,0],
       [-1,1,0,1,0,0,0,0],
       [-1,1,1,0,1,1,0,0],
       [-1,1,0,1,0,1,0,0],
       [-1,0,0,1,1,0,1,1],
       [-1,0,0,0,0,1,0,0],
       [-1,0,0,0,0,1,0,0]]

Stack = []
explored_nodes = []
start_node = 3
mem = []
mem.append(start_node)
Stack.append(start_node)
explored_nodes.append(start_node)
DFS(start_node)
print("DFS:",mem)
print("--------------")
print("Adjaceny list")
print_ajacency_list()