#!/bin/python3

import math
import os
import random
import re
import sys

def maxRepeating(str):
 
    n = len(str)
    count = 0
    res = str[0]
    cur_count = 1
 
    # Traverse string except
    # last character
    for i in range(n):
         
        # If current character
        # matches with next
        if (i < n - 1 and
            str[i] == str[i + 1]):
            cur_count += 1
 
        # If doesn't match, update result
        # (if required) and reset count
        else:
            if cur_count > count:
                count = cur_count
                res = str[i]
            cur_count = 1
    return count

def decimalToBinary(n):
    return bin(n).replace("0b", "")

if __name__ == '__main__':
    n = int(input())
    n=str(decimalToBinary(n))
    res=maxRepeating(n)
    print(res)
    
