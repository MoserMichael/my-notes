# 68. Text Justification
# Hard
#Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
#
#You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
#
#Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
#
#For the last line of text, it should be left-justified, and no extra space is inserted between words.
#
#Note:
#
#    A word is defined as a character sequence consisting of non-space characters only.
#    Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
#    The input array words contains at least one word.
#
#
#
#Example 1:
#
#Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
#Output:
#[
#   "This    is    an",
#   "example  of text",
#   "justification.  "
#]
#
#Example 2:
#
#Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
#Output:
#[
#  "What   must   be",
#  "acknowledgment  ",
#  "shall be        "
#]
#Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
#Note that the second line is also left-justified because it contains only one word.
#
#Example 3:
#
#Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
#Output:
#[
#  "Science  is  what we",
#  "understand      well",
#  "enough to explain to",
#  "a  computer.  Art is",
#  "everything  else  we",
#  "do                  "
#]
#
#
#
#Constraints:
#
#    1 <= words.length <= 300
#    1 <= words[i].length <= 20
#    words[i] consists of only English letters and symbols.
#    1 <= maxWidth <= 100
#    words[i].length <= maxWidth
#



import io

class Solution:
    def fullJustify(self, tokens: List[str], maxWidth: int) -> List[str]:
        ret = []

        start_sentence = 0
        sum_sentence_length = 0

        idx = 0
        line_buf = io.StringIO()

        while idx < len(tokens):
            token = tokens[idx]
            assert len(token) <= maxWidth

            word_len = len(token)
            if sum_sentence_length != 0:
                word_len += 1

            if sum_sentence_length + word_len > maxWidth:

                ret.append( Solution.formatSentence(line_buf, start_sentence, idx, tokens, sum_sentence_length, maxWidth) )
                sum_sentence_length = len(token)
                start_sentence = idx
            else:
                sum_sentence_length += word_len

            idx += 1

        if start_sentence < len(tokens):
            ret.append(Solution.formatLastSentence(line_buf, start_sentence, len(tokens), tokens, sum_sentence_length, maxWidth) )

        return ret

    @staticmethod
    def formatLastSentence(line_buf, start_idx, end_idx, tokens, sum_sentence_length, max_length):
        line_buf.truncate(0)
        line_buf.seek(0)

        sentence_len = 0
        first_call = True
        while start_idx < end_idx:
            if not first_call:
                line_buf.write(" ")
                sentence_len += 1
            else:
                first_call = False
            line_buf.write(tokens[start_idx])
            sentence_len += len(tokens[start_idx])
            start_idx += 1

        if sentence_len < max_length:
            line_buf.write(' ' * (max_length - sentence_len))

        return line_buf.getvalue()



    @staticmethod
    def formatSentence(line_buf, start_idx, end_idx, tokens, sum_sentence_length, max_length):
        line_buf.truncate(0)
        line_buf.seek(0)

        num_words = end_idx - start_idx

        sum_of_words_len = sum_sentence_length - num_words + 1

        required_spaces = max_length - sum_of_words_len
        #print(f"required_spaces {required_spaces} num_words {end_idx - start_idx}")

        if num_words > 1:
            even_spaces = required_spaces // (num_words-1)
            odd_spaces =  required_spaces % (num_words-1)
        else:
            even_spaces = required_spaces
            odd_spaces = 0

        ret = io.StringIO()

        while start_idx < end_idx:
            if ret != "" and start_idx != (end_idx-1):
                num_spaces = even_spaces
                if odd_spaces != 0:
                    num_spaces += 1
                    odd_spaces -= 1
                line_buf.write(tokens[start_idx])
                line_buf.write(' ' * num_spaces)
            else:
                line_buf.write(tokens[start_idx])
                first_call = False
            start_idx += 1

        if num_words == 1:
            line_buf.write(' ' * required_spaces)

        return line_buf.getvalue()







