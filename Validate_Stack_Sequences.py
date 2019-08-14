class Solution(object):
  def validateStackSequences(self, pushed, popped):
    """
    input: int[] pushed, int[] popped
    return: boolean
    """
    # write your solution here
    s, consume_next = [], 0
    for item in popped:
      while (not s or s[-1] != item) and consume_next < len(pushed):
        s.append(pushed[consume_next])
        consume_next += 1
      if s[-1] == item:
        s.pop()
      else:
        break
    return not s
