import numpy as np

a=np.array([[0.886,-0.500,0.000,11.0],[0.5,0.866,0.0,-3],[0,0,1,9],[0,0,0,1]])
b=np.array([[10,20,30,1]]).T
print(a)
print(b)
print(np.dot(a,b))
c=np.array([[1,0,0,11],[0,1,0,-3],[0,0,1,9],[0,0,0,1]])
print(c)
c_=np.linalg.inv(c)
d=np.dot(c_,a)
print(d)