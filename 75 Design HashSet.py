# Design a HashSet without using any built-in hash table libraries.

# Implement MyHashSet class:

# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or not.
# void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
 

# Example 1:

# Input
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# Output
# [null, null, null, true, false, null, true, null, false]

# Explanation
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // return True
# myHashSet.contains(3); // return False, (not found)
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // return True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // return False, (already removed)
 

# Constraints:

# 0 <= key <= 106
# At most 104 calls will be made to add, remove, and contains.

class MyHashSet:

    def __init__(self):
        self.size = 0
        self.capacity = 2
        self.map = [None] * self.capacity
        self.DELETED = "<deleted>"  # special marker for removed items

    def hash(self, key):
        return key % self.capacity

    def add(self, key):
        index = self.hash(key)

        while True:
            if self.map[index] is None or self.map[index] == self.DELETED:
                self.map[index] = key
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.rehash()
                return
            elif self.map[index] == key:  # already exists
                return
            index = (index + 1) % self.capacity

    def remove(self, key):
        index = self.hash(key)

        while self.map[index] is not None:
            if self.map[index] == key:
                self.map[index] = self.DELETED
                self.size -= 1
                return
            index = (index + 1) % self.capacity

    def contains(self, key):
        index = self.hash(key)

        while self.map[index] is not None:
            if self.map[index] == key:
                return True
            index = (index + 1) % self.capacity
        return False

    def rehash(self):
        old_map = self.map
        self.capacity *= 2
        self.map = [None] * self.capacity
        self.size = 0
        for item in old_map:
            if item is not None and item != self.DELETED:
                self.add(item)
