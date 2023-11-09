from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

import pandas as pd
import matplotlib.pyplot as plt

def pasar_a_horas_minutos(h_seg):
    h_hora = h_seg // 3600
    h_min = (h_seg % 3600) // 60
    return f'{h_hora} horas y {h_min} minutos'

class AbstractFactory(ABC):
    def __init__(self, datos):
        self.datos = datos

    @abstractmethod
    def calcular_media(self) -> AbstractMedia:
        pass

    @abstractmethod
    def calcular_mediana(self) -> AbstractMediana:
        pass
    
    @abstractmethod
    def graficar_histograma(self) -> AbstractHistograma:
        pass

    @abstractmethod
    def calcular_moda(self) -> AbstractModa:
        pass

class ConcreteFactory_HSolicitud(AbstractFactory):
    def calcular_media(self) -> AbstractMedia:
        return ConcreteMedia_HSol(self.datos)

    def calcular_mediana(self) -> AbstractMediana:
        return ConcreteMediana_HSol(self.datos)
    
    def calcular_moda(self) -> AbstractModa:
        return ConcreteModa_HSol(self.datos)

    def graficar_histograma(self) -> AbstractHistograma:
        return ConcreteHistograma_HSol(self.datos)

class ConcreteFactory_HIntervencion(AbstractFactory):
    def calcular_media(self) -> AbstractMedia:
        return ConcreteMedia_HInterv(self.datos)

    def calcular_mediana(self) -> AbstractMediana:
        return ConcreteMediana_HInterv(self.datos)

    def calcular_moda(self) -> AbstractModa:
        return ConcreteModa_HInterv(self.datos)

    def graficar_histograma(self) -> AbstractHistograma:
        return ConcreteHistograma_HInterv(self.datos)

class AbstractMedia(ABC):
    def __init__(self, datos):
        self.datos = datos

    @abstractmethod
    def calcular_media(self):
        pass

class ConcreteMedia_HSol(AbstractMedia):
    def calcular_media(self):
        return pasar_a_horas_minutos(self.datos['Hora de Solicitud (seg)'].mean())

class ConcreteMedia_HInterv(AbstractMedia):
    def calcular_media(self):
        return pasar_a_horas_minutos(self.datos['Hora de Intervencion (seg)'].mean())

class AbstractMediana(ABC):
    def __init__(self, datos):
        self.datos = datos

    @abstractmethod
    def calcular_mediana(self) -> None:
        pass

class ConcreteMediana_HSol(AbstractMediana):
    def calcular_mediana(self) -> str:
        return pasar_a_horas_minutos(self.datos['Hora de Solicitud (seg)'].median())

class ConcreteMediana_HInterv(AbstractMediana):
    def calcular_mediana(self) -> str:
        return pasar_a_horas_minutos(self.datos['Hora de Intervencion (seg)'].median())

class AbstractModa(ABC):
    def __init__(self, datos):
        self.datos = datos

    @abstractmethod
    def calcular_moda(self) -> str:
        pass

class ConcreteModa_HSol(AbstractModa):
    def calcular_moda(self) -> str:
        return pasar_a_horas_minutos(self.datos['Hora de Solicitud (seg)'].mode()[0])

class ConcreteModa_HInterv(AbstractModa):
    def calcular_moda(self) -> str:
        return pasar_a_horas_minutos(self.datos['Hora de Intervencion (seg)'].mode()[0])

class AbstractHistograma(ABC):
    def __init__(self, datos):
        self.datos = datos

    @abstractmethod
    def graficar_histograma(self) -> str:
        pass

class ConcreteHistograma_HSol(AbstractHistograma):
    def graficar_histograma(self) -> str:
        plt.hist(self.datos['Hora de Solicitud (seg)'], bins=50)
        plt.show()

class ConcreteHistograma_HInterv(AbstractHistograma):
    def graficar_histograma(self) -> str:
        plt.hist(self.datos['Hora de Intervencion (seg)'], bins=50)
        plt.show()

def client_code_media(factory: AbstractFactory) -> None:
    media = factory.calcular_media()
    print(f"Media: {media.calcular_media()}\n")

def client_code_mediana(factory: AbstractFactory) -> None:
    mediana = factory.calcular_mediana()
    print(f"Mediana: {mediana.calcular_mediana()}\n")

def client_code_moda(factory: AbstractFactory) -> None:
    moda = factory.calcular_moda()
    print(f"Moda: {moda.calcular_moda()}\n")

def client_code_histograma(factory: AbstractFactory) -> None:
    histograma = factory.graficar_histograma()
    print("Histograma mostrado en gráfico.\n")

if __name__ == "__main__":
    URL = 'https://datos.madrid.es/egob/catalogo/300178-10-samur-activaciones.csv'
    data = pd.read_csv(URL, sep=';')
    data_1 = data.dropna()
    data_2 = data_1.drop_duplicates()

    df = data_2.copy()
    dict_meses = {'ENERO':1, 'FEBRERO':2, 'MARZO':3, 'ABRIL':4, 'MAYO':5, 'JUNIO':6, 'JULIO':7, 'AGOSTO':8, 'SEPTIEMBRE':9, 'OCTUBRE':10, 'NOVIEMBRE':11, 'DICIEMBRE':12}
    df['Mes'] = df['Mes'].map(dict_meses)

    df['Hora de Solicitud (seg)'] = pd.to_datetime(df['Hora Solicitud'], format='%H:%M:%S')
    df['Hora de Solicitud (seg)'] = df['Hora de Solicitud (seg)'].dt.hour * 3600 + df['Hora de Solicitud (seg)'].dt.minute * 60 + df['Hora de Solicitud (seg)'].dt.second

    df['Hora de Intervencion (seg)'] = pd.to_datetime(df['Hora Intervención'], format='%H:%M:%S')
    df['Hora de Intervencion (seg)'] = df['Hora de Intervencion (seg)'].dt.hour * 3600 + df['Hora de Intervencion (seg)'].dt.minute * 60 + df['Hora de Intervencion (seg)'].dt.second

    factory_h_sol = ConcreteFactory_HSolicitud(df)
    factory_h_interv = ConcreteFactory_HIntervencion(df)

    print()
    print('----------------------------------------')
    print('ESTADÍSTICAS HORA SOLICITUD')
    print('----------------------------------------')
    client_code_media(factory_h_sol)
    client_code_mediana(factory_h_sol)
    client_code_moda(factory_h_sol)
    client_code_histograma(factory_h_sol)

    print()
    print('----------------------------------------')
    print('ESTADÍSTICAS HORA INTERVENCIÓN')
    print('----------------------------------------')
    client_code_media(factory_h_interv)
    client_code_mediana(factory_h_interv)
    client_code_moda(factory_h_interv)
    client_code_histograma(factory_h_interv)
