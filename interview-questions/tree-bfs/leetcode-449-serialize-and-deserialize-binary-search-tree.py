# 449. Serialize and Deserialize BST
# Medium
#
#    Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
#
#    Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.
#
#    The encoded string should be as compact as possible.
#
#     
#
#    Example 1:
#
#    Input: root = [2,1,3]
#    Output: [2,1,3]
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
#        0 <= Node.val <= 104
#        The input tree is guaranteed to be a binary search tree.
#
 
import io

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        buf = io.StringIO()
        Codec.ser(buf, root)
        rt = buf.getvalue()
        return rt
    
    def ser(buf, root):
        if not root:
            return
        buf.write(str(root.val))
        buf.write(" ")
        Codec.ser(buf, root.left)
        Codec.ser(buf, root.right)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        stk = []
        self.data=data
        self.pos = 0

        root = None

        while True:
            val = self.getToken()
            if val is None:
                break
            newNode = TreeNode(val)

            if not root:
                stk.append(newNode)
                root = newNode
            else:
                if val > stk[-1].val:        
                    pos = len(stk)-2
                    insPoint = len(stk)-1
                    while pos >= 0:
                        if stk[pos].val < val:
                            if stk[pos].right is None:
                                insPoint = pos                            
                        pos -= 1
                    
                    stk = stk[0:(insPoint+1)]
                    stk[-1].right = newNode
                    stk.append(newNode)
                    
                else:
                    stk[-1].left = newNode
                    stk.append(newNode)
        return root

    def getToken(self):
        if self.pos >= len(self.data):
            return None
        next_pos = self.data.find(' ', self.pos)
        tk = self.data[self.pos:next_pos]
        self.pos = next_pos + 1
        return int(tk)

    def show_sexpr(node):
        buf = io.StringIO()
        Codec.make_sexpr(node, buf)
        print(buf.getvalue())
     
    def make_sexpr(node, buf):
        if not node:
            return
        buf.write("(")
        buf.write(str(node.val))

        Codec.make_sexpr(node.left, buf)
        Codec.make_sexpr(node.right, buf)
        buf.write(")") 
        


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
