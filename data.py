import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

class Data:
    X_train = None
    y_train = None
    X_test = None
    y_test = None

    def __init__(self):
        (self.X_train, self.y_train),(self.X_test, self.y_test) = self.load_data()


    def load_data(self):
        df = pd.read_csv('data.csv')

        #se dropean columnas que consideramos que no nos sirven
        df = df.drop(columns=['Unnamed: 0','song_title','artist'])

        X = df[list(df.columns[:-1])]
        y = df[[df.columns[-1]]]

        (X_train, X_test, y_train, y_test) = train_test_split(X, y, test_size=0.3, random_state=42)
        
        return (X_train, y_train),(X_test, y_test)
