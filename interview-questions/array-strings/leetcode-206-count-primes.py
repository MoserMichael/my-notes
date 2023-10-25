# 204. Count Primes
# Medium
#    Given an integer n, return the number of prime numbers that are strictly less than n.
#
#     
#
#    Example 1:
#
#    Input: n = 10
#    Output: 4
#    Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
#
#    Example 2:
#
#    Input: n = 0
#    Output: 0
#
#    Example 3:
#
#    Input: n = 1
#    Output: 0
#
#     
#
#    Constraints:
#
#        0 <= n <= 5 * 106
#


#    # Intuition
#
#    That's the sieve of Erastophenes, learned this one in school.
#
#    # Approach
#
#    How can you make this one fast in python? I tries simple sieve of Erastophenes with array entry for each number, tried the same with a bit vector instead of an integer array, even adapted the sieve of Sundaram from the wikipedia article (here https://en.wikipedia.org/wiki/Sieve_of_Sundaram )  - still the best result is the first one - and is only 28% better than the worst entry.
#
#    # Complexity
#    - Time complexity: O(n* 2)
#
#    - Space complexity:
#    O(n)
#


class Solution:
    def countPrimes(self, n: int) -> int:
        #return Solution.sietheSundaram(n)
        #return Solution.siethePacked(n)
        return Solution.siethe(n)

    def sietheSundaram(n):
        # copied from wikipedia https://en.wikipedia.org/wiki/Sieve_of_Sundaram
        k = (n - 2) // 2
        integers_list = [True] * (k + 1)
        for i in range(1, k + 1):
            j = i
            while i + j + 2 * i * j <= k:
                integers_list[i + j + 2 * i * j] = False
                j += 1

        #if n > 2:
        #    print(2, end=' ')

        count_res = 0
        if n > 2:
            count_res += 1
        for i in range(1, k + 1):
            if integers_list[i]:
                count_res += 1
                #print(2 * i + 1, end=' ')

        return count_res

    # this one is too slow, gets 'time limit exceeded', but it doesn't get stuck!
    def siethePacked(n):
        num_entries = ((n >> 5) + 1)
        arr = [0] * num_entries

        for num in range(2,n):
            #if not Solution.isBitSet(arr,num):
            test = arr[ num >> 5 ] & (1 << (num & 31))
            if test == 0:
                for n_num in range(num+num, n, num):
                    arr[ n_num >> 5 ] |= 1 << (n_num & 31)
                    #Solution.setBit(arr, n_num)

        count = 0
        for idx in range(0,num_entries):
            count += arr[idx].bit_count()
            #count += Solution.countBitsInInt(arr[idx])

        return max(n - count - 2, 0)

    def setBit(arr, n):
        arr[ n >> 5 ] |= 1 << (n & 31)

    def isBitSet(arr, n):
        return arr[ n >> 5 ] & (1 << (n & 31))


    def siethe(n):
        arr = [0] * max(2,n)

        for num in range(2,n):
            if arr[num] == 0:
                for n_num in range(num+num, n, num):
                    arr[n_num] = 1

                #n_num = num + num
                #while True:
                #    if n_num >= n:
                #        break
                #    arr[n_num] = 1
                #    n_num += num


        #count = 0
        #for num in range(2,n):
        #    if arr[num] == 0:
        #        count += 1
        #return count

        return max(arr.count(0)-2, 0)



