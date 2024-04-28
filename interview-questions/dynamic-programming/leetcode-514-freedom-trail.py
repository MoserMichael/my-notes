# 514. Freedom Trail
# Hard
#    In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial called the "Freedom Trail Ring" and use the dial to spell a specific keyword to open the door.
#
#    Given a string ring that represents the code engraved on the outer ring and another string key that represents the keyword that needs to be spelled, return the minimum number of steps to spell all the characters in the keyword.
#
#    Initially, the first character of the ring is aligned at the "12:00" direction. You should spell all the characters in key one by one by rotating ring clockwise or anticlockwise to make each character of the string key aligned at the "12:00" direction and then by pressing the center button.
#
#    At the stage of rotating the ring to spell the key character key[i]:
#
#        You can rotate the ring clockwise or anticlockwise by one place, which counts as one step. The final purpose of the rotation is to align one of ring's characters at the "12:00" direction, where this character must equal key[i].
#        If the character key[i] has been aligned at the "12:00" direction, press the center button to spell, which also counts as one step. After the pressing, you could begin to spell the next character in the key (next stage). Otherwise, you have finished all the spelling.
#
#
#
#    Example 1:
#
#    Input: ring = "godding", key = "gd"
#    Output: 4
#    Explanation:
#    For the first key character 'g', since it is already in place, we just need 1 step to spell this character.
#    For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two steps to make it become "ddinggo".
#    Also, we need 1 more step for spelling.
#    So the final output is 4.
#
#    Example 2:
#
#    Input: ring = "godding", key = "godding"
#    Output: 13
#
#
#
#    Constraints:
#
#        1 <= ring.length, key.length <= 100
#        ring and key consist of only lower case English letters.
#        It is guaranteed that key could always be spelled by rotating ring.
#

# Intuition
#
#    Looking at function ```slowRec```
#
#    This is searching through a binary tree of variants.
#    at each node there are two branches - one of searching forward and the other of searching backward in the ring.
#
#    The recursive function is an inner function ```def rec(path_cost, ring_pos, key_pos):``` 
#        - ```path_cost``` sum of the costs of all turns so far
#        - ```ring_pos``` current position in the ```ring``` string
#        - ```key_pos``` current position in the ```key``` string, each call is advancing key_pos by one.
#
#    Each call is searching for ```key[key_pos]``` in ring. One search is from ring[ring_pos] forward - while incrementing ```ring_pos```. The second search is searching backward - while decrementing ```ring_pos```
#
#    If a match is found then the distance is added to ```path_cost``` and a new recursive call is made, starting with the new ring position.
#
#    When key_pos has reached the length of the key string: in this case ```path_cost``` is the total cost of solving the riddle in the given way, so we have to update the minimum of all solutions computed so far.
#
#    Memoization. This approach is not fast enough, therefore we must avoid repeatedly solving the riddle for the same input. 
#
#    Therefore the ```rec``` function returns the minimum of all solutions acchieved so far. At each step the memoization is on two variables, the position within the key and the position within the ring - the combination of values identifies a given sub problem, so a concatenation of these values is the key to the memoization map. The value stored in the map is the best solution minus the current value of the ```path_cost``` - that is the best solution we can do for the subtree of the solution space, starting with the current position within the key and given the current position within the ring. 
#
#    If the memoization key is present in the memoization map, then check if the stored value added to the current ```path_cost``` is a better minimum than the current one.
#
#
#    I tried to speed up the solution with ```Solution.fasterRec``` by precomputing the lookup value for searching for a given character in the ring, so as to remove the inner loop. However this didn't speed things up - I guess memoization costs too much.
#
#


import math

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        #return Solution.slowRec(ring, key)
        return Solution.fasterRec(ring, key)

    # precomputing the distancces didn't help with performance - same percentage...
    # need to do this bottom-up. Probably. Memoization costs too much.
    def fasterRec(ring, key):
        min_path_cost = math.inf
        memo = {}

        ring_precomp=[]

        def precompute(ring):
            nonlocal ring_precomp

            for idx in range(len(ring)):
                add_map = {}
                sub_map = {}

                for ridx in range(len(ring)):
                    ch = ring[(idx+ridx) % len(ring)]
                    if not ch in add_map:
                        add_map[ch] = ridx

                    ch = ring[(idx-ridx) % len(ring)]
                    if not ch in sub_map:
                        sub_map[ch] = ridx

                ring_precomp.append( (add_map, sub_map) )

        def rec(path_cost, ring_pos, key_pos):
            nonlocal ring_precomp, min_path_cost, ring, key, memo

            if key_pos == len(key):
                min_path_cost = min(path_cost, min_path_cost)
                return path_cost

            tkey = f"{key_pos}-{ring_pos}"
            m = memo.get(tkey)
            if m:
                m += path_cost
                min_path_cost = min(m, min_path_cost)
                return m

            min_ret = math.inf

            ch = key[key_pos]
            r = ring_precomp[ring_pos][0].get(ch)
            if r is not None:
                res = rec(path_cost+r+1, (ring_pos+r) % len(ring), key_pos+1)
                min_ret = min(min_ret, res)

            r = ring_precomp[ring_pos][1].get(ch)
            if r is not None:
                res = rec(path_cost+r+1, (ring_pos-r) % len(ring), key_pos+1)
                min_ret = min(min_ret, res)

            memo[tkey] = min_ret - path_cost
            return min_ret

        precompute(ring)
        rec(0, 0, 0)

        return min_path_cost


    def slowRec(ring , key):
        min_path_cost = math.inf
        memo = {}

        def rec(path_cost, ring_pos, key_pos):
            nonlocal min_path_cost, ring, key, memo

            if key_pos == len(key):
                min_path_cost = min(path_cost, min_path_cost)
                return path_cost

            tkey = f"{key_pos}-{ring_pos}"
            m = memo.get(tkey)
            if m:
                m += path_cost
                min_path_cost = min(m, min_path_cost)
                return m

            # search right clockwise
            #rlen = len(ring)

            min_ret = math.inf

            for idx in range(len(ring)):
                if ring[(ring_pos+idx) % len(ring)] == key[key_pos]:
                    r = rec(path_cost+idx+1, (ring_pos+idx) % len(ring), key_pos+1)
                    min_ret = min(min_ret, r)
                    break

            for idx in range(0,len(ring)):
                if ring[(ring_pos-idx) % len(ring)] == key[key_pos]:
                    r = rec(path_cost+idx+1, (ring_pos-idx) % len(ring), key_pos+1)
                    min_ret = min(min_ret, r)
                    break

            memo[tkey] = min_ret - path_cost
            return min_ret

        rec(0, 0, 0)

        return min_path_cost

