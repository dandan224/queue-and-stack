# not easy understand
def solution():
    if len(nums) == 0:
      return 0
    l, r, k = 0, 0, 1
    zero = 0
    ret = 1
    for r in range(0, len(nums)):
       if nums[r] == 0:
          zero += 1
          
       while zero > k:
         if nums[l] == 0:
           zero -= 1
         l += 1
       ret = max(ret, r - l + 1)
    return ret
