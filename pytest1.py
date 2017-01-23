# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
import numpy as np
import math
import decimal
import vector
import sys
import line


def unit_vector(v):
    vmag = np.linalg.norm(v)
    return (1/vmag*v)



    
    
#==============================================================================
# a = np.array([8.218, -9.341], float)
# b = np.array([-1.129, 2.111], float)
# print(a+b)
# c = np.array([7.119, 8.215], float)
# d = np.array([-8.223, 0.878], float)
# print(c-d)
# e = np.array([1.671, -1.012, -0.318], float)
# print(7.41*e)
#==============================================================================

#==============================================================================
# v21 = np.array([-0.221, 7.437])
# v22 = np.array([8.813, -1.331, -6.247])
# mag21 = np.linalg.norm(v21)
# print(mag21)
# mag22 = np.linalg.norm(v22)
# print(mag22)
# 
# v23 = np.array([5.581, -2.136])
# mag23 = np.linalg.norm(v23)
# uv23 = (1/mag23*v23)
# print(uv23)
# v24 = np.array([1.996, 3.108, -4.554])
# mag24 = np.linalg.norm(v24)
# uv24 = (1/mag24*v24)
# print(uv24)
#==============================================================================


#==============================================================================
# v31 = np.array([7.887, 4.138])
# w31 = np.array([-8.802, 6.776])
# dp31 = np.dot(v31, w31)
# print(dp31)
# 
# a31 = Vector(['7.887', '4.138'])
# b31 = Vector(['-8.802', '6.776'])
# print(a31.dotproduct(b31))
# 
# 
# v32 = np.array([-5.955, -4.904, -1.874])
# w32 = np.array([-4.496, -8.755, 7.103])
# dp32 = np.dot(v32, w32)
# print(dp32)
# 
# v33 = np.array([3.183, -7.627])
# w33 = np.array([-2.668, 5.319])
# dp33 = np.dot(v33, w33)
# angle33 = math.acos(dp33/((np.linalg.norm(v33))*(np.linalg.norm(w33))))
# print(angle33)
# 
# a33 = Vector(['3.183', '-7.627'])
# b33 = Vector(['-2.668', '5.319'])
# c33 = a33.angle_calc(b33)
# print(c33)
# 
# 
# v34 = np.array([7.35, 0.221, 5.188])
# w34 = np.array([2.751, 8.259, 3.985])
# dp34 = np.dot(v34, w34)
# angle34 = math.acos(dp34/((np.linalg.norm(v34))*(np.linalg.norm(w34))))
# print(math.degrees(angle34))
#==============================================================================

#==============================================================================
# v41 = np.array([-7.579, -7.88])
# w41 = np.array([22.737, 23.64])
# dp41 = np.dot(v41, w41) 
# angle41 = math.acos(dp41/((np.linalg.norm(v41))*(np.linalg.norm(w41))))
# print(math.degrees(angle41))
# 
# a41 = Vector([-7.579, -7.88])
# b41 = Vector([22.737, 23.64])
# print (a41.is_parallel(b41))
# 
# v42 = np.array([-2.029, 9.97, 4.172])
# w42 = np.array([-9.231, -6.639, -7.245])
# dp42 = np.dot(v42, w42)
# angle42 = math.acos(dp42/((np.linalg.norm(v42))*(np.linalg.norm(w42))))
# print(math.degrees(angle42))
# 
# v43 = np.array([-2.328, -7.284, -1.214])
# w43 = np.array([-1.821, 1.072, -2.94])
# dp43 = np.dot(v43, w43)
# angle43 = math.acos(dp43/((np.linalg.norm(v43))*(np.linalg.norm(w43))))
# print(math.degrees(angle43))
#==============================================================================

#==============================================================================
# v51 = np.array([3.039, 1.879])
# b51 = np.array([0.825, 2.036])
# ub51 = unit_vector(b51)
# v51_parral = np.dot(v51, ub51)*ub51
# print("blah   " + str(np.round_(v51_parral, 3)))
# 
# v52 = np.array([-9.88, -3.264, -8.159])
# b52 = np.array([-2.155, -9.353, -9.473])
# ub52 = unit_vector(b52)
# #print (ub52)
# #print (np.dot(v52, b52))
# v52_parral = np.dot(v52, ub52)*ub52
# v52_orth = v52 - v52_parral
# print (np.round_(v52_orth, 3))
# 
# v53 = np.array([3.009, -6.172, 3.692, -2.51])
# b53 = np.array([6.404, -9.144, 2.759, 8.718])
# ub53 = unit_vector(b53)
# v53_parral = np.dot(v53, ub53)*ub53
# v53_orth = v53 - v53_parral
# print (np.round_(v53_parral, 3))
# print (np.round_(v53_orth, 3))
#==============================================================================

#==============================================================================
# v61 = np.array([8.462, 7.893, -8.187])
# w61 = np.array([6.984, -5.975, 4.778])
# cp61 = np.cross(v61, w61)
# print(np.round_(cp61, 3))
# #print(np.dot(v61, cp61))
# #print(np.dot(w61, cp61))
# 
# v62 = np.array([-8.987, -9.838, 5.031])
# w62 = np.array([-4.268, -1.861, -8.866])
# cp2 = np.cross(v62, w62)
# area1=np.linalg.norm(cp2)
# print(area1)
# 
# v63 = np.array([1.5, 9.547, 3.691])
# w63 = np.array([-6.007, 0.124, 5.772])
# cp63 = np.cross(v63, w63)
# area63=0.5*np.linalg.norm(cp63)
# print(area63)
#==============================================================================

#v71 = vector.Vector(['2', '3'])
#v72 = vector.Vector(['3', '-2'])
#print(v71.dotproduct(v72))

line71 = Line([4.046, 2.836], 1.21)
line72 = Line([10.115, 7.09], 3.025)
print(line71.basepoint)
check1 = line71.is_parallel(line72)
print(check1)








