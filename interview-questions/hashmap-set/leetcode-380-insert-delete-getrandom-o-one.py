# 380. Insert Delete GetRandom O(1) 
# Medium
#
#    Implement the RandomizedSet class:
#
#        RandomizedSet() Initializes the RandomizedSet object.
#        bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
#        bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
#        int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
#
#    You must implement the functions of the class such that each function works in average O(1) time complexity.
#
#

#
#    # Intuition
#
#    - ```getRandom``` needs to access a list/array of all values, however we also need to remove an entry at $$O(1)$$.
#
#    The solution is to maintain a list of freed enries, within the array of all values. If the free list is not empty, then insertion will reuse an entry from the free list.
#
#    The datastructure:
#    ```self.entries``` - the list of all entries, is a tuple, either
#    - (RandomizedSet.USED_ENTRY, value) - in this case the entry is in use, and the value is that of an inserted value.
#    - (RandomizedSet.FREE_ENTRY, next_idx) - in this case the entry is not in use, the next_idx  value points to the index of the next free entry.
#    ```self.map_to_link``` maps the entry value to the slot index in ```self.entries``` (this is needed for removal)
#
#    ```RandomizedSet.insert``` first inserts an entry into ```self.entries```, if the free list is not empty, then an empty entry slot will be reused.
#
#    ```RandomizedSet.remove``` finds the index of the entries slot in ```self.map_to_link```, moves an allocated slot in ```self.entries``` to the free list, also deletes the map entry.
#
#    ```RandomSet.getRandom``` gets a random index in ```self.entries```, if the entry is allocated then return its value. 
#
#

import random


class RandomizedSet:
    
    USED_ENTRY = 0
    FREE_ENTRY = 1

    def __init__(self):
        self.map_to_link = {}
        self.entries = []
        self.free_list = -1

    def insert(self, val: int) -> bool:
        #print(f"insert {val}")

        if val in self.map_to_link:
            return False

        new_link = (RandomizedSet.USED_ENTRY, val)    
        if self.free_list == -1:
            self.entries.append( new_link )
            self.map_to_link[val] = len(self.entries) - 1
        else:
            idx = self.free_list
            self.free_list = self.entries[idx][1]

            self.entries[idx] = new_link
            self.map_to_link[val] = idx
            
        return True

    
    def remove(self, val: int) -> bool:
        #print(f"remove {val}")

        if val not in self.map_to_link:
            return False

        free_link = (RandomizedSet.FREE_ENTRY, self.free_list)
        idx = self.map_to_link[val]
        self.entries[idx] = free_link
        self.free_list = idx
        
        del self.map_to_link[val]
        
        return True

    def getRandom(self) -> int:
        while True:
            idx = random.randint(0, len(self.entries)-1)
            entry = self.entries[idx]
            if entry[0] == RandomizedSet.USED_ENTRY:
                return entry[1]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

