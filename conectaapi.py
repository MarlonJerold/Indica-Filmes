import smtplib
import email.message
import requests
import pandas as pd
from random import randint 


class Conexao:
    
    def teste():
        conect = requests.get("https://imdb-api.com/en/API/Top250Movies/k_l89y0mfu")
        valor_requisicao = conect.json()
        return valor_requisicao
    


