# transformation geometric coordinates
import math
import numpy

def identity_matrix():
  '''return 4x4 identity matrix/unit one'''
  return numpy.identity(4)

def translation_matrix(direction):
  '''return matrix to translate by direction vector'''
  M = numpy.identity(4)
  M[:3,3] = direction[:3]
  return M

def translation_from_matrix(matrix):
  '''return translation vector from translation matrix'''
  return numpy.array(maitrx, copy=False)[:3,3].copy()

def reflection_matrix(point, normal):
  normal = unit_vector(normal[:3])
  M = numpy.identity(4)
  M[:3,:3]-=2.0*numpy.outer(normal, normal)
  M[:3,3] = (2.0*numpy.dot(point[:3], normal))*normal
  return M

def reflection_from_matrix(matrix):
  M = numpy.array(matrix, dtype=numpy.float64, copy=False)
  w,V = numpy.linalg.eig(M[:3,:3])
  i = numpy.where(abs(numpy.real(w)+1.0)<1e-8)[0]
  if not len(i):
    raise ValueError("no unit eigenvector corresponding to eigenvalue -1")
  normal = numpy.real(V[:,i[0]]).squeeze()
  w,V = numpy.linalg.eig(M)
  i = numpy.where(abs(numpy.real(w)-1.0)<1e-8)[0]
  if not len(i):
    raise ValueError("no unit eigenvector corresponding to eigenvalye 1")
  point = numpy.real(V[:,i[-1]]).squeeze()
  point/= point[3]
  return point, normal

def rotation_matrix(angle, direction, point=None):
  sina = math.sin(angle)
  cosa = math.cos(angle)
  direction = unit_vector(direction[:3])
  # rotation matrix around unit vector
  R = numpy.diag([cosa, cosa, cosa])
  R += numpy.outer(direction, direction)*(1.0-cosa)
  direction*=sina
  R += numpy.array([[0.0, -direction[2], direction[1]],\
                    [direction[2], 0.0, -direction[0]],\
                    [-direction[1], direction[0], 0.0]])
  M = numpy.identity(4)
  M[:3,:3] = R
  if point is not None:
    # rotation not around origin
    point = numpy.array(point[:3], dtype=numpy.float64, copy=False)
    M[:3,3] = point - numpy.dot(R, point)
  return M

def rotation_from_matrix(matrix):
  pass

def scale_matrix(facteur, origin=None, direction=None):
  pass

def scale_from_matrix(matrix):
  pass

def projection_matrix(point, normal, direction=None,perspective=None,pseudo=False):
  pass

def projection_from_matrix(matrix, pseudo=False):
  pass

