#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    n=math.ceil(math.sqrt(len(s)))
    p=' '.join(map(lambda x:s[x: :n],range(n)))
    return p
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#

def twoArrays(k, A, B):
    return "YES" if all(a+b>=k for a,b in zip(sorted(A,reverse=True),sorted(B))) else "NO"
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input().strip())

    for q_itr in xrange(q):
        first_multiple_input = raw_input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = map(int, raw_input().rstrip().split())

        B = map(int, raw_input().rstrip().split())

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()
