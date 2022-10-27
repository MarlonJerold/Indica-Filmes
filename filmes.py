import smtplib
import email.message
import requests
import pandas as pd


from conectaapi import *

from random import randint 


class Filmes(Conexao):
        
    conectar = Conexao
    apiJson = conectar.teste()  

    
    def keysapiflimes(apiJson):
        keys = apiJson['items'][0].keys()    
        return keys
    
    def valuesapifilmes(apiJson):
        values = apiJson['items'][0].values()  
        return values        
        
    def filmealeatorio():
        valor = Filmes
        testevalues = valor.valuesapifilmes()
        keys = Filmes
        testekeys = keys.keysapiflimes()
    
        dadostratado = pd.DataFrame(testevalues, index=testekeys)
        print(dadostratado)
                
    filmealeatorio()      