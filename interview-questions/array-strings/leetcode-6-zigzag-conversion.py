# 6. Zigzag Conversion
# Medium
#    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
#    P   A   H   N
#    A P L S I I G
#    Y   I   R
#
#    And then read line by line: "PAHNAPLSIIGYIR"
#
#    Write the code that will take a string and make this conversion given a number of rows:
#
#    string convert(string s, int numRows);
#
#
#
#    Example 1:
#
#    Input: s = "PAYPALISHIRING", numRows = 3
#    Output: "PAHNAPLSIIGYIR"
#
#    Example 2:
#
#    Input: s = "PAYPALISHIRING", numRows = 4
#    Output: "PINALSIGYAHRPI"
#    Explanation:
#    P     I    N
#    A   L S  I G
#    Y A   H R
#    P     I
#
#    Example 3:
#
#    Input: s = "A", numRows = 1
#    Output: "A"
#
#
#
#    Constraints:
#
#        1 <= s.length <= 1000
#        s consists of English letters (lower-case and upper-case), ',' and '.'.
#        1 <= numRows <= 1000
#


class Entry:
    def __init__(self, offset_input, jump_input, offset_output, jump_output):
        self.offset_input = offset_input
        self.jump_input = jump_input
        self.offset_output = offset_output
        self.jump_output = jump_output

    def __repr__(self):
        return f"(in: {self.offset_input} {self.jump_input} out: {self.offset_output} {self.jump_output})"

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if len(s) <= numRows or numRows == 1:
            return s

        elm_in_row = numRows
        if numRows > 2:
            elm_in_row += numRows - 2

        fill_arr = []

        for idx in range(0, elm_in_row):
            if idx < numRows:
                e = Entry(idx, elm_in_row, 0, 1 if idx == 0 or idx == numRows-1 else 2)
                fill_arr.append( [ e ] )
            else:
                e = Entry(idx, elm_in_row, 1, 2)
                fill_arr[ elm_in_row - idx ].append(e)


        #print("fill_arr", fill_arr)
        ret = ""
        line = [' '] * len(s)

        for val in fill_arr:


            #print("line!")
            max_out = 0

            for e in val:

                out_offset = e.offset_output
                in_offset = e.offset_input
                jump_input = e.jump_input

                while in_offset < len(s):
                    max_out = max(max_out, out_offset)

                    line[out_offset] = s[in_offset]

                    out_offset += e.jump_output
                    in_offset +=  jump_input

                #print(line[0 : (max_out+1)])

            ret = ret + "".join(line[0 : (max_out+1)])

        #print("res: ", ret)
        return ret


