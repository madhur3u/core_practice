# https://leetcode.com/problems/happy-number/

def getNextNumber(n): # this function give me the next number
    
    sum1 = 0
    while (n > 0) :
        d = n % 10
        n = n / 10
        sum1 += d**2
        
    return sum1

class Solution(object):
    def isHappy(self, n): # main fn

        set1 = set()      # this set will store all numbers encountered till now
        
        while n != 1 :              # if n == 1 we found ans so yes            
            set1.add(n)             # add previous no. to set
            n = getNextNumber(n)    # get next number
            
            if n in set1:           # if we found n in set means in previous numbers we return false as the loop will repeat
                return False
        
        return n == 1               # this return true
