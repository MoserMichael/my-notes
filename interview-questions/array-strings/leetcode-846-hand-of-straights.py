#846. Hand of Straights
#Medium
#Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.
#
#Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.
#
#
#
#Example 1:
#
#Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
#Output: true
#Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
#
#Example 2:
#
#Input: hand = [1,2,3,4,5], groupSize = 4
#Output: false
#Explanation: Alice's hand can not be rearranged into groups of 4.
#
#
#
#Constraints:
#
#    1 <= hand.length <= 104
#    0 <= hand[i] <= 109
#    1 <= groupSize <= hand.length
#
#
#
#Note: This question is the same as 1296: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
#

#- count frequency of all cards (variable `cnt`). set `next_low` to the minimum of all cards. also: sort the array of all cards (will be explained why this is needed) 
#- The inner loop (after first while) is assigning a consecutive sequence of cards starting with `next_low`.
#  - For each matching number the frequency count is decrement, as one number has been used in a card deal. Update the count of non zero count cards in variable `init_keys` - these are used to check if all cards have been dealt out.
#  - the inner loop tries to determine the initial value of the first card to be checked upon the next iteration. See variable `next_low` - if `next_low` has not been set and a card count is still bigger than zero after updating the frequency count then that's the new value of `next_low`.
#- after the inner loop: if we couldn't deal a consecutive sequence of `groupSize` element - return False
#- if all we had a hand and all cards have been dealt completely (`init_keys` is zero) then return True - we have dealt all cards in consecutive hands.
#- Now what will be the `next_low` - next card to be checked upon the next iteration? If this has not been established by the inner loop, then do a binary search among the sorted numbers for the next value (that's the reason why the cards had to be sorted) 
#

import bisect

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cnt = Counter(hand)        
        init_keys = len(cnt.keys())
        
        hand.sort()
        next_low = hand[0]

        #print(f"init {cnt}")

        while True:
            ckey = next_low
            next_low = -1
            csize = groupSize

            while csize > 0:
                cur = cnt.get(ckey)
                if cur:
                    csize -= 1
                    if cur == 1:
                        init_keys -= 1
                        if init_keys == 0:
                            break                            
                    cnt[ckey] = cur - 1

                    if next_low == -1 and cur > 1:
                        next_low = ckey
                else:
                    break
 
                ckey += 1
                

            #print(f"csize {csize} init_keys {init_keys} next_low {next_low} - {cnt}")
            if csize:
                return False

            if init_keys == 0:
                return True

            if next_low == -1:
                # find next after ckey - binsearch
                next_low_pos = bisect.bisect_right(hand, ckey-1)
                next_low = hand[next_low_pos]
                #print(f"-> set next low {next_low}")

        return False
    

