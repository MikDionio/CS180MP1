import math
from matplotlib import pyplot as plt

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

def initMapUninformed(start, goal):
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

def DFS(S, G, map):
    fringe = [S]
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
def Input():

    #Obtain input file text, ensure input file is in same directory
    f = open(fileNameInput(), 'r')
    fileTxt = f.read()
    f.close()

    #Divide input text by line
    fileTxt = fileTxt.split('\n')

    #First line is start pos
    startPos = textToTuple(removeFirst(fileTxt))

    #Next line is goal pos
    goalPos = textToTuple(removeFirst(fileTxt))

    # print(startTxt)
    # print(goalTxt)

    #Remove empty line from end of list
    if(fileTxt[len(fileTxt)-1] == ""):
        fileTxt.pop()
    # print(fileTxt)

    #Obtain polygon vertices
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

    #Print inputs
    print(startPos)
    print(goalPos)
    for p in polygons:
        print(p)

    inputs = []
    inputs.append(startPos)
    inputs.append(goalPos)
    for p in polygons:
        inputs.append(p)

    return inputs

def DFSProper(startPos, goalPos, polygons):
    map = initMapUninformed(startPos,goalPos)
    #fringe = [startPos]
    map[startPos[0]][startPos[1]] = startPos
    DFS(startPos, goalPos, map)
    path = getPath(startPos,goalPos,map)
    print(path)
    x = []
    y = []
    for p in path:
        x.append(p[0])
        y.append(p[1])
    plt.plot(x,y)
    plt.show()
Input = Input()
DFSProper(removeFirst(Input), removeFirst(Input), Input)
