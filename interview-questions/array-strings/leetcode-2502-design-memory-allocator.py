# 2502. Design Memory Allocator
# Medium
#
#    You are given an integer n representing the size of a 0-indexed memory array. All memory units are initially free.
#
#    You have a memory allocator with the following functionalities:
#
#        Allocate a block of size consecutive free memory units and assign it the id mID.
#        Free all memory units with the given id mID.
#
#    Note that:
#
#        Multiple blocks can be allocated to the same mID.
#        You should free all the memory units with mID, even if they were allocated in different blocks.
#
#    Implement the Allocator class:
#
#        Allocator(int n) Initializes an Allocator object with a memory array of size n.
#        int allocate(int size, int mID) Find the leftmost block of size consecutive free memory units and allocate it with the id mID. Return the block's first index. If such a block does not exist, return -1.
#        int free(int mID) Free all memory units with the id mID. Return the number of memory units you have freed.
#
#
#
#    Example 1:
#
#    Input
#    ["Allocator", "allocate", "allocate", "allocate", "free", "allocate", "allocate", "allocate", "free", "allocate", "free"]
#    [[10], [1, 1], [1, 2], [1, 3], [2], [3, 4], [1, 1], [1, 1], [1], [10, 2], [7]]
#    Output
#    [null, 0, 1, 2, 1, 3, 1, 6, 3, -1, 0]
#
#    Explanation
#    Allocator loc = new Allocator(10); // Initialize a memory array of size 10. All memory units are initially free.
#    loc.allocate(1, 1); // The leftmost block's first index is 0. The memory array becomes [1,_,_,_,_,_,_,_,_,_]. We return 0.
#    loc.allocate(1, 2); // The leftmost block's first index is 1. The memory array becomes [1,2,_,_,_,_,_,_,_,_]. We return 1.
#    loc.allocate(1, 3); // The leftmost block's first index is 2. The memory array becomes [1,2,3,_,_,_,_,_,_,_]. We return 2.
#    loc.free(2); // Free all memory units with mID 2. The memory array becomes [1,_, 3,_,_,_,_,_,_,_]. We return 1 since there is only 1 unit with mID 2.
#    loc.allocate(3, 4); // The leftmost block's first index is 3. The memory array becomes [1,_,3,4,4,4,_,_,_,_]. We return 3.
#    loc.allocate(1, 1); // The leftmost block's first index is 1. The memory array becomes [1,1,3,4,4,4,_,_,_,_]. We return 1.
#    loc.allocate(1, 1); // The leftmost block's first index is 6. The memory array becomes [1,1,3,4,4,4,1,_,_,_]. We return 6.
#    loc.free(1); // Free all memory units with mID 1. The memory array becomes [_,_,3,4,4,4,_,_,_,_]. We return 3 since there are 3 units with mID 1.
#    loc.allocate(10, 2); // We can not find any free block with 10 consecutive free memory units, so we return -1.
#    loc.free(7); // Free all memory units with mID 7. The memory array remains the same since there is no memory unit with mID 7. We return 0.
#
#
#
#    Constraints:
#
#        1 <= n, size, mID <= 1000
#        At most 1000 calls will be made to allocate and free.
#
#


class Entry:
    def __init__(self, offset, size, mid):
        self.offset = offset
        self.size = size
        self.mid = mid

    def __repr__(self):
        return f"(at={self.offset} sz={self.size} id={self.mid})"

class Allocator:

    def __init__(self, n: int):
        self.arena = [0] * n
        self.free_list = [Entry(0, n, -1,)]
        self.mid_to_mem={}


    def allocate(self, size: int, mID: int) -> int:
        for idx in range(0, len(self.free_list)):
            elm = self.free_list[idx]
            if elm.size >= size:
                alloc = Entry(elm.offset, size, mID)
                if mID not in self.mid_to_mem:
                    self.mid_to_mem[mID] = [ alloc ]
                else:
                    self.mid_to_mem[mID].append(alloc)

                elm.offset += size
                elm.size -= size

                if elm.size == 0:
                    self.free_list.pop(idx)

                #Allocator.validate(self.free_list)
                return alloc.offset

        return -1

    def free(self, mID: int) -> int:
        if mID in self.mid_to_mem:
            #to_free = len(self.mid_to_mem[mID])

            flist = self.mid_to_mem[mID]
            to_free = reduce(lambda a, b : a + b.size, flist, 0)
            self.mid_to_mem[mID] = []

            flist.sort(key = lambda elm : elm.offset)
            #print(f"to free {flist}")
            Allocator.free_all(flist, self.free_list)

            #Allocator.validate(self.free_list)
            return to_free

        return 0

    def free_all(flist, free_list):

        idx = 0
        while idx < len(flist):
            if idx + 1 == len(flist):
                break
            if flist[idx].offset + flist[idx].size == flist[idx+1].offset:
                flist[idx].size += flist[idx+1].size
                del flist[idx+1]
            else:
                idx += 1

        #print(f"before: {free_list}")



        flist_idx = 0
        if flist_idx >= len(flist):
            return
        e = flist[flist_idx]

        idx = 0
        prev = -1
        while idx < len(free_list):

            eat = e.offset + e.size
            if eat == free_list[idx].offset:

                while True:
                    free_list[idx].offset -= e.size
                    free_list[idx].size += e.size

                    if idx - 1 < 0:
                        break
                    e = free_list[idx-1]
                    if free_list[idx].offset != e.offset:
                        break
                    del free_list[idx-1]
                    idx -= 1

                flist_idx += 1
                if flist_idx >= len(flist):
                    return
                e = flist[flist_idx]
            elif free_list[idx].offset + free_list[idx].size == e.offset:
                while True:
                    free_list[idx].size += e.size
                    if idx + 1 == len(free_list):
                        break
                    e = free_list[idx+1]
                    if free_list[idx].offset + free_list[idx].size != e.offset:
                        break
                    del free_list[idx+1]

                flist_idx += 1
                if flist_idx >= len(flist):
                    return
                e = flist[flist_idx]



            elif eat < free_list[idx].offset:
                free_list.insert(idx, e)
                flist_idx += 1
                if flist_idx >= len(flist):
                    return
                e = flist[flist_idx]
                continue

            idx += 1

        if flist_idx < len(flist):
            free_list.extend(flist[flist_idx:])

    def validate(free_list):
        prev = -1
        for e in free_list:
            if prev >= e.offset:
                print(free_list)
                assert False

            assert e.offset >= 0
            assert e.size >= 0
            prev = e.offset + e.size




# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)
