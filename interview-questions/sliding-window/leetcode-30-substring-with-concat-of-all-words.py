# 30. Substring with Concatenation of All Words
# Hard
#You are given a string s and an array of strings words. All the strings of words are of the same length.
#
#A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.
#
#    For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.
#
#Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.
#
#
#
#Example 1:
#
#Input: s = "barfoothefoobarman", words = ["foo","bar"]
#Output: [0,9]
#Explanation: Since words.length == 2 and words[i].length == 3, the concatenated substring has to be of length 6.
#The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
#The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.
#The output order does not matter. Returning [9,0] is fine too.
#
#Example 2:
#
#Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
#Output: []
#Explanation: Since words.length == 4 and words[i].length == 4, the concatenated substring has to be of length 16.
#There is no substring of length 16 in s that is equal to the concatenation of any permutation of words.
#We return an empty array.
#
#Example 3:
#
#Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
#Output: [6,9,12]
#Explanation: Since words.length == 3 and words[i].length == 3, the concatenated substring has to be of length 9.
#The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"] which is a permutation of words.
#The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"] which is a permutation of words.
#The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"] which is a permutation of words.
#
#
#
#Constraints:
#
#    1 <= s.length <= 104
#    1 <= words.length <= 5000
#    1 <= words[i].length <= 30
#    s and words[i] consist of lowercase English letters.
#



 class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ret = []

        word_len = len(words[0])
        sum_of_len = len(words) * word_len
        word_freq = Solution.count_words(words)

        #print(f"text: {s} in_words {word_freq}")

        low=high=0
        words_in_window = {}

        while low <= (len(s) - sum_of_len) and high <= (len(s) - word_len):

            #Solution.verify_window(s, words_in_window, low, high, word_len)

            next_word = s[high : (high+word_len) ]

            expand_high = False

            if next_word in word_freq:

                wcount = Solution.add_freq(next_word, words_in_window, high)
                desired_count = word_freq[next_word]

                if wcount < desired_count:
                    expand_high = True
                elif wcount == desired_count:
                    is_match = Solution.has_match(words_in_window, word_freq)
                    if is_match:
                        ret.append(low)
                        #print(f"hit: {low}")
                    else:
                        expand_high = True

            if expand_high:
                high += word_len
            else:
                words_in_window = {}
                low = Solution.searchForWord(s, low+1, len(s) - sum_of_len+1, word_freq, word_len) #, visisted_pos_set)
                high=low

            #Solution.verify_window(s, words_in_window, low, high, word_len)

        return ret

    def searchForWord(s, low, to_pos, word_freq, word_len): #, visisted_pos_set):
        idx = low
        while idx <= to_pos:
            #if idx not in visisted_pos_set:
            next_word = s[idx : (idx+word_len) ]
            if next_word in word_freq:
                return idx
            idx += 1
        return idx


    def verify_window(s, words_in_window, low, high, word_len):

        valid = True
        for idx in range(low, high, word_len):
            word = s[ idx: (idx+word_len) ]
            if word not in words_in_window:
                #print(f"NOT-VALID word {word} at {idx} is missing")
                valid = False
                break

            pos_set = words_in_window[ word ]
            if idx not in pos_set:
                #print(f"NOT-VALID pos {idx} for word {word}  missing from {pos_set}")
                valid = False
                break

        for word, pos in words_in_window.items():
            for p in pos:
                if p < low or p > high:
                    #print(f"NOT-VALID out of range: {p} for word {word}")
                    valid = False
                    break

        #print(f"after {low}..{high} words_in_window {words_in_window} text: {s[low:high]}")
        assert valid


    def has_match(words_in_window, word_freq):
        if len(words_in_window) != len(word_freq):
            #print("not equal words")
            return False

        if words_in_window.keys() != word_freq.keys():
            #print("not equal keys")
            return False

        for word, pos_set in words_in_window.items():
            count = len(pos_set)
            if count != word_freq[word]:
                #print(f"count: word: {word}  - {count} != {word_freq[word]}")
                return False

        return True

    def dec_freq(word, words_in_window, low):
        ws = words_in_window.get(word)
        print(f"dec_freq {low} {word} {ws}")
        assert ws is not None, f"ws: {ws}"
        ws.remove(low)
        if len(ws) == 0:
            del words_in_window[word]


    def add_freq(next_word, words_in_window, word_pos ):
        if next_word not in words_in_window:
            words_in_window[ next_word ] = set([ word_pos ])
            return 1

        st = words_in_window[ next_word ]
        st.add(word_pos)

        return len(st)

    def count_words(words):
        word_freq = {}

        for word in words:
            word_freq[ word ] = word_freq.setdefault( word, 0) + 1

        return word_freq



