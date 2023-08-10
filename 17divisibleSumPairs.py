#---> this solution uses hashmaps, hence the complexity is  O(n) 
def divisibleSumPairs1(n, k, ar):
    remainder_count = [0] * k
    count = 0
    
    for num in ar:
        remainder = num % k
        complement_remainder = (k - remainder) % k
        
        count += remainder_count[complement_remainder]
        remainder_count[remainder] += 1
    
    return count
#---> below solution uses loop , resulting in complexity of O(n^2). But it is more redable for a beginner
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    c=0
    for i in range(n):
        for j in range(i+1,n):
            if ( ar[i]+ar[j] ) % k==0:
                c+=1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
