#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    if(n%2!=0):
        print("Weird")
    elif(n%2==0 and n==range(2,5)):
        print("Not Weird")
    elif(n%2==0 and n==range(6,20)):
        print("Weird")
    elif(n%2==0 and n==18):
        print("Weird")
    else:
        print("Not Weird")