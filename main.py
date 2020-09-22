import numpy as np
from array import *
from PyAstronomy.pyasl import planck

arrtemp = array('i',[])

n = int(input('Enter the amount of temperatures you would like: '))

for i in range(n):
    temp = int(input('Enter the next value: '))
    arrtemp.append(temp)

print(arrtemp)

arrfreq = array('q',[])

m = int(input('Enter the amount of temperatures you would like: '))

for q in range(m):
    freq = int(input('Enter the next value: '))
    arrfreq.append(freq)

print(arrfreq)

def planck(n,m):
    for (i,q) in range(n,m):
        planck(arrtemp,arrfreq)
        print(planck)
    return 
