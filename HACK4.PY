"""
# Tree : TOP VIEW.............................
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value o(f the node)
"""
def topView(root):
    cu_level=[(root,0)]
    scores={}
    while cu_level:
        for _ in range(len(cu_level)):
            node,score=cu_level.pop(0)
            if not node:
                continue
            if score not in scores:
                scores[score]=node.info
            cu_level.extend([(node.left,score-1),(node.right,score+1)])  
    for  _,val in sorted(list(scores.items())):

        print(val,end=' ')
    #Write your code here
*************************************************
#LARGEST RECTANGLE.........................
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    if(len(h)==0):return
    if(len(h)==1):
        if(h[0]>largestRectangle.max):
            largestRectangle.max=n
        return
    v=min(h)
    if(v*len(h)>largestRectangle.max):
        largestRectangle.max=len(h)*v
    largestRectangle(h[0:h.index(v)])
    largestRectangle(h[h.index(v)+1:len(h)])
    return largestRectangle.max
largestRectangle.max=0
     
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
********************************************************
# PILLING UP....................
for _ in range(int(input())):
    
    _,l1=input(),list(map(int,input().split()))
    min_index=l1.index(min(l1))
    print("Yes" if sorted(l1[:min_index],reverse=True)==l1[:min_index] and sorted(l1[min_index:])==l1[min_index:] else "No")           
               
               
   