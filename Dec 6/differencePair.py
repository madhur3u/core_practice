# https://practice.geeksforgeeks.org/problems/find-pair-given-difference1559/1#
class Solution:

    def findPair(self, arr, L,N):
        #code here
        
        arr.sort()  # sort the array
        lo = 0
        hi = 1
        
        while (lo < L and hi < L) :
            # if diff = n then we got ans
            if arr[hi] - arr[lo] == N :
                return True
              
            # if diff < n we increase the higher one else lower one
            elif arr[hi] - arr[lo] < N :
                hi += 1
            else :
                lo += 1
        
        return False
