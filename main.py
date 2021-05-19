import numpy as np
from data import load_data

class Neuron:
    previous_layer = []
    previus_weights = []
    value = float()
    weight_updated = []
    next_layer = []

    def __init__(self, previous_layer = None, previus_weights = None, value = None):
        self.previous_layer = previous_layer
        self.previus_weights = previus_weights
        self.value = value

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
    data        = None
       
    def __init__(self):
        self.list_layers = []

    def add_layer(self):

        return 1

    def load_data(self):
        self.data
