import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    sockpair = []
    matchCount = 0
    for i in range(0,n):
        current_color = ar[i]
        if(sockpair.__contains__(current_color)):
            matchCount +=1
            sockpair.remove(current_color.index)
        else:
            sockpair.append(current_color)
    return matchCount 


if __name__ == '__main__':


    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    print("Result ", sockMerchant(n,ar))



""" Solution that need to be pasted in hackerank"""

# import math
# import os
# import random
# import re
# import sys

# Complete the sockMerchant function below.
# def sockMerchant(n, ar):
#     sockpair = []
#     matchCount = 0
#     for i in range(0,n):
#         current_color = ar[i]
#         if(sockpair.__contains__(current_color)):
#             matchCount +=1
#             sockpair.remove(current_color)
#         else:
#             sockpair.append(current_color)
#     return matchCount 


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input())

#     ar = list(map(int, input().rstrip().split()))

#     result = sockMerchant(n, ar)

#     fptr.write(str(result) + '\n')

#     fptr.close()
