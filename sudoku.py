# sudoku 9x9 algorithm
# algorithm: go through the table, test value from 1-9 for the current square.
# if no value accepted then back a square (initially empty) and try next value.
# noting the squares from 1 to 81 by going from left to right, high to low.

import numpy as np
import time

matsudoku = np.array([0, 8, 0, 1, 0, 7, 0, 6, 0, \
                      0, 0, 4, 0, 0, 0, 1, 0, 0, \
                      0, 5, 0, 6, 0, 9, 0, 2, 0, \
                      0, 1, 3, 0, 0, 0, 2, 4, 0, \
                      2, 0, 0, 0, 0, 0, 0, 0, 6, \
                      0, 7, 5, 0, 0, 0, 3, 1, 0, \
                      0, 9, 0, 8, 0, 5, 0, 3, 0, \
                      0, 0, 1, 0, 0, 0, 7, 0, 0, \
                      0, 3, 0, 4, 0, 2, 0, 9, 0])

initsudoku = matsudoku.copy()

# filling a number into a square
# z = Possible_Case(k,n)
# k = the square number
# n = the tested number
# z: if z = n if n can be placed in the square k and z=0 otherwise
def Possible_Case(k,n):
  r = k%9
  b = int(k/9)
  
  if r==0:
    c = 9
    l=b
  else:
    c=r
    l=b+1
  
  # column treatment
  ci=range(c,c+72+1,9)
  for p in ci:
    if matsudoku[p-1]==n:
      return 0
  
  # line treatment
  q=9*(l-1) + 1
  li=range(q,q+8+1,1)
  for s in li:
    if matsudoku[s-1]==n:
      return 0
  
  # block treatment
  t=int(k/27)
  f=k%27
  
  if f==0: lb=t-1
  else: lb=t
  
  v=c%3
  w=int(c/3)
  
  if v==0: cb=w-1
  else: cb=w
  
  # the square number N1 of the block
  numb=3*cb+1 +27*lb
  bj=range(0,2+1,1)
  be=range(0,2+1,1)
  for j in bj:
    for e in be:
      i=numb+9*j+e
      if matsudoku[i-1]==n:
        return 0
  return n

def Reculer_Case(k):
  temp2=k-1
  while initsudoku[temp2-1]!=0:
    temps2 = temps2-1
  return temps2

def Avancer_Case(k):
  if k==81:
    return 82
  temp = k+1
  while initsudoku[temp-1]!=0:
    temp+=1
  return temp

#----------------
dtime=time.time()
nsudo=Avancer_Case(0)
firstn = nsudo

while nsudo<82:
  valeurn=matsudoku[nsudo-1]
  if valeurn<9:
    sn=0
    lt=range(valeurn+1,9+1,1)
    for test in lt:
      rn=Possible_Case(nsudo,test)
      if rn!=0:
        matsudoku[nsudo-1]=rn
        sn=1
        nsudo=Avancer_Case(nsudo)
        break
    if sn==0:
      matsudoku[nsudo-1]=0
      nsudo=Reculer_Case(nsudo)
  elif nsudo==firstn:
    break
  else:
    matsudoku[nsudo-1]=0
    nsudo=Reculer_Case(nsudo)

if nsudo!=firstn:
  ftime=time.time()
  print("Initial grid:")
  print(initsudoku.reshape(9,9))
  print("found solution:")
  print(matsudoku.reshape(9,9))
  print("Execution time: "+str(ftime-dtime)+ " seconds")
else:
  print("No solution found")
