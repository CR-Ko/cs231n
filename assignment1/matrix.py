import numpy as np

X = np.array([[1, 2, 3], [6, 5, 4]])                              # 2 x 3 array
X_train = np.array([[-4, -5, -6], [-3, -2, -1] , [-7, -8, -9]])   # 3 x 3 array
y_train = np.array([1, 2 , 3])   
num_test  =  X.shape[0]
num_train =  X_train.shape[0]
dists1 = np.zeros((num_test, num_train))
dists2 = np.zeros((num_test, num_train))
dists3 = np.zeros((num_test, num_train))

#print X.shape 
#print X_train.shape
print('num_test = ' , num_test)
print('num_train = ', num_train)


for i in xrange(num_test): #only scan to num_test-1
   for j in xrange(num_train):
	       dists1[i,j] = np.sqrt(np.sum(np.square(X[i] - X_train[j])))
               #dists2[i,:] = np.linalg.norm(X[i] - X_train)
               #print i, dists[i,:]


for i in xrange(num_test): #only scan to num_test-1
   #for j in xrange(num_train):
	       #dists1[i,j] = np.sqrt(np.sum(np.square(X[i] - X_train[j])))
               dists2[i,:] = np.linalg.norm(X[i] - X_train , axis=1)
               #print i,  dists2[i,:]

M = np.dot(X, X_train.T)
print M
te = np.square(X).sum(axis = 1)
print te
tr = np.square(X_train).sum(axis = 1)
print tr 
dists3 = np.sqrt(-2*M+tr+np.matrix(te).T)

#dists3 = X   X_train

     


print dists1
print dists2
print dists3
print '------------------'
num_folds = 5
k_choices = [1, 3, 5, 8, 10, 12, 15, 20, 50, 100]
#for k in range(num_folds):
#    print(k)

#index = np.argsort(dists)
#idx = index[0]

#print idx[1]
#print idx.shape

#k=1
#print idx.find[k-1]

#for z in xrange(num_train):
#     print z ,idx[z]# should be 0, 1, 2 ok
#     if z == k
#        print idx[]   
 


#idx_min = np.argmin(index[0]) # index[i]: the index list of the ith testing point

#for i in xrange(num_test):
#   closest_y = []
#   idx = index[i]
#   print idx

#print index
#print idx_min
#print dists
#print dists[1,:]
#print dists[1]
#labels = y_train[np.argsort(dists[1,:])].flatten()
#print np.argsort(dists[1,:])
#k=2
#print y_train[np.argsort(dists[1,:])]
#print labels.shape
#print labels[0:k]
#print index
#print np.take(np.argsort(dists),0,1)

print('---')
x = np.arange(15.0)
print x.reshape(5,3)
print np.array_split(x, 5)
#[array([ 0.,  1.,  2.]), array([ 3.,  4.,  5.]), array([ 6.,  7.])]
X_train_folds = np.array_split(x, 5)
print('---')
j=4
print X_train_folds[0:j]   #[0:j]     0    to  j-1  0, 1
print X_train_folds[j+1:]  #[j+1:]   j+1   to  end  3, 4 
X_train_cv = np.vstack(X_train_folds[0:j]+X_train_folds[j+1:])
X_test_cv = X_train_folds[j]
print X_train_cv 
print X_test_cv

k_to_accuracies = {}
#print k_to_accuracies
for k in k_choices:
    #print k
    k_to_accuracies[k] = [] #{1: [], 3: [], 100: [], 5: [], 8: [], 10: [], 12: [], 15: [], 50: [], 20: []}

#print k_to_accuracies




