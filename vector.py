from math import sqrt, acos, pi
from decimal import Decimal, getcontext
#import numpy as np

getcontext().prec = 30

class Vector(object):
    
    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalise the zero vector'
    
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)
        
    def minus(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)
        
    def times_scalar(self, c):
        new_coordinates = [Decimal(c)*x for x in self.coordinates]
        return Vector(new_coordinates)
        
    def magnitude(self):
        coord_squared = [Decimal(x)**2 for x in self.coordinates]
        return Decimal(sqrt(sum(coord_squared)))
        
    def normalised(self):
        try:
            magn = self.magnitude()
            return self.times_scalar(Decimal('1.0')/magn)
        except ZeroDivisionError:
            raise Exception('Cannot normalise the zero vector')
    
    def dotproduct(self, v):
        return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])
    
    def angle_calc(self, v, in_degrees=False):
        try:
            u1 = self.normalised()
            u2 = v.normalised()
            angle_rad = acos(u1.dotproduct(u2))
            
            if in_degrees:
                degrees_in_rad = 180./ pi
                return angle_rad * degrees_in_rad
            else:
                return angle_rad
                
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute with zero vector')
            else:
                raise e
    
    def is_orthogonal(self, v, tolerance=1e-10):
        return abs(self.dotproduct(v)) < tolerance
        
    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance

    def is_parallel(self, v):
        return (self.is_zero() or
                v.is_zero() or
                self.angle_calc(v) == 0 or
                self.angle_calc(v) == pi)
        
    def comp_parallel(self, basis):
        try:
            ub = basis.normalise()
            vmag = self.dotproduct(ub)
            return ub.times_scalar(vmag)
            
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONET_MSG)
            else:
                raise e

    def comp_ortho(self, basis):
        try:
            projection = self.comp_parallel(basis)
            return self.minus(projection)
            
        except Exception as e:
            if e == self.NO_UNIQUE_PARALLEL_COMPONET_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONET_MSG)
            else:
                raise e

#==============================================================================
#      def crossproduct(self, v):
#          try:
#              x1, x2, x3 = self.coordinates
#              y1, y2, y3 = v.coordinates
#              new_coords = [x2*y3-y2*x3,
#                            -(x1*y3-y1*x3),
#                              x1*y2-y1*x2]
#              return Vector(new_coords)
#          except ValueError as e:
#              msg = str(e)
#              if msg == 'need more than 2 values to unpack':
#                  self_embeded_in_R3 = Vector(self.coordinates+('0', ))
#                  v_embedded_in_R3 = Vector(v.coordinates+ ('0',))
#                  return self_embeded_in_R3.crossproduct(v_embedded_in_R3)
#              elif(msg=='too many values to unpack' or
#                   msg=='need more than 1 value to unpack):
#                  raise Exception(self.ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG)
#              else:
#                  raise e
#==============================================================================

                 
                 
            
        