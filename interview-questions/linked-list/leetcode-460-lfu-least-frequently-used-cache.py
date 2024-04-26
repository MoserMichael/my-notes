# 460. LFU Cache
# Hard
#
#    Design and implement a data structure for a Least Frequently Used (LFU) cache.
#
#    Implement the LFUCache class:
#
#        LFUCache(int capacity) Initializes the object with the capacity of the data structure.
#        int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
#        void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
#
#    To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.
#
#    When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.
#
#    The functions get and put must each run in O(1) average time complexity.
#
#
#
#    Example 1:
#
#    Input
#    ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
#    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
#    Output
#    [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
#
#    Explanation
#    // cnt(x) = the use counter for key x
#    // cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
#    LFUCache lfu = new LFUCache(2);
#    lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
#    lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
#    lfu.get(1);      // return 1
#                     // cache=[1,2], cnt(2)=1, cnt(1)=2
#    lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
#                     // cache=[3,1], cnt(3)=1, cnt(1)=2
#    lfu.get(2);      // return -1 (not found)
#    lfu.get(3);      // return 3
#                     // cache=[3,1], cnt(3)=2, cnt(1)=2
#    lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
#                     // cache=[4,3], cnt(4)=1, cnt(3)=2
#    lfu.get(1);      // return -1 (not found)
#    lfu.get(3);      // return 3
#                     // cache=[3,4], cnt(4)=1, cnt(3)=3
#    lfu.get(4);      // return 4
#                     // cache=[4,3], cnt(4)=2, cnt(3)=3
#
#
#
#    Constraints:
#
#        1 <= capacity <= 104
#        0 <= key <= 105
#        0 <= value <= 109
#        At most 2 * 105 calls will be made to get and put.
#


#    Solution has one map from key to Entry object. The Entry object has the following fields
#
#    class Entry
#        + key - key value
#        + data - the value of the mapping
#        + usage_count - usage count of this entry
#        + next - next entry in double linked list of entries sorted by usage count
#        + prev  - previous entry in double linked list of entries sorted by usage count
#        + run_data - an object that keeps the first and last element of entries that have the same usage_count as this one
#
#    The ```Entry``` elements are kept in a double linked list that is sorted by ```usage_count```.
#
#    Now the double linked list must be reordered upon incrementing this counter, this must happen in ```O(1)``` time. For this purpose each ```Entry``` object with the same ```usage_count``` value is pointing to a ```RunData``` object - this object keeps track of the first and last element of entries with the same ```usage_count``` value. This reordering will unlink the ```Entry``` object from its current position and insert it again right after the end of the last element specified by ```RunData```, in this case check if it is part of existing run that covers the incremented ```usage_count``` value, or create a new ```RunData``` object.
#
#    Eviction of a "old" entry removes the last element of the first ```RunData``` - that is the entry that was least recently used.
#
#    class RunData
#        + first - first ```Entry``` for given ```usage_count``` value
#        + last  - last  ```Entry``` for given ```usage_count``` value
#


class Entry:
    def __init__(self, key=None, data=None):
        self.next=self.prev=self
        self.key = key
        self.data = data
        self.usage_count = 1
        self.run_data = None

    def empty(self):
        return self.next == self.prev

    def unlink(self):
        self.next.prev = self.prev
        self.prev.next = self.next

    def insert(self, data):
        dnext = self.next
        self.next = data
        data.next = dnext
        dnext.prev = data
        data.prev = self

    def __str__(self):
        return f"usage={self.usage_count} key={self.key} data={self.data} /{str(self.run_data)}/"

class RunData:
    def __init__(self,first, last):
        self.first, self.last = first, last

    def set_first(self, item):
        self.first = item

    def remove(self, item):      
        if self.last == item:
            self.last = self.last.prev
            return False
        elif self.first == item:
            self.first = self.first.next
        
        return True

    def remove_last(self):
        ret = self.last
        self.last = self.last.prev
        ret.unlink()

        return ret

    def __str__(self):
        return f"{self.first.key}-{self.last.key}"

class LFUCache:

    def __init__(self, capacity: int):
        #print(f"capacity {capacity}")
        self.capacity = capacity
        self.lookup = {} 

        self.head = Entry()
        self.head.usage_count = None      

    def get(self, key: int) -> int:
        val_entry = self.lookup.get(key)
        if val_entry:
            self._update_count(val_entry)
            return val_entry.data
        return -1

    def _update_count(self, val_entry):
        last_run = val_entry.run_data.last
        next_after_last = last_run.next

        if val_entry.run_data.remove(val_entry):
            val_entry.unlink()
            last_run.insert(val_entry)   
        
        val_entry.usage_count += 1
        
        if next_after_last.usage_count  == val_entry.usage_count:
            next_after_last.run_data.set_first(val_entry)
            val_entry.run_data = next_after_last.run_data
        else:
            val_entry.run_data = RunData(val_entry, val_entry)

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            val_entry = self.lookup[key]
            val_entry.data = value
            
            self._update_count(val_entry)
        else:
            if len(self.lookup) == self.capacity:
                self._remove_item()

            val_entry = Entry(key, value)
            self.lookup[key] = val_entry
            
            self._insert_new(val_entry)

    def _insert_new(self, val_entry):
        old_first = self.head.next
        self.head.insert(val_entry)

        if old_first.usage_count == 1:
            # add to existing
            val_entry.run_data = old_first.run_data 
            val_entry.run_data.set_first(val_entry)
            return
        val_entry.run_data = RunData(val_entry, val_entry)


    def _remove_item(self):
        first = self.head.next
        to_remove = first.run_data.last
        del self.lookup[ to_remove.key ]
        return to_remove.run_data.remove_last()

    def show_counts(self):
        print(self.lookup)
        c = self.head.next
        prev_usage_count = 0
        cnt = 0
        while c != self.head:
            print(f"->{str(c)}")
            assert c.usage_count >= prev_usage_count
            assert c.key in self.lookup
            assert self.lookup[c.key].data == c.data
            prev_usage_count = c.usage_count
            c = c.next
            cnt += 1

        assert cnt == len(self.lookup)    



