#While running the code, enter the size of the map and the p value for filling the nodes. 
#For checking different algorithms, enter "BFS" for BFS, "DFS" for DFS, "astarmd" for A* using Manhattan
#Distance, "astared" for A* using Euclidean Distance in "Enter the algorithm" field for input.
import random
import math
import time
index=[]
FringeList=[]
path=[]
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
    if len(td)>0:
        while len(td)>0:
            td.pop(0)
    for j in range(k**2):
        td.append(0)

def inisl(k):
    if len(scoreList)>0:
        while len(scoreList)>0:
            scoreList.pop(0)
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

def Make_Fringe_BFS(MAZE,Qu,d):
    "Generates a fringe for a given cell"
    fringe=[]
    if (Qu[0]+d)<d**2:
        if MAZE[Qu[0]+d]==0 and Qu[0]+d not in Qu:
            fringe.append(Qu[0]+d)
    if (Qu[0]+1)%d!=0:
        if MAZE[Qu[0]+1]==0 and Qu[0]+1 not in Qu:
            fringe.append(Qu[0]+1)
    if (Qu[0]-d)>0:
        if MAZE[Qu[0]-d]==0 and Qu[0]-d not in Qu:
            fringe.append(Qu[0]-d)
    if Qu[0]%d!=0:
        if MAZE[Qu[0]-1]==0 and Qu[0]-1 not in Qu:
            fringe.append(Qu[0]-1)
    #print(fringe)
    FringeList[Qu[0]]=fringe
    return fringe

def Make_Fringe_DFS(MAZE,Qu,d):
    "Generates a fringe for a given cell"
    fringe=[]
    TOP=len(Qu)-1
    if (Qu[TOP]-d)>0:
        if MAZE[Qu[TOP]-d]==0 and Qu[TOP]-d not in Qu:
            fringe.append(Qu[TOP]-d)
    if Qu[TOP]%d!=0:
        if MAZE[Qu[TOP]-1]==0 and Qu[TOP]-1 not in Qu:
            fringe.append(Qu[TOP]-1)
    if (Qu[TOP]+d)<d**2:
        if MAZE[Qu[TOP]+d]==0 and Qu[TOP]+d not in Qu:
            fringe.append(Qu[TOP]+d)
    if (Qu[TOP]+1)%d!=0:
        if MAZE[Qu[TOP]+1]==0 and Qu[TOP]+1 not in Qu:
            fringe.append(Qu[TOP]+1)
    #print(fringe)
    FringeList[Qu[TOP]]=fringe
    return fringe

def BFS_Agent(MAZE,n):
    "Breadth First Search algorithm"
    BFS_Q=[]
    BFS_Q.append(0)
    p=0
    global nc
    nc=0
    while True:
        if (n**2)-1 in BFS_Q: 
            global s
            s="path found"
            #print("path found")
            break
        elif len(BFS_Q)==0:
            s="path not found"
            #print("path not found")
            break
        else:
            nc=nc+1
            BFS_Q = BFS_Q + Make_Fringe_BFS(MAZE,BFS_Q,n)
            MAZE[BFS_Q[0]]=1
            #print(BFS_Q.pop(0))
            p=BFS_Q.pop(0)
            #print(p)
    return p

def DFS_Agent(MAZE,n):
    "Depth First Search Algorithm"
    DFS_S=[0]
    global nc
    nc=0
    while True:
        if (n**2)-1 in DFS_S:
            global s
            s="path found"
            #print("path found")
            break
        elif len(DFS_S)==0:
            s="path not found"
            #print("path not found")
            break
        else:
            top=len(DFS_S)-1
            temp=DFS_S[top]
            nc=nc+1
            DFS_S=DFS_S+Make_Fringe_DFS(MAZE,DFS_S,n)
            MAZE[DFS_S[top]]=1
            DFS_S.remove(temp)
            #print(DFS_S)
            #print(temp)
    return temp

def parent(node):
    "Returns parent node"
    if node==0:
        return 0
    for a in FringeList:
        if node in a:
            return FringeList.index(a)

def pathGen(c): #Displays the indices of nodes in 1-D list
    "displays a path"
    pl=0
    while c!=0:
        print(c)
        pl+=1
        c=parent(c)
    return pl   

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

def h_ed(n,dim):
    "Euclidean Distance heuristic function"
    z=0
    x = int(n/dim)+1
    y = (n%dim)+1
    z = ((dim-x)**2) + ((dim-y)**2)
    return int(math.sqrt(z))

def h_md(n,dim):
    "Manhattan Distance heuristic function"
    z=0
    x = int(n/dim)+1
    y = (n%dim)+1
    z = (dim-x) + (dim-y)
    return z

def perm_md(F,dim):
    "Permutes a given list based on score calculation using a heuristic function;"
    "and assigns priority in the returned list;"
    "the node with highest priority is appended in the end"
    score=0
    a=[]
    b=[]
    c=[]
    for i in F:
        if scoreList[i]!=0:
            a.append([i,scoreList[i]])
        else:
            score=td[i]+h_md(i,dim)
            scoreList[i]=score
            a.append([i,score])
    for i in a:
        b.append(i[1])
    b.sort()
    b.reverse()
    for j in b:
        for k in a:
            if j in k and k[0] not in c:
                c.append(k[0])
                break
    return c

def perm_ed(F,dim):
    "Permutes a given list based on score calculation using a heuristic function;"
    "and assigns priority in the returned list;"
    "the node with highest priority is appended in the end"
    score=0
    a=[]
    b=[]
    c=[]
    for i in F:
        if scoreList[i]!=0:
            a.append([i,scoreList[i]])
        else:
            score=td[i]+h_ed(i,dim)
            scoreList[i]=score
            a.append([i,score])
    for i in a:
        b.append(i[1])
    b.sort()
    b.reverse()
    for j in b:
        for k in a:
            if j in k and k[0] not in c:
                c.append(k[0])
                break
    return c
        
def A_star_md(MAZE,dim):
    "A* Algorithm with Manhattan Distance as heuristic function"
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
            s="path not found"
            #print(s)
            break
        else:
            nc=nc+1
            temp=AQ[len(AQ)-1]
            #print(temp)
            AQ = AQ + Make_Fringe_AS(MAZE,AQ,dim)
            MAZE[temp]=1
            AQ.remove(temp)
            AQ=perm_md(AQ,dim)
            #print(AQ)
    return(temp)
 
def A_star_ed(MAZE,dim):
    "A* Algorithm with Euclidean Distance as heuristic function"
    AQ=[0]
    global nc
    nc=0
    while True:
        if (dim**2)-1 in AQ:
            global s
            s="path found"
            print(s)
            break
        elif len(AQ)==0:
            s="path not found"
            print(s)
            break
        else:
            nc=nc+1
            temp=AQ[len(AQ)-1]
            #print(temp)
            AQ = AQ + Make_Fringe_AS(MAZE,AQ,dim)
            MAZE[temp]=1
            AQ.remove(temp)
            AQ=perm_ed(AQ,dim)
            #print(AQ)
    return(temp)

#pathList=[]
#nc_list=[]
#c=0
#for i in range(100):
#    pathList.append(0)
#for i in range(100):
#    nc_list.append(0)
#while c<1:
#    M=MazeGen(100,0.1)
#    ltn=A_star(M,100)
#    if s=="path found":
        #pathList[c]=pathGen(ltn)+1
        #count=count+1
#        nc_list[c]=nc
#        c=c+1
#print("count = ",count)
    #print("\n")
#print(nc_list)


#Generates a map at random and solves it using one of the algorithms

d=int(input("Enter the dimension: "))
pr=float(input("Enter the probability: "))
S=input("Enter the algorithm: ")
if S=="BFS":
    M=MazeGen(d,pr)
    ltn=BFS_Agent(M,d)
    if s=="path found":
        print("Length of Path: ",pathGen(ltn)+1)
    else:
        print("path not found")
elif S=="DFS":
    M=MazeGen(d,pr)
    ltn=DFS_Agent(M,d)
    if s=="path found":
        print("Length of Path: ",pathGen(ltn)+1)
    else:
        print("path not found")
elif S=="astared":
    M=MazeGen(d,pr)
    ltn=A_star_ed(M,d)
    if s=="path found":
        print("Length of Path: ",pathGen(ltn)+1)
    else:
        print("path not found")
elif S=="astarmd":
    M=MazeGen(d,pr)
    ltn=A_star_md(M,d)
    if s=="path found":
        print("Length of Path: ",pathGen(ltn)+1)
    else:
        print("path not found")
else:
    print("wrong algorithm code")



#start_time=time.clock()
#print(time.clock()-start_time,"seconds")



            
            
    

