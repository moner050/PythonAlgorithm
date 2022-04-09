# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 16:18:07 2022
@author: LMH
"""

# Fibonacci Function

# Recursive Function
def fibonacci( x ) :
    """
    # 이건 if문 3개
    if x == 0:
        return 0
    elif x == 1:
        return 1
    elif x > 1 :
        return fibonacci( x - 1 ) + fibonacci( x - 2 )
    """
    # 요건 하나
    if ( x < 2 ) : 
        return x
    y = fibonacci( x - 1 ) + fibonacci( x - 2 )
    return y
    
###########################################################################
# Without Recursive Function
def f1( n ):
    
    """
    aList = [0] * (n+1)

    aList[1] = 1
    
    for i in range( 2, n+1 ):
        aList[i] = aList[i - 1] + aList[i - 2]
        
    return aList[n]
    """
    # if문 없이 Fibonacci 수열 만들
    fn = [0]*( n + 1 )
    fn[1] = 1
    for x in range( 2, n+1 ):
        fn[x] = fn[x - 1] + fn[x - 2]
        
    return fn[n]
###########################################################################
# Not Recursive Function
def f3( n ) :
    # 요건 하나
        
    fn = [0]*( n + 1 )
    fn[1] = 1
    for x in range( 2, n+1 ):
        fn[x] = fn[x - 1] + fn[x - 2]
    
    if ( n < 2 ) : 
        fn[n] = n
    elif ( n >= 2) :
        if f3 in fn :
            return f3( n - 1 ) + f3( n - 2 )
    
# 0, 1, 1, 2, 3, 5, 8, 13
def main() :
    for n in range(1, 10):
        print( fibonacci(n), end=" " )
    
    print("\n")
    
    for n in range(1, 5 + 1):
        print( f1(n), end=" " )
    
    print("\n")
    
    for n in range(1, 5 + 1):
        print( f3(n), end=" " )

if (__name__ == "__main__") :
    main()
