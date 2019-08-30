# Solution #1:
class Solution(object):
  def longest(self, input):
    """
    input: string input
    return: int
    """
    # write your solution here
    maxL = 0
    hashS =dict()
    l = 0
    s = list(input)
    for r in range(0,len(s)):
      if s[r] not in hashS:
        hashS[s[r]] = 0
      hashS[s[r]] += 1
      while l < len(s) and hashS[s[r]] > 1:
        hashS[s[l]] -= 1
        l += 1

      maxL = max(maxL,r-l+1)
    return maxL
  
 # Solution #2:
 class Solution(object):
  def longest(self, input):
    """
    input: string input
    return: int
    """
    # write your solution here
    dic = {}
    longest, h = 0, 0
    input = list(input)
    for i in range(len(input)):
      if input[i] in dic:
        h = max(h, dic[input[i]] + 1)
      
      dic[input[i]] = i
      longest = max(longest, i-h +1)
    return longest
