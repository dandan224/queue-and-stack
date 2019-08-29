class Solution(object):
  def containsDuplicate(self, nums):
    """
    input: int[] nums
    return: boolean
    """
    # write your solution here
    # brute force time:O(n^2)
    if not nums or len(nums) == 1 :
      return False
    for i in range(len(nums)):
      for j in range(i+1,len(nums)):
        if nums[i] == nums[j]:
          return True
    return False
    
    # slution #2, sort the list, then compare the list, time: O(nlogn + n)
    if not nums or len(nums) == 1:
      return False
    nums.sort()
    for i in range(1, len(nums)):
      if nums[i] == nums[i - 1]:
        return True
    return False
    
    #solution#3: by using dictornary
    class Solution(object):
  def containsDuplicate(self, nums):
    """
    input: int[] nums
    return: boolean
    """
    # write your solution here
    map = {}
    for i in nums:
      if i in map:
        return True
      else:
        map[i] = 1
    return False
    
        
