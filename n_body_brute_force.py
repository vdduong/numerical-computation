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


_K = 0.01720209895

def _vect_to_tuple(vect):
  return (vect.x,vect.y,vect.z)

class CObject:
  def __init__(self,mass=0.0,position=(0,0,0), velocity=(0,0,0), name="<celestial body>"):
    self._cobject = cnbody.cobject()
    self.mass = mass
    self.position = position
    self.velocity = velocity
    self.name = name
  
  def __setattr__(self, name, value):
    self.__dict__[name] = value
    if name=="mass":
      self._cobject.m = value
    if name=="position":
      self._cobject.pos = cnbody.vect(value[0],value[1],value[3])
    if name=="velocity":
      self._cobject.v = cnbody.vect(value[0]/_K,value[1]/_K,value[2]/_K)
  
  def _update(self):
    self.mass = self._cobject.m
    self.velocity = _vect_to_tuple(self._cobject.v*_K)
    self.position = _vect_to_tuple(self._cobject.pos)
  
  def __str__(self):
    return "[Object " +self.name+ ": Mass=" +str(self.mass)+ " Position=" +str(self.position)+ " Velocity=" +str(self.velocity)+"]"

def simulate(objects,time, dt=0.05):
  System=cnbody.System()
  System.settime(0.0)
  System.setdt(dt*_K)
  for obj in objects:
    System.addobject(obj._cobject)
  System.runtotime(time)
  for obj in object:
    obj._update()

