import random
import copy
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from matplotlib.pylab import cm


"DFS part"
#finds possible tracks
def track():
    #initializing the stack with the starting cell that is 0
    A.append(0)
    
    var=A.pop(0)
    #till last cell is reached if it is possible to be reached
    while (var!=((dim**2)-1)):
    	#output the current cell 
        # print (var)
        #since we have visited the current cell, set the flag value 1 so that it is not included in the fringe of the child cell
        flag[var]=1

        if var-1 not in A:
            if (var%dim)!=0 and flag[var-1]==0:
                A.append(var-1)
                fringe_list[var].append(var-1)
                
        if var-dim not in A:
            if (var-dim)>=0 and flag[var-dim]==0:
                A.append(var-dim)
                fringe_list[var].append(var-dim)
                
        if var+1 not in A:
            if (var+1)%dim!=0 and flag[var+1]==0:
                A.append(var+1)
                fringe_list[var].append(var+1)
                
        if var+dim not in A:
            if (var+dim)<=((dim**2)-1) and flag[var+dim]==0:
                A.append(var+dim)
                fringe_list[var].append(var+dim)
       
        if (len(A)>0):
            var=A.pop(len(A)-1)
        else:#stack is empty
            print ("path not found")
            break
       
    if (var==(dim**2)-1):#last cell is reached
        print ("path is found")
        global path
        path=1
# ---------Function stops------------ #
       
# ---------Function starts------------ # 
def find_path():
    k = dim**2-1
    final_path.append(dim**2-1)

    while (k!=0):

        if (k+dim)<=((dim**2)-1):
            if k in fringe_list[k+dim]:
                final_path.append(k+dim)
                k=k+dim

        if (k+1)%dim!=0:
            if k in fringe_list[k+1]:
                final_path.append(k+1)
                k=k+1

        if (k-dim)>=0:
            if k in fringe_list[k-dim]:
                final_path.append(k-dim)
                k=k-dim

        if (k%dim)!=0:
            if k in fringe_list[k-1]:
                final_path.append(k-1)
                k=k-1                
# ---------Function stops------------ #

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

# common function to load DFS steps
# returns no value
def generate_dfs():
    # calling function to find possible paths
    track()
    if (path==1):
        #if path exists, it will get the path indices and store them in final_path
        find_path()
        final_path.reverse()
##Step 1
#flag values of all the cells
flag=[]
initial_maze=[]
#a flag to know that the path is found and break out of the loop
path=0
#stack A
A = []
#the final path traversed
final_path=[]
#setting values for dim and p
dim, p = 100, 0.2

#initializing list to store possible fringe of every cell
fringe_list=[]

for i in range(dim**2):
	#creates a list of the fringe for every value of the current cell
    fringe_list.append([])

#calling function to create the maze with (dim,p)
flag =  MazeGen(dim,p)
# creating a copy of the maze to use for visualization
initial_maze = copy.deepcopy([x if x == 0 else 0.4 for x in flag])

##Step 2
generate_dfs()

##Step Last
if (path==1):
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