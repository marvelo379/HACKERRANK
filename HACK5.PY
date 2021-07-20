#CLOSEST NUMBER'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    arr.sort()
    diff_curr=arr[1]-arr[0]
    res=[arr[0],arr[1]]
    for i in range(1,len(arr)-1):
        if arr[i+1]-arr[i]<diff_curr:
            res=[]
            res.append(arr[i])
            res.append(arr[i+1])
            diff_curr=abs(arr[i+1]-arr[i])
        elif arr[i+1]-arr[i]==diff_curr:
            res.append(arr[i])
            res.append(arr[i+1])
    return res[:]        
        
        
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
**********************************************************
#THE MAXIMUM SUBARRAY'''''''''''''''''''''''''''''''''''''''''''''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    if max(arr)<0:
        return (max(arr),max(arr))
    a=0
    max_sum=0
    curr_sum=0
    for i in arr:
        if i>0:
            a=a+i
        curr_sum=max(0,curr_sum+i)
        max_sum=max(curr_sum,max_sum)
    return max_sum,a    
        



        
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
******************************************************
#COUNT ARRAY'''''''''''''''''''''''''''''''''''''''''''''''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countArray' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER x
#

def countArray(n, k, x):
    mod=10**9+7
    dp0=0
    dp1=0
    dp0old=1
    for i in range(2,n+1):
        dp0=(dp1*(k-1))%mod
        dp1=(dp0old + dp1*(k-2))%mod
        dp0old=dp0
    if x==1:
        return dp0
    return dp1
'''
p=(k-1)**(n-2)
if n%2==0:
    ot_total=(p-1)/k
    one_total=ot_total+1
else:
    ot_total=(p+1)/k
    one_total=other_total-1
'''
    
    
    # Return the number of ways to fill in the array.

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = int(first_multiple_input[2])

    answer = countArray(n, k, x)

    fptr.write(str(answer) + '\n')

    fptr.close()
**************************************