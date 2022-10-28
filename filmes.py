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
        keys = apiJson['items'][number].keys()  
        values = apiJson['items'][number].values()
        dadostratado = pd.DataFrame(values, index=keys)
        return dadostratado
        

          
    
    