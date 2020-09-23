import numpy as np
from array import *

arrtemp = array('i',[])

m = int(input('Enter the amount of temperatures you would like: '))

for i in range(m):
    temp = int(input('Enter the next value: '))
    arrtemp.append(temp)

print(arrtemp)

arrfreq = array('q',[])

n = int(input('Enter the amount of temperatures you would like: '))

for q in range(n):
    freq = int(input('Enter the next value: '))
    arrfreq.append(freq)

print(arrfreq)

def planck(m,n):
    h = 6.62606896**(−34)
    c = 2.99792458**8
    k = 1.3806504**(−23)
    v = arrfreq
    T = arrtemp
    x = (2*h*(v**3/c**2))*(exp(hv/k*T)-1)**(-1)
