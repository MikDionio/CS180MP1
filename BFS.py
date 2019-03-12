import math

#Functions
def fileNameInput():
    fileName = input("Input filename: ")
    return fileName

def textToTuple(text):
    text = text.replace("(","")
    text = text.replace(")","")
    text = text.replace("\n","")
    text = text.split(",")
    # print(text)
    return ((int(text[0]),int(text[1])))

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

def removeFirst(list):
    n = list[0]
    list.pop(0)
    return n

def BFS(S, G, map, fringe):

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
                    fringe.append((left,n[1]))
                    map[left][n[1]] = n
            if(right < 100):
                if(map[right][n[1]] == 0):
                    fringe.append((right,n[1]))
                    map[right][n[1]] = n
            if(up >= 0):
                if(map[n[0]][up] == 0):
                    fringe.append((n[0],up))
                    map[n[0]][up] = n
            if(down < 200):
                if(map[n[0]][down] == 0):
                    fringe.append((n[0],down))
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
def Main():

    f = open(fileNameInput(), 'r')
    fileTxt = f.read()
    f.close()

    fileTxt = fileTxt.split('\n')

    startPos = textToTuple(removeFirst(fileTxt))
    goalPos = textToTuple(removeFirst(fileTxt))

    # print(startTxt)
    # print(goalTxt)
    if(fileTxt[len(fileTxt)-1] == ""):
        fileTxt.pop()
    # print(fileTxt)
    polygons = []
    i = 0
    for p in fileTxt:
        p = p.replace("(","")
        p = p.replace(")","")
        p = p.split(",")
        k = 0
        vertices = []
        while(k*2 < len(p)):
            vertices.append((int(p[2*k]),int(p[2*k+1])))
            # print(p[2*k])
            # print(p[2*k + 1])
            # print(i)
            # print(k)
            # print("\n")
            k = k + 1
        polygons.append(vertices)
        i = i + 1
    print(startPos)
    print(goalPos)
    for p in polygons:
        print(p)
    map = initMap(startPos,goalPos)
    fringe = [startPos]
    map[startPos[0]][startPos[1]] = startPos
    BFS(startPos, goalPos, map, fringe)
    print(getPath(startPos,goalPos,map))

Main()
