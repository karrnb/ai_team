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
path=0
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
            global path
            path = 1
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
        # print(c)
        global final_path
        final_path.append(c)
        c=parent(c)

# Standard update function for animation
# Uses path generated to plot as an animation in the maze
# accepts i as an integer for index on iterations
# returns nothing
def update(i):
    temp_maze = initial_maze
    # set the path to be displayed as a frame of animation
    temp_maze[final_path[i]] = 0.25
    # set matrice with updated values
    matrice.set_array(convertMaze(dim, temp_maze))

# Generates a random maze of dim*dim with blocks of probability p
# accepts dim: dimension of maze and p: probability of blocks in the maze
# returns a 1D array with obstacles to mimic a maze
def MazeGen(dim, p):
    # generates indices for blocks in a maze
    index=random.sample(range(1,(dim**2)-1), int(p*(dim**2)))
    #print(index)
    maze=[]
    for i in range(dim**2):
        if i in index:
            maze.append(1)
        else:
            maze.append(0)
    return maze

# Converting maze array into 2D array for visualization
# accepts dim: dimension of dim*dim array and maze: array of maze
# returns 2D array
def convertMaze(dim, maze):
    return np.array_split(maze, dim)

#initialize variables
dim, p = 100, 0.2

#calling function to create the maze with (dim,p)
flag =  MazeGen(dim, p)
iniFL(dim)
initd(dim)
# creating a copy of the maze to use for visualization
initial_maze = copy.deepcopy([x if x == 0 else 0.4 for x in flag])

##Step 2
# generate_bfs()
ltn = BFS_Agent(flag,dim)
pathGen(ltn)
final_path.append(0)
final_path.reverse()
final_path.append((dim**2) - 1)

##Step Last
if (path==0):
    # generating visualizations starts here
    # initializing graph variables
    fig, ax = plt.subplots()
    # building the initial maze
    matrice = ax.matshow(convertMaze(dim, initial_maze),cmap=cm.nipy_spectral)
    # removing axes and legends from the map
    plt.axis('off')
    ax.legend_ = None

    # running the animation function
    # fig: graph variable, update: update function to change map, 
    # frames: count of animations, interval: frequency of frames
    ani = animation.FuncAnimation(fig, update, frames=(len(final_path)), interval=100)
    
    # display the animation
    plt.show()