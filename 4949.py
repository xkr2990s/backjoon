while True:
  stack = []
  str = input()
  answer = 'yes'
  if str=='.':
    break
  else:
    for char in str:
      if char=='(' or char=='[':
        stack.append(char)
      elif char==')':
        if not len(stack):
          answer = 'no'
          break
        else:
          if stack.pop(-1)!='(':
            answer = 'no'
            break
      elif char==']':
        if not len(stack):
          answer = 'no'
          break
        else:
          if stack.pop(-1)!='[':
            answer = 'no'
            break
      else: continue
  if len(stack):
    answer = 'no'
  print(answer)