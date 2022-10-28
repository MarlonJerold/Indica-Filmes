from random import randint
import pandas as pd

from conectaapi import *

class Top200filmes:
        
    conexao = Conexao
    apiJson = conexao.top200filmesAPI()
                        
    def filme200aleatorio(apiJson):
        
        numero = randint(1,200)        
        keys = apiJson['items'][numero].keys()  
        values = apiJson['items'][numero].values()
        dadostratado = pd.DataFrame(values, index=keys)
        print(dadostratado)   
        return dadostratado
    
    def listafilmestitle(apiJson):
        posicao = 0
        filmeslistados = []
        while posicao < 200:
            filme = apiJson['items'][posicao]['title']        
            filmeslistados.append(filme)    
            posicao+=1            
        return filmeslistados
    
    