class Solution(object):
  def maxWindows(self, array, k):
    """
    input: int[] array, int k
    return: Integer[]
    """
    # write your solution here
    from collections import deque
    q = deque()
    res = []
    i = 0
    
    while i < k:
      q.append(array[i])
      i += 1
    num = max(q)
    res.append(num)
      

    while i>=k and i < len(array):
      q.append(array[i])
      q.popleft()
      num = max(q)
      res.append(num)
      i += 1
    return res





