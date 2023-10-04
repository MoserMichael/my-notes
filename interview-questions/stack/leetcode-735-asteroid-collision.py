# 735. Asteroid Collision
# Medium
#We are given an array asteroids of integers representing asteroids in a row.
#
#For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
#
#Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
#
# 
#
#Example 1:
#
#Input: asteroids = [5,10,-5]
#Output: [5,10]
#Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
#
#Example 2:
#
#Input: asteroids = [8,-8]
#Output: []
#Explanation: The 8 and -8 collide exploding each other.
#
#Example 3:
#
#Input: asteroids = [10,2,-5]
#Output: [10]
#Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
#
# 
#
#Constraints:
#
#    2 <= asteroids.length <= 104
#    -1000 <= asteroids[i] <= 1000
#    asteroids[i] != 0
#




class Solution:
    def asteroidCollision(self, asteroids):

        stack = []
        
        curIdx = 0
        while curIdx < len(asteroids):
            #print(f"? curIdx: {curIdx} stack {stack} ast {asteroids}")

            if not len(stack):
                stack.append(asteroids[curIdx])
                asteroids = asteroids[1:]
            else:
                while curIdx < len(asteroids):
                    cur = asteroids[curIdx]
                    #print(f"{stack} {asteroids[curIdx:]}")
                    if len(stack) == 0:
                        break
                    topOfStack = stack[-1]
                    if topOfStack * cur < 0 and cur < 0:
                        if abs(topOfStack) == abs(cur):
                            stack.pop()
                            curIdx += 1
                            
                        elif abs(topOfStack) < abs(cur):
                            stack.pop()                        
                        elif abs(topOfStack) > abs(cur):
                            curIdx += 1
                            break
                    else:
                        stack.append(cur)
                        curIdx += 1
                        break
        
        return stack


