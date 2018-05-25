# -*- coding:utf-8 -*-
principal = 1000
rate = 0.05
numyears = 5

year = 1

f = open("out.txt", "w")
while year <= numyears:
    principal = principal * (1 + rate)
    print >> f, "%3d %0.2f" % (year, principal)
    year += 1
f.close()
