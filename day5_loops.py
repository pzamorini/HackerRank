import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    for i in range (1,11):
        if n >= 2 and n <= 20:
            result = n * i
            print(f'{n} x {i} = {result}')
            