#Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
#
#Implement the LRUCache class:
#
#    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
#    int get(int key) Return the value of the key if the key exists, otherwise return -1.
#    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
#
#The functions get and put must each run in O(1) average time complexity.
#
# 
#
#Example 1:
#
#Input
#["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
#[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
#Output
#[null, null, null, 1, null, -1, null, -1, 3, 4]
#
#Explanation
#LRUCache lRUCache = new LRUCache(2);
#lRUCache.put(1, 1); // cache is {1=1}
#lRUCache.put(2, 2); // cache is {1=1, 2=2}
#lRUCache.get(1);    // return 1
#lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
#lRUCache.get(2);    // returns -1 (not found)
#lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
#lRUCache.get(1);    // return -1 (not found)
#lRUCache.get(3);    // return 3
#lRUCache.get(4);    // return 4
#
# 
#
#Constraints:
#
#    1 <= capacity <= 3000
#    0 <= key <= 104
#    0 <= value <= 105
#    At most 2 * 105 calls will be made to get and put.
#


class Link:
    def __init__(self, key, value, left = None, right = None):
        self.key = key
        self.value = value
        self.left = self.right = self

    def unlink(self):
        oldLeft = self.left
        self.left.right = self.right
        self.right.left = oldLeft

    def insert(self, newLink):
        oldRight = self.right
        self.right = newLink

        newLink.left = self
        newLink.right = oldRight

        oldRight.left = newLink



class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.imp = {}
        self.top = Link(-1, -1)


    def get(self, key: int) -> int:
        val = self.imp.get(key)
        if val:
            val.unlink()
            self.top.insert(val)
            return val.value

        return -1

    def put(self, key: int, value: int) -> None:
        val = self.imp.get(key)
        if val:
            val.value = value
            val.unlink()
            self.top.insert(val)
            return
            
        newLink = Link(key, value)
        self.top.insert(newLink)
        
        self.imp[key] = newLink

        if len(self.imp) > self.capacity:
            val = self.top.left.key
            self.top.left.unlink()
            self.imp.pop(val) 

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


