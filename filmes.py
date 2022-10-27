from random import randint
import smtplib
import email.message
import requests
import pandas as pd
import numpy as np
from sympy import numer

from conectaapi import *


class Filmes:
        
    conectar = Conexao
    apiJson = conectar.leituraJson()
                
    def Top200filmes(apiJson, number):   
                      
        keys = apiJson['imDbId'][number].keys()  
        values = apiJson['imDbId'][number].values()
        dadostratado = pd.DataFrame(values, index=keys)
        print(dadostratado)
        
    def filme200aleatorio(apiJson, number):
        
        numer = range(1,200)    
        keys = apiJson['imDbId'][number].keys()  
        values = apiJson['imDbId'][number].values()
        dadostratado = pd.DataFrame(values, index=keys)
        print(dadostratado)   
        