# 151. Reverse Words in a String
# Medium
#Given an input string s, reverse the order of the words.
#
#A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
#
#Return a string of the words in reverse order concatenated by a single space.
#
#Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
#
# 
#
#Example 1:
#
#Input: s = "the sky is blue"
#Output: "blue is sky the"
#
#Example 2:
#
#Input: s = "  hello world  "
#Output: "world hello"
#Explanation: Your reversed string should not contain leading or trailing spaces.
#
#Example 3:
#
#Input: s = "a good   example"
#Output: "example good a"
#Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
#
# 
#
#Constraints:
#
#    1 <= s.length <= 104
#    s contains English letters (upper-case and lower-case), digits, and spaces ' '.
#    There is at least one word in s.
#
# 
#
#Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?
#



class Solution:
    def reverseWords(self, s: str) -> str:
        #return Solution.simple(s)
        return Solution.reverse_inplace(s)

    @staticmethod
    def reverse_inplace(in_str):

        s = list(in_str)

        eof_left = len(s)
        eof_right = len(s)

        word_buf = []

        while True:
            #print(f"-> {s} eof_left {eof_left} eof_right {eof_right}")
            start_word = Solution.skipSpace(s, 0, eof_left)
            eof_word, word_len = Solution.skipNonSpace(s, start_word, eof_left, word_buf)
            after_word = Solution.skipSpace(s, eof_word, eof_left)

            Solution.moveToLeft(s, after_word, eof_left, -after_word)
            eof_left -= after_word

            #print(f"-> word_buf {word_buf[0:word_len]}")

            if word_len == 0:
                break


            Solution.copyBuf(s, eof_right - word_len, word_buf, word_len)
            eof_right -= word_len + 1
            if eof_right >= 0:
                s[eof_right] = ' '


        #print(f"!!! eof_right {eof_right} ::: {s}")
        if eof_right >= 0:
            eof_right += 1
            Solution.moveToLeft(s, eof_right, len(s), -eof_right)
            s = s[0: len(s) - eof_right]

        return "".join(s)





    @staticmethod
    def copyBuf(s, idx, buf, buf_len):
        for buf_idx in range(0,buf_len):
            s[idx+buf_idx] = buf[buf_idx]

    @staticmethod
    def moveToLeft(s, idx, eof_idx, diff):
        #print(f"moveToLeft idx {idx} eof_idx {eof_idx} {diff}")
        while idx < eof_idx:
            s[idx+diff] = s[idx]
            idx += 1

    @staticmethod
    def skipSpace(s, idx, eof_idx):
        while idx < eof_idx and s[idx].isspace():
            idx+= 1
        return idx

    @staticmethod
    def skipNonSpace(s, idx, eof_idx, buf):
        word_pos = 0
        while idx < eof_idx and not s[idx].isspace():
            if word_pos < len(buf):
                buf[word_pos] = s[idx]
            else:
                buf.append(s[idx])
            word_pos += 1
            idx+= 1
        return idx, word_pos



    @staticmethod
    def simple(s):
        reversedWordList = s.split()

        reversedWordList.reverse()

        return " ".join(reversedWordList)

