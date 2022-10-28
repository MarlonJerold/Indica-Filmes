import smtplib
import email.message

import requests
import pandas as rs
from random import randint 
import json


class Conexao:
    
    
    conect = requests.get("https://imdb-api.com/en/API/Top250Movies/k_l89y0mfu")
    obj = conect.json()
    
    posicao = 0
    while posicao < 2:
        keys = obj['items'][posicao].keys()
        values = obj['items'][posicao].values()
        teste = obj['items'][posicao]['title']
        
        
        print(teste)
        
        
        valor = rs.DataFrame(values, index=keys)
        print(valor)
        posicao += 1
    


    
    


