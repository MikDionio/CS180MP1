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

    for i in range(100):
        for j in range(200):
            map[i].append(math.sqrt((goal[1]-i)**2 + (goal[0]-j)**2))

    print(map[0][5])
    return

#Main

#Initialize Map
initMap(startPosition(), goalPosition())
