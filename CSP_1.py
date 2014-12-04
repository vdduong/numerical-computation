# CSP
# search a solution by exploring a search tree.
def solve():
  if solved():
    return True
  i = selectVar()
  dom = var[i] # save domain
  for v in dom:
    if  consistant1(i,v):
      var[i] = [v]
      if solve():
        return True
  var[i] = dom # .. restore domain
  return False # backtrack

