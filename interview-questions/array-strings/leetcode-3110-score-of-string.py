#3110. Score of a String
#Easy
#You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.
#
#Return the score of s.



#    Two solutions: the first solution is a one-liner with reduce, the second solution is using reduce with a local function (not one liner). (If you get this question at a job interview with Python then a follow-up question might be to solve the same problema with reduce)
#
#    ## one-liner with reduce
#
#    See ```Solution.oneLineReduce```
#
#    Starting with inital tuple value ```(0, s[0])``` - first element of the tuple is the initial sum value, second element will be used by the lambda function as the previous character of the input sequence.
#
#    the lambda function passed to ```reduce``` will be called for the second character of the string onward, second argument to ```reduce``` is ```s[1:]```
#
#    Function called on each iteration: 
#    ```lambda prev, cur : (prev[0]+abs(ord(cur)-ord(prev[1])), cur)```
#
#    ```abs(ord(cur)-ord(prev[1]))``` - compute the absolute difference between ascii value of current character ```cur``` and the previous character ```prev[1]```; then add the absolute difference to the accumulated sum of differences computed by the the previous step - that one is in ```prev[0]+ ... ```,
#
#    Return this value as the first element of a tuple ```( <result of computation>, cur )``` where the second value is the current character (will be the previous character in the next iteration)
#
#    The solution returns the first element of the tuple returned by ```reduce``` - which is the accumulated value.
#
#    I am not sure that this solution is better then doing it with a loop, the loop is easier to read and probably faster then creating a tuple for each element of the string.
#
#    ## reduce with local function
#
#    See ```Solution.reduce_fast```
#
#    A faster solution with ```reduce``` - here a local function is used that accesses a local variable that is out of the scope of the function. This variable is ```prev_ch``` and it holds the previous character. This solution is faster, it does not create a tuple for each character of the input string, howeve this one is assigning values to a non local variable and can't be written as a one liner.
#
from functools import reduce

class Solution:
    def scoreOfString(self, s: str) -> int:
        return Solution.reduce_fast(s)

    def reduce_fast(s):        
        prev_ch = s[0]

        def sum_it(prev, cur):
            nonlocal prev_ch
            ret=prev+abs(ord(cur)-ord(prev_ch))
            prev_ch=cur
            return ret

        return reduce(sum_it, s[1:], 0)

    def oneLineReduce(s):        
        return reduce(lambda prev, cur : (prev[0]+abs(ord(cur)-ord(prev[1])), cur), s[1:], (0, s[0]))[0]
        

