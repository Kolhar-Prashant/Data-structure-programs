def explore(col):
    indx = 1
    while indx != len(mat[col]):
        if mat[col][indx] == 1:
            if indx not in BFS:
                BFS.append(indx)
            if indx not in mem:
                Queue.append(indx)
                mem.append(indx)
        indx+=1
    if len(Queue) > 0:
        val = Queue[0]
        Queue.pop(0)
        explore(val)

mat = [[-1,-1,-1,-1,-1,-1,-1],
       [-1,0,1,1,0,0,0],
       [-1,1,0,0,1,0,0],
       [-1,1,0,0,1,0,0],
       [-1,0,1,1,0,1,1],
       [-1,0,0,0,1,0,0],
       [-1,0,0,0,1,0,0]]
Queue = []
BFS = []
start_node = 3
mem = [start_node]
BFS.append(start_node)
explore(start_node)
nodes = list(range(1,len(mat)))
unexplored_nodes = []

for num in nodes:
    if num not in mem:
        unexplored_nodes.append(num)
for node in unexplored_nodes:
    mem.append(node)
    explore(node)
print(BFS)