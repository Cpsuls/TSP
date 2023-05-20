import sys
import numpy as np
import itertools
import random
from numba import jit,njit
import math
@njit
def generate(n=10,a=0,b=100):
    points=[(random.randint(0,10),random.randint(10,11)) for i in range(n)]
    print(points)
    ind=['A','B','C','D','E','F','G','H','J','K','O']
    x=[point[0] for point in points ]
    y=[point[1] for point in points ]
    dicts={ind[i]:points[i] for i in range(len(points))}
    return dicts
np.set_printoptions(threshold=sys.maxsize)

def find_distance(dicts):
    distance_lsit=[]
    d=dicts
    lst=list(d.keys())
    combinations=np.array(list(itertools.permutations(lst,9)))[:math.factorial(len(lst)-1)]
    for el in combinations:
        el=np.append(el,'A')
        dist=[]
        for i in range(len(el)):
            try:
                point1=d[el[i]]
                point2=d[el[i+1]]
                dist.append(math.sqrt((point2[0]-point1[0])**2 +(point2[1]-point1[1])**2))
            except:
                distance_lsit.append(sum(dist))
                dist = []
                pass
    return min(distance_lsit),combinations.tolist()[distance_lsit.index(min(distance_lsit))]

print(find_distance(generate(n=10)))





