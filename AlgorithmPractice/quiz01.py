# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 16:01:44 2022
@author: LMH
"""

def f1( x ) :
    a, b, c = 1, 2, 1
    return (a*x**2) + (b*x) + c

def f( x ) :
    y = x * x
    return y

def main() :
    print( f1(-1) )
    print( f(2) )

if (__name__ == "__main__") :
    main()
