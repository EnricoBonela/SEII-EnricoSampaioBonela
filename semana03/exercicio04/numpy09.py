#Reshape
import numpy as np
a = np.arange(1, 7)
print(a)
b = a.reshape((2, 3))
print(b)
c = a.reshape((3, 2))
print(c)
print(a.shape)
d = a[np.newaxis, :]
print(d)
print(d.shape)
e = a[:, np.newaxis]
print(e)
print(e.shape)
