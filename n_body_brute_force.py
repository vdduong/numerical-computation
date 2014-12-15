# N body simulation using brute force algorithm

# X and Y for (x,y) space coordinates of the bodies
# Vx Vy for the components of the velocity vectors of the bodies
# M for the masses of the bodies
# F for the net forces acting on the bodies

for time xrange(time_max):
  for i in xrange(N_bodies):
    F[i] = 0
    for j in xrange(N_bodies):
      if j!=i:
        F[i] +=f(i,j)
  for i in xrange(N_bodies):
    recalculate_position(i)


  
