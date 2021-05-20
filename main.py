import numpy as np
from data import Data

class Neuron:
    previous_layer = []
    previus_weights = []
    value = float()
    weight_updated = []
    next_layer = []
    
    def __init__(self, previous_layer = None, previus_weights = None, value = None):
        self.previous_layer = previous_layer
        self.previus_weights = previous_layer
        if not value:
            self.value = value
        else:
            self.value = self.calculate_value()

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
        if len(self.list_layers) == 1:
            for n in range(n_neuronas):
                layer.append(Neuron(previus_weights = self.ini_weight(self.list_layers[0]), previous_layer = self.list_layers[0]))
        else:
            for n in range(n_neuronas):
                layer.append(Neuron(previus_weights = self.ini_weight(self.list_layers[-1]), previous_layer = self.list_layers[-1]))

        self.list_layer.append(layer)

    def add_first_layer(self, row):
        layer = []
        for i in range(len(row)):    
            layer.append(Neuron(value = row[i]))
        return layer
    
    def ini_weight(self, first_layer):
        random_weights = []
        
        for i in range(len(first_layer)):
            weight = np.random.random_sample()   
            random_weights.append(weight)

        return random_weights


a = Network()
a.add_layer(5,[1,2,3,4,5])
