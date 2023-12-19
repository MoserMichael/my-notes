# 1286. Iterator for Combination
# Medium
#    Design the CombinationIterator class:
#
#        CombinationIterator(string characters, int combinationLength) Initializes the object with a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
#        next() Returns the next combination of length combinationLength in lexicographical order.
#        hasNext() Returns true if and only if there exists a next combination.
#
#
#
#    Example 1:
#
#    Input
#    ["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
#    [["abc", 2], [], [], [], [], [], []]
#    Output
#    [null, "ab", true, "ac", true, "bc", false]
#
#    Explanation
#    CombinationIterator itr = new CombinationIterator("abc", 2);
#    itr.next();    // return "ab"
#    itr.hasNext(); // return True
#    itr.next();    // return "ac"
#    itr.hasNext(); // return True
#    itr.next();    // return "bc"
#    itr.hasNext(); // return False
#
#
#
#    Constraints:
#
#        1 <= combinationLength <= characters.length <= 15
#        All the characters of characters are unique.
#        At most 104 calls will be made to next and hasNext.
#        It is guaranteed that all calls of the function next are valid.
#


# that's a slow one. don't do it like this...

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.comb = []
        self.characters = characters
        self.combLength = combinationLength
        self.rec([], 0, 0)

    def rec(self, s, curPos, curVal):
        if curPos == self.combLength:
            self.comb.append( "".join(s) )
            return

        for pos in range(curVal, len(self.characters)-(self.combLength -curPos) + 1 ):

            s.append( self.characters[pos] )
            self.rec(s, curPos+1, pos+1)
            s.pop()

    def next(self) -> str:
        ret = self.comb[0]
        self.comb = self.comb[1:]
        return ret

    def hasNext(self) -> bool:
        return len(self.comb) != 0


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()


