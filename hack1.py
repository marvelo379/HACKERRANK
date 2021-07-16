#bigger is greater
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    res=" "
    n=len(w)
    w=list(w)
    i=n-2
    while i>=0 and w[i]>=w[i+1]:
        i=i-1
    if i==-1:
        res="no answer"
    else:
        j=n-1
        while j>=i and w[j]<=w[i]:
            j=j-1
        w[i],w[j]=w[j],w[i]
        w="".join(w)
        res=w[:i+1] + w[i+1:][: :-1]
    return res    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
#strange grid again
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'strangeGrid' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER r
#  2. INTEGER c
#

def strangeGrid(r, c):
    return ((r-(r%2==0))//2*10+(r%2==0)+(c-1)*2)
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    result = strangeGrid(r, c)

    fptr.write(str(result) + '\n')

    fptr.close()
# even tree
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
    wt={}
    for i in range(t_edges-1,-1,-1):
        if t_from[i] in wt:
            wt[t_from[i]]+=1
        else:
            wt[t_from[i]]=1
        if t_to[i] in wt:
            wt[t_to[i]]+=wt[t_from[i]]
        else:
            wt[t_to[i]]=wt[t_from[i]]
    return (len([1 for key in wt if wt[key]%2==0]))        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_nodes, t_edges = map(int, raw_input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in xrange(t_edges):
        t_from[i], t_to[i] = map(int, raw_input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)

    fptr.write(str(res) + '\n')

    fptr.close()
