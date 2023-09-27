#605. Can Place Flowers
#
#You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
#
#Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
#


class Solution:
    def canPlaceFlowers(self, flowerbed, n):

        addFlowers=0
        
        i=0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                j=i
                while j<len(flowerbed) and flowerbed[j]==0:
                    j += 1
                rangeLen=j-i
                if i==0:
                    rangeLen+=1
                if j==len(flowerbed):
                    rangeLen+=1


                addFlowers += (rangeLen-1) // 2   
                i=j
            else:
                i += 1

        return addFlowers >= n         
 
