#Solution #1:
class Solution(object):
  def shortestDistance(self, words, word1, word2):
    """
    input: string[] words, string word1, string word2
    return: int
    """
    # write your solution here
    size = len(words)
    index1, index2 = size, size
    ans = size

    for i in range(size):
      if words[i] == word1:
        index1 = i
        ans = min(ans, abs(index1 - index2))
      elif words[i] == word2:
        index2 = i
        ans = min(ans, abs(index1 - index2))
    return ans
    
  # Solution #2:
  class Solution(object):
  def shortestDistance(self, words, word1, word2):
    """
    input: string[] words, string word1, string word2
    return: int
    """
    # write your solution here
    index1 = [i for i in range(len(words)) if words[i] == word1]
    index2 = [i for i in range(len(words)) if words[i] == word2]
    min_dis = float('inf')
    for i in index1:
      for j in index2:
        if abs(i-j) < min_dis:
          min_dis = abs(i - j)
    return min_dis
