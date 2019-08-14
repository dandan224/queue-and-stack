class Solution(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self._size = k
        self._items = []
        

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
          return False
        if self._size == 0:
          self._items.append(value)
        else:
          self._items.insert(0, value)
        #self._size += 1
        # how to return True
        return True

        

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
          return False
        self._items.append(value)
        #self._size += 1
        return True
        

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
          return False
        
        del self._items[0]
        #self._size -= 1
        return True
        

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
          return False
        
        del self._items[-1]
        #self._size -= 1
        return True
        

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.isEmpty():
          return -1
        return self._items[0]


        

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.isEmpty():
          return -1
        return self._items[-1]
        

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        if self._size == 0:
          return True
        return False

        

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        
        if len(self._items) >= self._size:
          return True
        return False
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
