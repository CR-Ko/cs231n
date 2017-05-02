import numpy as np

a=np.array([[1.0,2.0,3.0],[4.0,5.0,6.0]])
print 'a = '
print a 
print '------------------keepdims=True----------------'
b = np.sum(a, axis=1, keepdims=True)
print 'b.shape = ',b.shape
print 'b = np.sum(a, axis=1, keepdims=True)'
print b	

print 'a/b = '
print a/b

print '------------------keepdims=False----------------'
c = np.sum(a, axis=1, keepdims=False)
print 'c.shape = ',c.shape
print 'c = np.sum(a, axis=1, keepdims=False)'
print c

print 'a/c = '
print a/c

