class Solution(object):
  def evalRPN(self, tokens):
    """
    input: string[] tokens
    return: int
    """
    # write your solution here
    import operator
    operands = []
    ops = {'+':operator.add, '-': operator.sub, '*':operator.mul, '/':operator.floordiv}
    for token in tokens:
      if token in ops:
        right, left = operands.pop(), operands.pop()
        operands.append(int(ops[token](left, right)))
      else:
        operands.append(int(token))
    return operands[0]
