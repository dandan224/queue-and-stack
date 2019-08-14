class Solution(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.mins = []
        
    def push(self, x):
        """
        input : int x
        return : 
        """
        self.items.append(x)
        if not self.mins or self.mins[-1] >= x:
          self.mins.append(x)
          
        
    def pop(self):
        """
        return : int
        """
        if not self.items:
          return -1
        item = self.items.pop()
        if item == self.mins[-1]:
          self.mins.pop()
        return item  
        
    def top(self):
        """
        return : int
        """
        return self.items[-1] if self.items else -1
        
    def min(self):
        """
        return : int
        """
        return self.mins[-1] if self.mins else -1
