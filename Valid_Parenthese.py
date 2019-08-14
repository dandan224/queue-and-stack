class Solution(object):
  def isValid(self, input):
    """
    input: string input
    return: boolean
    """
    # write your solution here
    leftbrackets = []
    brackets = {'(':')', '[':']','{':'}'}
    for i in input:
      if i in brackets:
        leftbrackets.append(i)
      elif not leftbrackets or brackets[leftbrackets[-1]] != i:
        return False
      else:
        leftbrackets.pop()
    return not leftbrackets
