import time
import random
import copy
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from matplotlib.pylab import cm
import math

index=[]
FringeList=[]
path = 0
td=[]
s="lol"
scoreList=[]
count=0
nc=0
def iniFL(k):
    if len(FringeList)>0:
        while len(FringeList)>0:
            FringeList.pop(0)
    for j in range(k**2):
        FringeList.append([0]) 
        
def initd(k):
    for j in range(k**2):
        td.append(0)

def inisl(k):
    for j in range(k**2):
        scoreList.append(0)

def MazeGen(dim, p):
    "Generates a random maze"
    maze=[]
    iniFL(dim)
    initd(dim)
    inisl(dim)
    index=random.sample(range(1,(dim**2)-1), int(p*(dim**2)))
    #print(index)
    for i in range(dim**2):
        if i in index:
            maze.append(1)
        else:
            maze.append(0)
    return maze

# def Make_Fringe_BFS(MAZE,Qu,d):
#     "Generates a fringe for a given cell"
#     fringe=[]
#     if (Qu[0]+d)<d**2:
#         if MAZE[Qu[0]+d]==0 and Qu[0]+d not in Qu:
#             fringe.append(Qu[0]+d)
#     if (Qu[0]+1)%d!=0:
#         if MAZE[Qu[0]+1]==0 and Qu[0]+1 not in Qu:
#             fringe.append(Qu[0]+1)
#     if (Qu[0]-d)>0:
#         if MAZE[Qu[0]-d]==0 and Qu[0]-d not in Qu:
#             fringe.append(Qu[0]-d)
#     if Qu[0]%d!=0:
#         if MAZE[Qu[0]-1]==0 and Qu[0]-1 not in Qu:
#             fringe.append(Qu[0]-1)
#     #print(fringe)
#     FringeList[Qu[0]]=fringe
#     return fringe

# def Make_Fringe_DFS(MAZE,Qu,d):
#     "Generates a fringe for a given cell"
#     fringe=[]
#     TOP=len(Qu)-1
#     if (Qu[TOP]-d)>0:
#         if MAZE[Qu[TOP]-d]==0 and Qu[TOP]-d not in Qu:
#             fringe.append(Qu[TOP]-d)
#     if Qu[TOP]%d!=0:
#         if MAZE[Qu[TOP]-1]==0 and Qu[TOP]-1 not in Qu:
#             fringe.append(Qu[TOP]-1)
#     if (Qu[TOP]+d)<d**2:
#         if MAZE[Qu[TOP]+d]==0 and Qu[TOP]+d not in Qu:
#             fringe.append(Qu[TOP]+d)
#     if (Qu[TOP]+1)%d!=0:
#         if MAZE[Qu[TOP]+1]==0 and Qu[TOP]+1 not in Qu:
#             fringe.append(Qu[TOP]+1)
#     #print(fringe)
#     FringeList[Qu[TOP]]=fringe
#     return fringe

# def BFS_Agent(MAZE,n):
#     BFS_Q=[]
#     BFS_Q.append(0)
#     p=0
#     while True:
#         if (n**2)-1 in BFS_Q: 
#             print("path found")
#             break
#         elif len(BFS_Q)==0:
#             print("path not found")
#             break
#         else:
#             BFS_Q = BFS_Q + Make_Fringe_BFS(MAZE,BFS_Q,n)
#             MAZE[BFS_Q[0]]=1
#             #print(BFS_Q.pop(0))
#             p=BFS_Q.pop(0)
#             print(p)
#     return p

# def DFS_Agent(MAZE,n):
#     DFS_S=[0]
#     while True:
#         if (n**2)-1 in DFS_S:
#             global s
#             s="path found"
#             print("path found")
#             break
#         elif len(DFS_S)==0:
#             s="path not found"
#             print("path not found")
#             break
#         else:
#             top=len(DFS_S)-1
#             temp=DFS_S[top]
#             DFS_S=DFS_S+Make_Fringe_DFS(MAZE,DFS_S,n)
#             MAZE[DFS_S[top]]=1
#             DFS_S.remove(temp)
#             #print(DFS_S)
#             #print(temp)
#     return temp

def parent(node):
    "Returns parent node"
    if node==0:
        return 0
    for a in FringeList:
        if node in a:
            return FringeList.index(a)

def pathGen(c):
    global final_path
    final_path=[]
    pl=0
    while c!=0:
        final_path.append(c)
        pl+=1
        c=parent(c)
    return pl   

def Make_Fringe_AS(MAZE,Qu,d):
    "Generates a fringe for a given cell"
    fringe=[]
    if (Qu[0]-d)>0:
        if MAZE[Qu[0]-d]==0 and Qu[0]-d not in Qu:
            fringe.append(Qu[0]-d)
            td[Qu[0]-d]=td[Qu[0]]+1
    if Qu[0]%d!=0:
        if MAZE[Qu[0]-1]==0 and Qu[0]-1 not in Qu:
            fringe.append(Qu[0]-1)
            td[Qu[0]-1]=td[Qu[0]]+1
    if (Qu[0]+d)<d**2:
        if MAZE[Qu[0]+d]==0 and Qu[0]+d not in Qu:
            fringe.append(Qu[0]+d)
            td[Qu[0]+d]=td[Qu[0]]+1
    if (Qu[0]+1)%d!=0:
        if MAZE[Qu[0]+1]==0 and Qu[0]+1 not in Qu:
            fringe.append(Qu[0]+1)
            td[Qu[0]+1]=td[Qu[0]]+1  
    #print(fringe)
    FringeList[Qu[0]]=fringe
    return fringe   

def h_ed(n,dim):
    z=0
    x = int(n/dim)+1
    y = (n%dim)+1
    z = ((10-x)**2) + ((10-y)**2)
    return math.sqrt(z)

def h_md(n,dim):
    z=0
    x = int(n/dim)+1
    y = (n%dim)+1
    z = (10-x) + (10-y)
    return z

def perm(F,dim): 
    score=0
    a=[]
    b=[]
    c=[]
    for i in F:
        if scoreList[i]!=0:
            a.append([i,score])
        else:
            score=td[i]+h_ed(i,dim)
            scoreList[i]=score
            a.append([i,score])
    for i in a:
        b.append(i[1])
    b.sort()
    for j in b:
        for k in a:
            if j in k and k[0] not in c:
                c.append(k[0])
                break
    return c

def permut(F,dim): 
    score=0
    for i in F:
        if scoreList[i]!=0:
            continue
        else:
            score=td[i]+h_md(i,dim)
            scoreList[i]=score
    return scoreList.index(max(scoreList))
        
def A_star(MAZE,dim):
    AQ=[0]
    global nc
    nc=0
    while True:
        if (dim**2)-1 in AQ:
            global s
            s="path found"
            #print(s)
            break
        elif len(AQ)==0:
            global path
            path = 1
            s="path not found"
            #print(s)
            break
        else:
            nc=nc+1
            AQ = AQ + Make_Fringe_AS(MAZE,AQ,dim)
            MAZE[AQ[0]]=1
            ln=AQ.pop(0)
            AQ=perm(AQ,dim)
    return(ln)

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

# Converting maze array into 2D array for visualization
# accepts dim: dimension of dim*dim array and maze: array of maze
# returns 2D array
def convertMaze(dim, maze):
    return np.array_split(maze, dim)
 
dim, p= 100, 0.2

M=MazeGen(dim, p)
# creating a copy of the maze to use for visualization
initial_maze = copy.deepcopy([x if x == 0 else 0.4 for x in M])
ltn=A_star(M,dim)
pathGen(ltn)
final_path.append(0)
final_path.reverse()
final_path.append((dim**2)-1)

##Step Last
if (path == 0):
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