# by using map
class Solution(object):
  def containsNearbyDuplicate(self, nums, k):
    """
    input: int[] nums, int k
    return: boolean
    """
    # write your solution here
    map = {}
    for i in range(len(nums)):
      if nums[i] in map and abs(map[nums[i]] - i ) <= k:
          return True
      else:
        map[nums[i]] = i
    return False
    
    # by using set
    window = set([])
    for i in xrange(len(nums)):
      if i > k:
        window.discard(nums[i-k-1])
      if nums[i] in window:
        return True
      else:
        window.add(nums[i])
    return False
