import numpy as np

input_size = 3 #D
hidden_size = 4
num_classes = 2
num_inputs = 5
output_size = num_classes

std = 1e-4
W1 = std * np.random.randn(input_size, hidden_size)  #[3x4] [DxH]
b1 = np.zeros(hidden_size)                           #[4x1]
#b1 = np.array([1,1,1,1])
W2 = std * np.random.randn(hidden_size, output_size) #[4x2]
b2 = np.zeros(output_size)                           #[2x1]
print 'b1',b1.shape

f = lambda x: 1.0/(1.0 + np.exp(-x))  # activation function
X = 10 * np.random.randn(num_inputs, input_size)             # random input vector of three numbers (5x3) [1xD]
print 'X*W1 = ', X.dot(W1)
print 'b1', b1
print 'X.dot(W1) +b1',(X.dot(W1) +b1)
h1 = f( X.dot(W1) +b1)                # (h1 =np.dot(W1,f(x)) is wrong) calculate  first hidden layer activations (4x3)
scores = f( h1.dot(W2) + b2)             # calculate second layer activations (4x1)
print scores.shape

N, D = X.shape
print 'N',N
print 'D',D
#y=None
y = np.array([0, 1, 2, 2, 1])
exp_scores = np.exp(scores)
probs = exp_scores / np.sum(exp_scores,axis=1, keepdims=True)
print 'type(probs)', type(probs)
print 'probs.shape'
print probs.shape

print 'probs = ' 
print  probs
print '---'

print y
print type(y)
print list(y) # [0, 1, 2, 2, 1]

print range(N) # [0, 1, 2, 3, 4]

print 'probs[[0, 1, 2, 3, 4], [0, 1, 2, 2, 1]] = '
print  probs[[0, 1, 2, 3, 4], [0, 1, 2, 2, 1]]
