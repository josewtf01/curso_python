import numpy

def NN(m1,m2,w2,w1,b):
    z = m1*w1+w2*m2+b
    return sigmoid(z)

def sigmoid(x):
    return 1/(1 + numpy.exp(-x))

w1 = numpy.random.randn()
w2 = numpy.random.randn()
b = numpy.random.randn()

print("w1 = ",w1,"\n")
print("w2 = ",w2,"\n")
print("b = ",b,"\n")

print(NN(3,1.5,w1,w2,b))
