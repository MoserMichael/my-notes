# 297. Serialize and Deserialize Binary Tree
# Hard
#
#    Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
#
#    Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
#
#    Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
#
#
#
#    Example 1:
#
#    Input: root = [1,2,3,null,null,4,5]
#    Output: [1,2,3,null,null,4,5]
#
#    Example 2:
#
#    Input: root = []
#    Output: []
#
#
#
#    Constraints:
#
#        The number of nodes in the tree is in the range [0, 104].
#        -1000 <= Node.val <= 1000
#

#
#    # Intuition
#    S-expr is a concise format for serialization, so lets go for it.
#
#    # Approach
#    use io.StringIO for managing the buffer.
#
#    # Complexity
#    - Time complexity:
#    $$O(n)$$ where n is the number of nodes in the tree
#
#    - Space complexity:
#    $$O(log(n))$$ provided that the tree is halfway balanaced, not a linked list, and we do count the stack space.
#

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import io

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        b = io.StringIO()
        Codec._serialize(b, root)
        ret = b.getvalue()
        #print(f"serializeL {ret}")
        return ret

    def _serialize(buf, root):
        if not root:
            buf.write(" #")
            return
        buf.write("(")
        buf.write(str(root.val))

        Codec._serialize(buf, root.left)
        Codec._serialize(buf, root.right)

        buf.write(")")

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        tree, _ = Codec._deser(data,0)
        return tree


    def _deser(buf, pos):
        pos = Codec.skipSpace(buf, pos)
        if pos > len(buf):
            print(f"end of input at {pos}")
            return None

        if buf[pos] == '#':
            return None, pos+1

        if buf[pos] == '(':
            num, pos = Codec.parseNum(buf, pos+1)

            tree = TreeNode(num)

            tree.left, pos = Codec._deser(buf, pos)

            tree.right, pos = Codec._deser(buf, pos)

            pos = Codec.skipSpace(buf, pos)
            if buf[pos] == ')':
                pos += 1
                return tree, pos

            print(f"Error at pos {pos}" )
            return None, pos

        print(f"expected ( character pos: {pos}")
        return None, pos


    def skipSpace(buf, pos):
        while pos < len(buf):
            if buf[pos] != ' ':
                break
            pos += 1
        return pos

    def parseNum(buf, pos):
        startPos = pos
        while pos < len(buf):
            if not buf[pos].isdigit() and not buf[pos] == '-':
                break
            pos += 1

        #print(f"num {buf[startPos:pos]} {startPos} {pos}")
        ret = int(buf[startPos:pos])
        return ret, pos

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

