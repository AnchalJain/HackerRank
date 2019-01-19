#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
        sock={}
            for i in ar:
                        if not i in sock:
                                        sock[i] = 1
                                                else:
                                                                sock[i] += 1
                                                                    print(sock)
                                                                        value=sock.values()
                                                                            count=0
                                                                                for i in value:
                                                                                            count=count+i//2
                                                                                                return count



                                                                                            if __name__ == '__main__':
                                                                                                    fptr = open(os.environ['OUTPUT_PATH'], 'w')

                                                                                                        n = int(input())

                                                                                                            ar = list(map(int, input().rstrip().split()))

                                                                                                                result = sockMerchant(n, ar)

                                                                                                                    fptr.write(str(result) + '\n')

                                                                                                                        fptr.close()

