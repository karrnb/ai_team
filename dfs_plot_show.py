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

def update(i):
    # i+=1
    # print(initial_maze)
    # print(convertMaze(dim, initial_maze))
    temp_maze = initial_maze
    temp_maze[final_path[i]] = 0.6
    # print(convertMaze(dim, temp_maze))
    matrice.set_array(convertMaze(dim, temp_maze))

def MazeGen(dim, p):
    "Generates a random maze"
    index=random.sample(range(1,(dim**2)-1), int(p*(dim**2)))
    #print(index)
    maze=[]
    for i in range(dim**2):
        if i in index:
            maze.append(1)
        else:
            maze.append(0)
    return maze
    # return np.array_split(maze, dim)

def convertMaze(dim, maze):
    return np.array_split(maze, dim)

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
#a flag to know that the path is found and break out of the loop
path=0
#stack A
A = []
#the final path traversed
final_path=[]
#setting values for dim and p
dim, p = 20, 0.2

#initializing list to store possible fringe of every cell
fringe_list=[]

for i in range(dim**2):
	#creates a list of the fringe for every value of the current cell
    fringe_list.append([])

#calling function to create the maze with (dim,p)
initial_maze =  MazeGen(dim,p)
flag = copy.deepcopy(initial_maze)

##Step 2
generate_dfs()


##Step Last
# generating visualizations starts here
# initializing graph variables
fig, ax = plt.subplots()

# matrice = ax.matshow(convertMaze(dim, initial_maze),cmap=cm.red)
matrice = ax.matshow(convertMaze(dim, initial_maze))
# plt.colorbar(matrice)
plt.axis('off')

ani = animation.FuncAnimation(fig, update, frames=(len(final_path)), interval=100)
ax.legend_ = None
plt.show()