import numpy as np
from data import Data

class Neuron:
    previous_layer = []
    previous_weights = []
    value = float()
    
    def __init__(self, previous_layer = None, previous_weights = None, value = None):
        self.previous_layer = previous_layer
        self.previous_weights = previous_weights
        self.value = value

    def act_sigmoid(self):
        return 1/(1+np.exp(-self.value))

    def derivate_sigmoid(self):
            return self.act_sigmoid()*(1-self.act_sigmoid())

    def calculate_value(self):
        value = 0
        for i in range(len(self.previous_layer)):
             value += self.previous_layer[i].act_sigmoid() * self.previous_weights[i]
        self.value = value

class Network:
    list_layers = []
    data = None

    def __init__(self):
        self.list_layers = []
        self.data = Data()

    def add_layer(self, n_neuronas):
        layer = []
        if not self.list_layers:
            layer = self.add_first_layer(n_neuronas)
        else:
            if len(self.list_layers) == 1:
                for n in range(n_neuronas):
                    layer.append(Neuron(previous_weights = self.ini_weight(self.list_layers[0]), previous_layer = self.list_layers[0]))
            else:
                for n in range(n_neuronas):
                    layer.append(Neuron(previous_weights = self.ini_weight(self.list_layers[-1]), previous_layer = self.list_layers[-1]))

        self.list_layers.append(layer)

    def add_first_layer(self, n_neuronas):
        layer = []
        for i in range(n_neuronas): 
            layer.append(Neuron())
        return layer
    
    def ini_weight(self, last_layer):
        random_weights = []
        
        for i in range(len(last_layer)):
            weight = np.random.random_sample()   
            random_weights.append(weight)
        return random_weights

    def create_network(self, hidden_layers):
        num_neuron_input_layer = (self.data.X_train.shape[1])
        self.add_layer(num_neuron_input_layer)
        for num_neuron in hidden_layers:
            if num_neuron != 0:
                self.add_layer(num_neuron)
        self.add_layer(1)
    
    def predict(self, input):
        for i in range(len(self.list_layers)):
            if i == 0:
                for j in range(len(input)):
                    self.list_layers[i][j].value = input[j]
            else:
                for n in self.list_layers[i]:
                    n.previous_layer = self.list_layers[i-1]
                    n.calculate_value()
        return self.list_layers[-1] #se retorna la ultima capa
            
    def calculate_new_weigth(self, learning_rate, expected_value):
        deltas=[None]*len(self.list_layers)
        for i in reversed(range(len(self.list_layers))): #se recorre la lista de layers desde la última a la primera layer
            if(i == len(self.list_layers)-1):
                deltas_layers = []
                k=0
                for neuron in self.list_layers[i]: #se recorre las neuronas de la última layer, en este caso 1
                    current_delta = (neuron.act_sigmoid() - expected_value[k]) * neuron.derivate_sigmoid()
                    deltas_layers.append(current_delta)
                    k=k+1
                deltas[i] = deltas_layers
            else:
                deltas_layers = []
                for j in range(len(self.list_layers[i])): #se recorre las neuronas de una layer
                    sum=0
                    n_weights = self.neuron_list_weights(j,i)
                    
                    for k in range(len(deltas[i+1])):
                        sum = sum + deltas[i+1][k]*n_weights[k]
                    
                    current_delta = sum*self.list_layers[i][j].derivate_sigmoid()
                    deltas_layers.append(current_delta)
                deltas[i] = deltas_layers
        self.update_weights(deltas, learning_rate)

    def neuron_list_weights(self, i_neuron, i_layer): #recibe el índice de la neurona  de la capa actual, retorna la lista de pesos asociados a tal neurona
        list_weights=[]
        for neuron in self.list_layers[i_layer+1]:
            list_weights.append(neuron.previous_weights[i_neuron])
        return list_weights
    
    def update_weights(self,deltas,learning_rate):
        for i in range(len(self.list_layers)):
            if( i != 0 ):
                for j in range(len(self.list_layers[i])):
                    for k in range(len(self.list_layers[i][j].previous_weights)):
                        self.list_layers[i][j].previous_weights[k] = self.list_layers[i][j].previous_weights[k] - learning_rate*deltas[i][j]*self.list_layers[i-1][k].act_sigmoid()
     
    def train(self, iter):
        for iterator in range(1,iter+1):
            print("      entrenando: ", iterator*100/iter,"%", end='\r')
            
            for i in range(self.data.X_train.shape[0]):
                row = self.data.X_train[i]
                self.predict(row)
                self.calculate_new_weigth(0.5,self.data.y_train[i])
        print()   

    def test(self):
        count_1=0
        count_0=0
        count_err=0
        for i in range(self.data.X_test.shape[0]):
            if(self.predict(self.data.X_test[i])[0].act_sigmoid()>0.5 and self.data.y_test[i][0]==1):
                count_1+=1
                continue
            if(self.predict(self.data.X_test[i])[0].act_sigmoid()<=0.5 and self.data.y_test[i][0]==0):
                count_0+=1
                continue
            count_err+=1 
        print("total: ", self.data.y_test.shape[0])
        print("aciertos de 1: ", count_1)
        print("aciertos de 0: ", count_0)
        print("erradas: ", count_err)
        print("porcentaje de acierto: ",(100/self.data.y_test.shape[0])*(count_1+count_0))

def menu_cli():
    print("Desafio 4: Red Neuronal")
    layers = input("Ingrese Número de Neuronas de cada capa oculta (separadas por coma pj: 12,6,2, se recomienda solo una capa con 8 neuronas): ")
    layers = layers.split(",")
    
    for i in range(len(layers)):
        layers[i] = int(layers[i])
    
    iter = input("Ingrese el máximo de iteraciones(se recomienda 200 o 500): ")
    iter = int(iter)
    nn = Network()
    nn.create_network(layers)
    nn.train(iter)
    nn.test()

if __name__ == "__main__":
    menu_cli()