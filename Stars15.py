from math import inf

def ManhattanDistance(x1,y1,x2,y2) :
    return abs(x1-x2) + abs(y1-y2)

with open("puzzle15.txt") as file :
    puzzle = file.read().splitlines()
    Map = dict()
    minimum = (inf,inf)
    maximum = (0,0)
    lineNumber = 2000000
    Intersection = set()
    for line in puzzle :
        line = line.split('Sensor at x=')[1].split(',')
        Sx = int(line[0])
        By = int(line[2].split(' y=')[1])
        line = line[1].split(' y=')[1].split(':')
        Sy = int(line[0])
        line = line[1].split(' x=')[1].split(',')
        Bx = int(line[0])
        distance = ManhattanDistance(Sx,Sy,Bx,By)
        distanceToLine = abs(Sy - lineNumber)
        if distanceToLine <= distance :
            if Sx != Bx :
                Intersection.add(Sx)
            for x in range(1, distance - distanceToLine + 1) :
                if lineNumber != By or  Sx-x != Bx :
                    Intersection.add(Sx - x)
                if lineNumber != By or Sx+x != Bx:
                    Intersection.add(Sx + x)

        """if Sx - distance < minimum[0] :
            minimum = (Sx - distance,minimum[1])
        if Sy - distance < minimum[1] :
            minimum = (minimum[0],Sy - distance )
        if Sx + distance > maximum[0] :
            maximum = (Sx  + distance,maximum[1])
        if Sy + distance > maximum[1] :
            maximum = (maximum[0], Sy + distance)

        Map[(Sx,Sy)] = [(Bx,By), distance]"""

    count = len(Intersection)
    print(count)
    

        