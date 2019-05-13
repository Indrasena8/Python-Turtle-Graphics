from turtle import *
def polygon(n,l):
    for i in range(n):
        lt(360/n)
        fd(l)

def dc(r):
    c=2*3.1428*r
    n=50
    l=c/n
    polygon(n,l)

dc(50)
