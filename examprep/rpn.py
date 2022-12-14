def evaluate_rpn(expression):
  stack = []

  # split the expression into a list of values
  values = expression.split()

  # loop through the values
  for val in values:
    # if the value is an operator, pop the last two values from the stack, perform the operation, and push the result back to the stack
    if val in ['+', '-', '*', '/']:
      op2 = stack.pop()
      op1 = stack.pop()
      result = 0
      if val == '+':
        result = op1 + op2
      elif val == '-':
        result = op1 - op2
      elif val == '*':
        result = op1 * op2
      else:
        result = op1 / op2
      stack.append(result)
    # if the value is not an operator, it is a number, so just push it to the stack
    else:
      stack.append(int(val))

  # after looping through the entire expression, the result should be the only value in the stack
  return stack[0]

# test the function
print(evaluate_rpn('2 3 + 5 *'))  # should print 25
print(evaluate_rpn('1 2 + 3 4 * + 5 6 * +'))  # should print 45s