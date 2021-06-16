import numpy as np

a = np.array([1, 2, 3])
print(a)
print(type(a))

b = np.array([(1, 2, 3), (4, 5, 6), (7,8,9)], dtype=np.uint8)
print(b)
print(type(b))
print(b.shape)
print(b.dtype)
print(b.sum(0))
print(b.sum(1))

c = np.array([(1,2,3),(4,5,6),(7,8,9)])
print(np.multiply(c, b))
print(np.median(c))
print(np.std(b))

d = c.view() # shallow copy
e = c.copy() # deep copy


print(c)
print(c.T)
print(np.transpose(c))






