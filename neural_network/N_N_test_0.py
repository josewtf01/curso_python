import numpy as np

# número de horas estudiando , número de horas durmiendo
#entradas ( inputs)
x = np.array(([2,9],[1,5],[3,6]),dtype=float)

# calificación del examen base 100
y = np.array(([92],[86],[89]),dtype=float)

#nuevo conjunto de datos , con los cuales predecir una salida
x_predicted = np.array(([4,8]), dtype=float)

# escala de unidades
scale_x = x/np.amax(x,axis=0)
scale_y = y/100
scale_x_predicted = x_predicted/np.max(x_predicted,axis=0)

#print(scale_x,"\n")
#print(scale_y,"\n")
#print(scale_x_predicted,"\n")

class Neural_Network(object):
    def __init__(self):
        #parametros
        self.InputSize = 2
        self.OutputSize = 1
        self.HiddenSize = 3
        #pesos
        print("pesos iniciales : \n")
        self.w1 = np.random.randn(self.InputSize,self.HiddenSize)
        print("w1 = ",self.w1,"\n")
        self.w2 = np.random.randn(self.HiddenSize,self.OutputSize)
        print("w2 = ",self.w2,"\n")
    
    # operaciones 
    def forward(self,x):
        #operaciones a realizar
        # z multiplicación de los pesos w1 por las entradas
        self.z = np.dot(x,self.w1)
        # aplicar la funcion sigmoide a los resultados en z
        self.z2 = self.sigmoid(self.z)
        # z3 multiplicación entre la capa intermedia con los siguiente pesos w2
        self.z3 = np.dot(self.z2, self.w2)
        # aplicar función sigmoide para obtener las salidas de cada ejemplo
        o = self.sigmoid(self.z3)
        return o
    
    # definición de función sigmoide
    def sigmoid(self,s):
        return 1/(1+np.exp(-s))
    
    # derivada de la función sigmoide
    def sigmoidPrime(self,s):
        return s*(1 - s)
    
    # backpropagation
    def backward(self,x,y,o):
        # error entre valores reales y predicciones
        self.o_error = y - o
        # aplicar la derivada de nuestra función al error
        self.o_delta = self.o_error * self.sigmoidPrime(o)
        #obtener error entre el delta del error y los pesos de la capa interna a la salida
        self.z2_error = self.o_delta.dot(self.w2.T)
        # aplicar la derivada de nuestra función al error de los pesos en la capa interna
        self.z2_delta = self.z2_error * self.sigmoidPrime(self.z2)
        # modificar los valores de los pesos 
        self.w1 += x.T.dot(self.z2_delta)
        self.w2 += self.z2.T.dot(self.o_delta)
    
    # entrenamiento
    def train(self,x,y):
        #realizar las operaciones de propagación
        o = self.forward(x)
        # realizar las operaciones de propagación inversa
        self.backward(x,y,o)
    # predicion
    def predict(self):
        print("Predicted data based on trained wights: ")
        print("Input (scaled): \n" + str(x_predicted))
        print("Output: \n" + str(self.forward(x_predicted)))
    #salvar pesos despueés del entrenamiento
    def saveweights(self):
        np.savetxt("w1.txt", self.w1, fmt="%s")
        np.savetxt("w2.txt", self.w2, fmt="%s")


neu_net = Neural_Network()
'''
o = neu_net.forward(x)
print("predicted output: \n" + str(o))
print("Actual output: \n" + str(y)) 
'''

for i in range(10000): # trains the NN 1,000 times
    print("Input: \n" + str(scale_x),"\n")
    print("Actual Output: \n" + str(scale_y),"\n")
    print("Predicted Output: \n" + str(neu_net.forward(scale_x)),"\n")
    print("Loss: " + str( np.mean( np.square( scale_y - neu_net.forward( scale_x ) ) ) ),"\n" ) # mean sum squared loss
    print("\n")
    neu_net.train(scale_x, scale_y)

#neu_net.saveweights()
neu_net.predict()
