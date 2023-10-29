# 72. Edit Distance
# Medium
#Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
#
#You have the following three operations permitted on a word:
#
#    Insert a character
#    Delete a character
#    Replace a character
#
#
#
#Example 1:
#
#Input: word1 = "horse", word2 = "ros"
#Output: 3
#Explanation:
#horse -> rorse (replace 'h' with 'r')
#rorse -> rose (remove 'r')
#rose -> ros (remove 'e')
#
#Example 2:
#
#Input: word1 = "intention", word2 = "execution"
#Output: 5
#Explanation:
#intention -> inention (remove 't')
#inention -> enention (replace 'i' with 'e')
#enention -> exention (replace 'n' with 'x')
#exention -> exection (replace 'n' with 'c')
#exection -> execution (insert 'u')
#
#
#
#Constraints:
#
#    0 <= word1.length, word2.length <= 500
#    word1 and word2 consist of lowercase English letters.
#


#    # Intuition
#
#    For a dynamic programming problem you first need to find the recurrency formula, that's the one for the edit distance
#
#    ```
#
#    dist(word1, word2) = if len(word1) == 0:
#                            # cost of inserting remaining chars from word2
#                            return len(word2)
#
#                        if  len(word2) == 0:
#                            # cost of inserting remaining chars from word1
#                            return len(word1)
#
#                         if word1[0]==word[1] then
#                            # first char the same - return cost of remainder (no change needed for this case - cost zero)
#                            return dist(word1[1:], word2[1:])
#                         else 
#                            # s substition/deletion/insertion costs 1, choose the best of all possible cases
#                            return 1 + min(
#                                # insert char to second word 
#                                dist(word1[1:], word2),      
#                                # insert char to first word
#                                dist(word1,     word2[1:]),  
#                                # substiution of current char
#                                dist(word1[1:], word2[1:]),  
#                            )
#
#    ```
#    # Approach
#
#    Dynamic programming is just a fancy word for a program that implements this recurrent formula. You need to avoid computing the same value twice. This is done
#
#    1) in a recursive function that puts the result in a hash map, then reuses already computed values (this is called 'memoization'). This is done in function ```Solution.recur```
#
#    2) compute the formula from the bottom up, first for smallest values, then for larger one.  Put the intermediate results in a table. This is done in function ```Solution.table```
#
#    Now the recursive solution is running faster, why?
#
#    I made a visualization of the intermediate results for both cases. For some cases you see that the recursive solution is computing half of the amount of values, whereas the table driven solution is doing all of the computations. You can see this visualizaiton for the following case - you need to comment out the calls to function calls to ```Solution.shwoTbl``` and ```Solution.showMem```
#
#    ```
#    w1= "pneumonoultramicroscopicsilicovolcanoconiosis"
#    w2= "ultramicroscopically"
#    ```
#
#    I can't put in the table in here, the would be too large.
#
#
#
#
#    # Complexity
#    - Time complexity:
#    O(m*n) - m length of word1 n lenght of word2
#    - Space complexity:
#    O(m*n) - m length of word1 n lenght of word2
#
#    # Code
import math

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rc = Solution.recur(word1, word2)
        #tb = Solution.table(word1,word2)
        return rc
 

    def table(word1, word2):
        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))
            
        row = [0] * (len(word2)+1)
        table = [row.copy() for i in range(0,len(word1)+1) ]

        table[0][0] = 0
        for idx in range(0, len(word2)):
            table[0][idx+1] = idx+1

        for idx in range(0, len(word1)):
            table[idx+1][0] = idx+1

        for ridx in range(1, len(word1)+1):
            for cidx in range(1, len(word2)+1):     

                if word2[cidx-1] == word1[ridx-1]:

                    res = table[ridx-1][cidx-1]

                else:
                    a1 = table[ridx-1][cidx-1]
                    a2 = table[ridx][cidx-1]
                    a3 = table[ridx-1][cidx]

                    res = min(a1, a2, a3) + 1


                table[ridx][cidx] = res

        #Solution.shwoTbl(table)

        return table[-1][-1]
        


    def recur(word1, word2):
        mem={}
        rt = Solution.rec(word1, 0, word2, 0, mem)
        #Solution.showMem(mem, word1, word2)
        return rt


    def showMem(mem, word2, word1):
        row = [0] * (len(word2)+1)
        table = [row.copy() for i in range(0,len(word1)+1) ]

        for key, val in mem.items():
            ps = key.find("-")
            x = int(key[0:ps])
            y = int(key[(ps+1):])

            table[len(word1)-y][len(word2)-x] = val
        
        Solution.shwoTbl(table)

    def shwoTbl(table):
        for row in table:
            print(row)

    def rec(word1, pos1, word2, pos2, mem):

        key = f"{pos1}-{pos2}"
        if key in mem:
            return mem[key]

        if pos1 == len(word1):
            return len(word2) - pos2
        if pos2 == len(word2):
            return len(word1) - pos1


        if word1[pos1] == word2[pos2]:
            ret = Solution.rec(word1,pos1+1,word2,pos2+1, mem)
        else:
            sub1 = Solution.rec(word1,pos1+1,word2,pos2,mem)
            sub2 = Solution.rec(word1,pos1,word2,pos2+1,mem)
            sub3 = Solution.rec(word1,pos1+1,word2,pos2+1,mem)
            ret = 1 + min(sub1, sub2, sub3)

        mem[key] = ret
        return ret        


