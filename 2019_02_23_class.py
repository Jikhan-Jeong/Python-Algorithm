# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 17:37:54 2019

@author: Jikhan Jeong
"""

## 2019_02_23_class
## reference : annotated algorithms in python with application in physics, biology and finance
## reference : https://github.com/mdipierro/nlib
## book p.182


import os
print("Current Working Directory " , os.getcwd())
os.chdir("C:/python/a_python/2019_python/")

class complex(object):
    z=2
    def __init__(self, real =0.0, imag = 0.0):
        self.real, self.imag = real, imag
    def magnitude(self):
        return(self.real**2 + self.imag**2)**0.5
    def __add__(self, other):
        return complex(self.real + other.real, self.imag + other.imag)
    
a = complex(1,3)    
b = complex(2,1)
c = a+b
c
print (c.magnitude())
(c.magnitude())

class MyList(object):
    def __init__(self,*a): self.a =list(a)
    def __len__(self): return len(self.a)
    def __getitem__(self, key): return self.a[key]
    def __setitem__(self, key, value): self.a[key] = value
    
b = MyList(3,4,5)    
b[0]
b.a[0]=7
b.a

from datetime import date
from math import exp

today = date.today()
r_free = 0.05/365.0


## Bond Prenet value PV(t, Principle = A) = A*exp(-trade duration* interest_rate)

class FinancialTranscation(object):
    def __init__(self, t,a, description =''):
        self.t =t
        self.a =a
        self.description = description
    def pv(self, t0 = today, r = r_free): # t0 and r is given
        return self.a*exp(r*(t0-self.t).days) # t0-t means period in temrs of days
    def __str__(self):
        return '%.2f dollars in %i days (%s)' % (self.a, self.t, self.description)

class CashFlow(object):
    def __init__(self):
        self.transations = []
    def add(self, transaction):
        self.transations.append(transaction)
    def pv(self,t0, r=r_free):
        return sum(x.pv(t0,r) for x in self.transations)
    def __str__(self):
        return '\n'.join(str(x) for x in self.transations)
        
bond = CashFlow()        
today = date(2019,2,23)        
for year in range(2019, 2021):
    for month in range(1,13):
        coupon = FinancialTranscation(date(year,month,20), 1000) # period, principle
        bond.add(coupon)
        
print(round(bond.pv(today, r=0.05/365),0)) # r = risk free =0
