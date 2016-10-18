'''
Problem: Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Approach : Least Recently Used cache implemented using OrderedDict
'''
from collections import OrderedDict

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity 
        self.items = OrderedDict()
    def get(self, key):
        """
        :rtype: int
        """
        if self.items.has_key(key):
            k = self.items.pop(key)
            self.items[key]=k
            return k
        else:
            return -1
    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if self.capacity != 0 or self.items.has_key(key):
            if not self.items.has_key(key):
                self.capacity = self.capacity-1
            self.get(key)
            self.items[key]=value
            #print ("setting item %d %d capacity:%d"%(key, value, self.capacity))
            #print (self.items)
        else:
            k,v = self.items.popitem(last=False)
            #print ("popping item %d %d capacity:%d"%(k, v, self.capacity))
            #print (self.items)
            self.items[key]=value
            #print ("After: {!r}".format(self.items))

s = LRUCache(2)
s.set(2,1)
s.set(2,2)
assert s.get(2)==2
s.set(1,1)
s.set(4,1)
assert s.get(2)==-1
