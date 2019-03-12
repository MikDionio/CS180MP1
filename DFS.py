import math

#Functions
def startPosition():
    startx = int(input("Start pos x:"))
    starty = int(input("Start pos y:"))

    startPos = (startx,starty)
    print("Start: " + str(startPos))
    return startPos

def goalPosition():
    goalx = int(input("Goal pos x:"))
    goaly = int(input("Goal pos y:"))

    goalPos = (goalx,goaly)
    print("Goal: " + str(goalPos))
    return goalPos

def initMap(start, goal):
    map = [[] for i in range(101)]

    #This is heuristic function for A*
    # for i in range(100):
    #     for j in range(200):
    #         map[i].append(math.sqrt((goal[1]-i)**2 + (goal[0]-j)**2))

    #List all values for map as 0, meaning they have not been visited yet
    for i in range (100):
        for j in range(200):
            map[i].append(0)

    return map

def remove(list):
    n = list[0]
    list.pop(0)
    return n

def DFS(S, G, map, fringe):

    if(G == S):
        map[S[0]][S[1]] = S
    else:
        while(1):
            if not fringe:
                break

            n = fringe.pop(0)
            #print("N: " + str(n))
            #print(fringe)

            #Check if dequeued node is G
            if(n == G):
                break
            #Expand dequeued node
            down = n[1] + 1
            up = n[1] - 1
            left = n[0] - 1
            right = n[0] + 1

            #Insert unvisisted nodes to fringe
            if(left >= 0):
                if(map[left][n[1]] == 0):
                    fringe.insert(0,(left, n[1]))
                    map[left][n[1]] = n
            if(right < 100):
                if(map[right][n[1]] == 0):
                    fringe.insert(0,(right,n[1]))
                    map[right][n[1]] = n
            if(up >= 0):
                if(map[n[0]][up] == 0):
                    fringe.insert(0,(n[0],up))
                    map[n[0]][up] = n
            if(down < 200):
                if(map[n[0]][down] == 0):
                    fringe.insert(0,(n[0],down))
                    map[n[0]][down] = n

    return map

def getPath(S,G,map):
    path = []
    path.append(G)
    p = G
    while(path[0] != S):
        p = (map[p[0]][p[1]])
        path.insert(0,p)

    return path

#Main

#Input
S = startPosition()
G = goalPosition()

#Initialize map
map = initMap(S, G)

fringe = [S]
map[S[0]][S[1]] = S #Denote starting node as visited

DFS(S,G,map,fringe)
print(getPath(S,G,map))
