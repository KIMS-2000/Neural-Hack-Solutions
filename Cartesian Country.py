#!/bin/python3

import sys

def getMaxBridges(x1, y1, x2, y2, xC, yC):
    if(x1==xC and y1==yC) or (x2==xC and y2==yC):
        return 0
    height = min(yC-y1,y2-yC)
    width = min(xC-x1, x2-xC)
    h = 2*height
    diags = h*width
    ups = height
    across = width
    return diags+ups+across
    # Complete this function

#  Return the maximum number of bridges the Rulers will commission.
x1, y1 = input().strip().split(' ')
x1, y1 = [int(x1), int(y1)]
x2, y2 = input().strip().split(' ')
x2, y2 = [int(x2), int(y2)]
xC, yC = input().strip().split(' ')
xC, yC = [int(xC), int(yC)]
result = getMaxBridges(x1, y1, x2, y2, xC, yC)
print(result)