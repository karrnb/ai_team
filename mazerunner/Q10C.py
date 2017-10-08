#input: the dimension for which you find to find a hard maze Eg:enter 10 to get a 10X10 hard maze
#(final_path_length)-length of the solution path
#(nodes_expanded)-total nodes expanded during runtime
#(max_fringe_size)-maximum size of the fringelist
#(final_path)-solution path traversed without
#top_prob-probability of cell being blocked from 1 to dim^2/4 and from 3dim^2/4+1 to dim^2
#middle_prob-probability of cell being blocked from dim^2/4+1 to 3dim^2/4
#usable_top_prob-top_prob at which a solvable maze could be created
#usable_middle_prob-middle_prob at which a solvable maze could be created
#FringeList-a list of the fringes generated for each explored cell
#difficulty_counter-keeps a track of the number of maze configurations for which no path was found
#scoreList-keeps a track of the heuristic scores of each node in the fringe of the expanded node

import random
import math
import copy
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from matplotlib.pylab import cm

print ("enter the dimensions\n")
dim = int(input ())

index=[]
FringeList=[]
path=[]
td=[]
path_flag=""
scoreList=[]
count=0
nodes_expanded=0
first_quarter = dim**2/4
three_quarter = 3*(dim**2)/4
final_path_length=0
final_path=[]


# ---------Function definition starts------------ #

# initializes the FringeList as an empty list of lists

def iniFL(k):
    if len(FringeList)>0:
        while len(FringeList)>0:
            FringeList.pop(0)
    for j in range(k**2):
        FringeList.append([]) 
        
# ---------Function definition stops------------ #
        


        
# ---------Function definition starts------------ #

# initializes the true distance value list as 0
        
def initd(k):
    for j in range(k**2):
        td.append(0)
        
        
# ---------Function definition stops------------ #



# ---------Function definition starts------------ #

# initializes the scoreList as 0 for each potential cell

def inisl(k):
    for j in range(k**2):
        scoreList.append(0)
        
# ---------Function definition stops------------ #




        
# ---------Function definition starts------------ #

# Generates a random maze for cells starting from index a to index b
# p is the probability of cells between index range (a,b) being blocked 

def MazeGen(a,b, p):
    "Generates a random maze"
    maze=[]
    iniFL(dim)
    initd(dim)
    inisl(dim)
    index=random.sample(range(int(a),int(b-1)), int(p*(b-a)))
    #print(index)
    for i in range(int(a-1),int(b)):
        if i in index:
            maze.append(1)
        else:
            maze.append(0)
    return maze
    
# ---------Function definition stops------------ #



# ---------Function definition starts------------ #

# Calls the function MazeGen() separately for the different partitions
# Combines the partitions to create the final maze and returns as final_flag

def CreateMaze(low_prob,high_prob):
    flag1 = MazeGen(1,first_quarter,low_prob)

    flag2 = MazeGen(first_quarter+1,three_quarter,high_prob)

    flag3 = MazeGen(three_quarter,(dim**2)-1,low_prob)

    final_flag = flag1 + flag2 + flag3
    return final_flag 
    
    
# ---------Function definition stops------------ #



# ---------Function definition starts------------ #


def parent(node):
    "Returns parent node"
    if node==0:
        return 0
    for a in FringeList:
        if node in a:
            return FringeList.index(a)
            
# ---------Function definition stops------------ #
            


# ---------Function definition starts------------ #

def pathGen(c):
    global final_path
    final_path=[]
    pl=0
    while c!=0:
        final_path.append(c)
        pl+=1
        c=parent(c)
    return pl   
    
# ---------Function definition stops------------ #
 


    
# ---------Function definition starts------------ #

def h_ed(n,dim):
    z=0
    x = int(n/dim)+1
    y = (n%dim)+1
    z = ((dim-x)**2) + ((dim-y)**2)
    return math.sqrt(z)
    
    
# ---------Function definition stops------------ #




# ---------Function definition starts------------ #


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
# ---------Function definition stops------------ #




# ---------Function definition starts------------ #

    
def Make_Fringe_AS(MAZE,Qu,d):
    "Generates a fringe for a given cell"
    fringe=[]
    top=len(Qu)-1
    if (Qu[top]+d)<d**2:
        if MAZE[Qu[top]+d]==0 and Qu[top]+d not in Qu:
            fringe.append(Qu[top]+d)
            td[Qu[top]+d]=td[Qu[top]]+1
    if (Qu[top]+1)%d!=0:
        if MAZE[Qu[top]+1]==0 and Qu[top]+1 not in Qu:
            fringe.append(Qu[top]+1)
            td[Qu[top]+1]=td[Qu[top]]+1 
    if (Qu[top]-d)>0:
        if MAZE[Qu[top]-d]==0 and Qu[top]-d not in Qu:
            fringe.append(Qu[top]-d)
            td[Qu[top]-d]=td[Qu[top]]+1
    if Qu[top]%d!=0:
        if MAZE[Qu[top]-1]==0 and Qu[top]-1 not in Qu:
            fringe.append(Qu[top]-1)
            td[Qu[top]-1]=td[Qu[top]]+1 
    #print(fringe)
    FringeList[Qu[top]]=fringe
    return fringe
    
    
# ---------Function definition stops------------ #


    
# ---------Function definition starts------------ #
        
def A_star(MAZE,dim):
    AQ=[0]
    global nodes_expanded
    nodes_expanded=0
    while True:
        if (dim**2)-1 in AQ:
            global path_flag
            path_flag="path found"
            break
        elif len(AQ)==0:
            path_flag="path not found"
            break
        else:
            nodes_expanded=nodes_expanded+1
            temp=AQ[len(AQ)-1]
            AQ = AQ + Make_Fringe_AS(MAZE,AQ,dim)
            MAZE[temp]=1
            AQ.remove(temp)
            AQ=perm(AQ,dim)
            #print(AQ)
    return(temp)
 

# ---------Function definition stops------------ #
 
# Converting maze array into 2D array for visualization
# accepts dim: dimension of dim*dim array and maze: array of maze
# returns 2D array
def convertMaze(dim, maze):
    return np.array_split(maze, dim)

# Standard update function for animation
# Uses path generated to plot as an animation in the maze
# accepts i as an integer for index on iterations
# returns nothing
def update(i):
    temp_maze = copy_maze
    # set the path to be displayed as a frame of animation
    temp_maze[final_path[i]] = 0.25
    # set matrice with updated values
    matrice.set_array(convertMaze(dim, temp_maze))


# ---------MAIN BODY OF THE CODE STARTS------------ #
  
top_prob = 0.4
middle_prob = 0.2

difficulty_counter=0   
while (difficulty_counter!=100) and (middle_prob<=1) and (top_prob<=1):
    final_maze = CreateMaze(top_prob,middle_prob)

    ltn=A_star(final_maze,dim)
   
    if path_flag=="path found":
        top_prob = top_prob + 0.005
        middle_prob = middle_prob + 0.01
        difficulty_counter = 0
        difficulty_counter=difficulty_counter+1
    elif path_flag=="path not found":
        difficulty_counter+=1



final_maze = CreateMaze(top_prob,middle_prob)



usable_top_prob = top_prob - 0.005
usable_middle_prob = middle_prob - 0.01



while (path_flag!="path found"):
    
    final_maze = CreateMaze(usable_top_prob,usable_middle_prob)
    copy_maze = copy.deepcopy([x if x == 0 else 0.4 for x in final_maze])
    ltn=A_star(final_maze,dim)

max_fringe_size = 0
for i in FringeList:
    max_fringe_size = max_fringe_size + len(i)
    
final_path_length = pathGen(ltn)+1
final_path.append(0)
final_path.reverse()
final_path.append((dim**2)-1)

##Step Last
if (final_path):
    # generating visualizations starts here
    # initializing graph variables
    fig, ax = plt.subplots()
    # building the initial maze
    matrice = ax.matshow(convertMaze(dim, copy_maze),cmap=cm.nipy_spectral)
    # removing axes and legends from the map
    plt.axis('off')
    ax.legend_ = None

    # running the animation function
    # fig: graph variable, update: update function to change map, 
    # frames: count of animations, interval: frequency of frames
    ani = animation.FuncAnimation(fig, update, frames=(len(final_path)), interval=100)
    
    # display the animation
    plt.show()
# ---------MAIN BODY OF THE CODE ENDS------------ #
            
    
