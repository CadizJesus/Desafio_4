import numpy as np
from data import Data

class Neuron:
    previous_layer = []
    previous_weights = []
    value = float()
    weight_updated = []
    next_layer = []
    
    def __init__(self, previous_layer = None, previous_weights = None, value = None):
        self.previous_layer = previous_layer
        self.previous_weights = previous_weights
        self.value = value
        """if value:
            self.value = value
        else:
            self.value = self.calculate_value()"""

    def act_sigmoid(self):
        return 1/(1+np.exp(-self.value))

    def derivate_sigmoid(self,a):
            return a*(1-a)

    def calculate_value(self):
        value = 0
        for i in range(len(self.previous_layer)):
             value += self.previous_layer[i].act_sigmoid() * self.previous_weights[i]
        return value

class Network:
    list_layers = []
    data = None

    def __init__(self):
        self.list_layers = []
        data = Data()

    def add_layer(self, n_neuronas, row):
        layer = []
        if not self.list_layers:
            layer = self.add_first_layer(row)
        else:
            if len(self.list_layers) == 1:
                for n in range(n_neuronas):
                    layer.append(Neuron(previous_weights = self.ini_weight(self.list_layers[0]), previous_layer = self.list_layers[0]))
            else:
                for n in range(n_neuronas):
                    layer.append(Neuron(previous_weights = self.ini_weight(self.list_layers[-1]), previous_layer = self.list_layers[-1]))

        self.list_layers.append(layer)

    def add_first_layer(self, row):
        layer = []
        for i in range(len(row)):    
            layer.append(Neuron())
        return layer
    
    def ini_weight(self, first_layer):
        random_weights = []
        
        for i in range(len(first_layer)):
            weight = np.random.random_sample()   
            random_weights.append(weight)

        return random_weights

    def create_network(self, input):
        self.add_layer(len(input), input)
        p=1
        while((len(input)/(2**p))>3):
            self.add_layer(int(len(input)/2**p),None)
            p=p+1

        self.add_layer(2,None)
    
    def predict(self, input):
        for i in range(len(self.list_layers)):
            if i == 0:
                for j in range(len(input)):
                    self.list_layers[0][j].value = input[j]
            else:
                for n in self.list_layers[i]:
                    n.previous_layer = self.list_layers[i-1]
                    n.value = n.calculate_value()
        return self.list_layers[-1]
            


a = Network()
a.create_network([1,2,3,4,5,6,7,8,9,10])
a.predict([1,2,3,4,5,6,7,8,9,10])

i=0
for layer in a.list_layers:
    print("=================layer=========")
    for n in layer:
        print("value: ",n.value)
    if i!=0:
        print("===========previous======layer=========")
        for ne in (layer[0].previous_layer):
            
            print("value: ",ne.value)
    i+=1