import numpy as np

# número de horas estudiando , número de horas durmiendo
#entradas ( inputs)
x = np.array(([2,9],[1,5],[3,6]),dtype=float)

# calificación del examen base 100
y = np.array(([92],[86],[89]),dtype=float)

x_predicted = np.array(([4,8]), dtype=float)

# escala de unidades
scale_x = x/np.amax(x,axis=0)
scale_y = y/100
scale_x_predicted = x_predicted/np.max(x_predicted,axis=0)

#print(scale_x,"\n")
#print(scale_y,"\n")
#print(scale_x_predicted,"\n")



#parametros
InputSize = 2
OutputSize = 1
HiddenSize = 3
#pesos
w1 = np.random.randn(InputSize,HiddenSize)
w2 = np.random.randn(HiddenSize,OutputSize)

def forward(x,w1,w2):
    z = np.dot(x,w1)
    z2 = sigmoid(z)
    z3 = np.dot(z2, w2)
    o = sigmoid(z3)
    return o

def sigmoid(s):
    return 1/(1+np.exp(-s))

def sigmoidPrime(s):
    return s*(1 - s)

def backward(x,y,o,w1,w2):
    o_error = y - o
    o_delta = o_error * sigmoidPrime(o)

    z2_error = o_delta.dot(w2.T)
    z2_delta = z2_error * sigmoidPrime(z2)

    w1 += x.T.dot(z2_delta)
    w2 += z2.T.dot(o_delta)

def train(x,y,w1,w2):
    o = forward(x,w1,w2)
    backward(x,y,o,w1,w2)

def predict(x_predicted,w1,w2):
    print("Predicted data based on trained wights: ")
    print("Input (scaled): \n" + str(x_predicted))
    print("Output: \n" + str(forward(x_predicted,w1,w2)))

def saveweights(w1,w2):
    np.savetxt("w1.txt", w1, fmt="%s")
    np.savetxt("w2.txt", w2, fmt="%s")


#neu_net = Neural_Network()
#o = neu_net.forward(x)
#print("predicted output: \n" + str(o))
#print("Actual output: \n" + str(y)) 

#print(neu_net.forward(x),"\n")
#print( ( y - neu_net.forward(x) )/100 )

for i in range(10000): # trains the NN 1,000 times
    print("Input: \n" + str(scale_x))
    print("Actual Output: \n" + str(scale_y))
    print("Predicted Output: \n" + str(forward(scale_x,w1,w2)))
    print("Loss: " + str( np.mean( np.square( scale_y - forward( scale_x,w1,w2 ) ) ) ) ) # mean sum squared loss
    print("\n")
    train(scale_x, scale_y,w1,w2)

#neu_net.saveweights()
#neu_net.predict()