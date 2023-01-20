from math import inf
from shapely import Polygon, MultiPolygon
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.ops import unary_union

def ManhattanDistance(x1,y1,x2,y2) :
    return abs(x1-x2) + abs(y1-y2)

with open("puzzle15.txt") as file :
    puzzle = file.read().splitlines()
    
    minimum = 0
    maximum = 4000000
    length = maximum + 1
    #Map = MultiPolygon([Polygon([(0,0), (0,maximum), (maximum,maximum), (maximum,0), (0,0)])])
    Map = Polygon([(0,0), (0,maximum), (maximum,maximum), (maximum,0), (0,0)])

    """
    maximum = (4000000,4000000)
    length = 4000001
    """    
    for (i,line) in enumerate(puzzle) :
        line = line.split('Sensor at x=')[1].split(',')
        Sx = int(line[0])
        By = int(line[2].split(' y=')[1])
        line = line[1].split(' y=')[1].split(':')
        Sy = int(line[0])
        line = line[1].split(' x=')[1].split(',')
        Bx = int(line[0])
        distance = ManhattanDistance(Sx,Sy,Bx,By)
        west = (Sx - distance, Sy)
        east = (Sx + distance, Sy)
        north = (Sx, Sy - distance)
        south = (Sx, Sy + distance)
        listPolygon = []
        #polygonToRemove = Map.intersection(Polygon([north, west, south, east]))
        polygon = Map.difference(Polygon([north, west, south, east]))
        if polygon.geom_type == 'Polygon' and not polygon.is_empty:
            Map = polygon
        elif polygon.geom_type == 'MultiPolygon' :
            for p in polygon.geoms :
                if not p.is_empty :
                    listPolygon.append(p)
            Map = unary_union(listPolygon)
        gpd.GeoSeries([Map]).boundary.plot()
        plt.pause(0.05)
        plt.show()        


    print(Map.centroid.x * 4000000 + Map.centroid.y)
    #tuningFrequency = x * 4000000 + magicLine[1]

    
    

        