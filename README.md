# Desafío 4
## Descripción del problema
Para este desafío se debe implementar un algoritmo de recomendación de Spotify, en el cual se predice si al usuario le gustará o no una canción del dataset. En el repositorio se adjunta un Dataset de 2000 canciones aproximadamente, cada una con sus atributos. 

## Solución Propuesta
Para la solución se implementa una red neuronal, como dato de entrada se tiene una canción de ciertos atributos específicos y como dato de salida se obtiene una predicción de si la siguiente canción será o no del gusto del usuario. 

En el preprocesamiento de los datos se analizan los atributos que servirán para la predicción, para el entrenamiento de la red neuronal se utiliza el 70% de los datos del Dataset y para el testeo el 30%, estos datos se normalizan para un mejor funcionamiento de la red.

## Estructura de datos utilizada
### Neuron: 
Estructura que almacena las neuronas de la capa anterior, el valor de los pesos previos, el valor de los pesos actualizados, el valor de la neurona actual y una lista con las neuronas de la siguiente.

-Previous_layer : Lista con las neuronas de la capa anterior 

-Previos_weights : Lista con los pesos de las neuronas anteriores

-Value : Valor de la neurona calculado con la funcion de activacion 

-weight_updated : Peso de la neurona actualizado

-next_layer : Lista con las neuronas de la siguiente capa


### Network: 
Estructura que almacena una lista de capas y un Data el cual contiene los datos del dataset divididos en entrenamiento y prueba 

-list_layers() : lista de las capas de la red las cuales a su vez contienen neuronas.

-data : object Data el cual contiene los datos del dataset divididos en datos de entrenamiento y de prueba 


### Data: 
Estructura que almacena los datos del dataset divididos en datos de entrenamiento y de prueba. 
