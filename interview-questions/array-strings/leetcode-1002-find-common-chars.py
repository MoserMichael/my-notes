#1002. Find Common Characters
#Easy
#
#Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
#
# 
#
#Example 1:
#
#Input: words = ["bella","label","roller"]
#Output: ["e","l","l"]
#
#Example 2:
#
#Input: words = ["cool","lock","cook"]
#Output: ["c","o"]
#
# 
#
#Constraints:
#
#    1 <= words.length <= 100
#    1 <= words[i].length <= 100
#    words[i] consists of lowercase English letters.
#
#

#The following solution is in three lines, but you can combine it into a somewhat complex one liner ;-)
#
## Intuition
#Finding the intersection set of all letters for all words does not solve the problem. The reason: if a letter appears twice in the intersection string, then it has to appear twice in the answer. Therefore we need to find a map, where the keys are the letters in the intersection string, which are mapped to the number of occurences of each letter in the intersection of all strings.
#
## Solution
#
#The following line finds this intersection map
#
#`res = reduce(lambda prev, cur : common_map(prev, Counter(cur)), words[1:], Counter(words[0]) )`
#
#The initial value is a map of character counts for the first word, produced by `Counter(words[0])`
#
#Now for each of the other words we find this intersection by calling `common_map(prev, Counter(cur))` lets look at function `common_map`
#
#An example of calling `common_map` explains it purpose:
#<pre>
#>>> common_map(Counter("aabbcc"), Counter("abbcccc"))
#{'b': 2, 'a': 1, 'c': 2}
#</pre>
#
#Here are the details:
#
#`common_map = lambda a,b :  dict( map(lambda val : (val, min(a[val],b[val])), set(a.keys()).intersection(set(b.keys())) `
#
#The key values common in both maps `a` and `b` is produced by `set(a.keys()).intersection(set(b.keys())` Now this set is converted into a list of tuples, where the first element is the character present in both dictionaries and he value is the common number of occurances in both maps `(val, min(a[val],b[val]))` - all this is repeated for each element of the intersection by `map` - the result is then converted back to a dictionary (dict receives list of tuples to key-value entries of the dictionary)
#
#We are not done yet! as a result we have the common character counts: now this is turned into the return value by means of
#
#`return itertools.chain.from_iterable([ [x[0]] * x[1]  for x in res.items() ])`
#
#The inner expression produces a list of lists,
#
#for the argument value
#<pre>
#>>> res = {'b': 2, 'a': 1, 'c': 2}
#>>> [ [x[0]] * x[1]  for x in res.items() ]
#[['b', 'b'], ['a'], ['c', 'c']]
#</pre>
#
#This result is flattened into the return value by calling `itertools.chain.from_iterable`
#
## Code
#
import itertools

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        common_map = lambda a,b :  dict( map(lambda val : (val, min(a[val],b[val])), set(a.keys()).intersection(set(b.keys())) ) )
        res = reduce(lambda prev, cur : common_map(prev, Counter(cur)), words[1:], Counter(words[0]) )
        return itertools.chain.from_iterable([ [x[0]] * x[1]  for x in res.items() ])

