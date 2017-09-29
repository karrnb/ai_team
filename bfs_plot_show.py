import random
import copy
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from matplotlib.pylab import cm
import math

"BFS part"
maze=[]
index=[]
FringeList=[]
path=[]
td=[]
final_path = []

def iniFL(k):
    for j in range(k**2):
        FringeList.append([0]) 
        
def initd(k):
    for j in range(k**2):
        td.append(0)

def Make_Fringe_BFS(MAZE,Qu,d):
    "Generates a fringe for a given cell"
    fringe=[]
    if (Qu[0]-d)>0:
        if MAZE[Qu[0]-d]==0 and Qu[0]-d not in Qu:
            fringe.append(Qu[0]-d)
    if (Qu[0]+d)<d**2:
        if MAZE[Qu[0]+d]==0 and Qu[0]+d not in Qu:
            fringe.append(Qu[0]+d)
    if Qu[0]%d!=0:
        if MAZE[Qu[0]-1]==0 and Qu[0]-1 not in Qu:
            fringe.append(Qu[0]-1)
    if Qu[0]%d!=-1:
        if MAZE[Qu[0]+1]==0 and Qu[0]+1 not in Qu:
            fringe.append(Qu[0]+1)
    #print(fringe)
    FringeList[Qu[0]]=fringe
    return fringe

def BFS_Agent(MAZE,n):
    BFS_Q=[]
    BFS_Q.append(0)
    p=0
    while True:
        if (n**2)-1 in BFS_Q: 
            print("path found")
            break
        elif len(BFS_Q)==0:
            print("path not found")
            break
        else:
            BFS_Q = BFS_Q + Make_Fringe_BFS(MAZE,BFS_Q,n)
            MAZE[BFS_Q[0]]=1
            #print(BFS_Q.pop(0))
            p=BFS_Q.pop(0)
            #print(p)
    return p

def parent(node):
    "Returns parent node"
    for a in FringeList:
        if node in a:
            return FringeList.index(a)

def pathGen(c):
    "displays a path"
    if c==0:
        return
    while(c!=0):
        print(c)
        global final_path
        final_path.append(c)
        c=parent(c)

def generate_bfs():
    ltn = BFS_Agent(M,dim)
    pathGen(ltn)
    final_path.reverse()

def update(i):
    temp_maze = initial_maze
    temp_maze[final_path[i]] = 0.6
    matrice.set_array(convertMaze(dim, temp_maze))

def MazeGen(dim, p):
    "Generates a random maze"
    index=random.sample(range(1,(dim**2)-1), int(p*(dim**2)))
    maze=[]
    for i in range(dim**2):
        if i in index:
            maze.append(1)
        else:
            maze.append(0)
    return maze

def convertMaze(dim, maze):
    return np.array_split(maze, dim)

#initialize variables
dim, p = 10, 0.1

#calling function to create the maze with (dim,p)
initial_maze =  MazeGen(dim,p)
M = copy.deepcopy(initial_maze)

##Step 2
# generate_bfs()
ltn = BFS_Agent(M,dim)
pathGen(ltn)
final_path.reverse()
##Step Last
# generating visualizations starts here
# initializing graph variables
fig, ax = plt.subplots()

matrice = ax.matshow(convertMaze(dim, initial_maze))
plt.axis('off')

ani = animation.FuncAnimation(fig, update, frames=(len(final_path)), interval=100)
ax.legend_ = None
plt.show()
