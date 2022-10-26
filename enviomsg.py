import smtplib
import email.message
import requests
import pandas as pd
import json

def api_dolar():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
    requisicao_dicionario = requisicao.json()
    cotacao = float(requisicao_dicionario['USDBRL']['bid'])
    print(cotacao)

def envioemail():   
    corpo_email = f"""
    <p>A cotação do dólar é de {cotacao}</p>
    """    
    msg = email.message.Message()
    msg['Subject'] = "Python"
    msg['From'] = 'jeroldmarlon12@gmail.com'
    msg['To'] = 'jeroldmarlon12@gmail.com'
    password = '***'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )
    
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

def conect_api_filmes():
    conect = requests.get("https://imdb-api.com/en/API/Top250Movies/k_l89y0mfu")
    valor_requisicao = conect.json()
    print(valor_requisicao)
    
    value = 0
    while value < 200:
        keys = valor_requisicao['items'][value].keys()  
        values = valor_requisicao['items'][value].values()
        value = value + 1 
        df = pd.DataFrame(values, index=keys, columns=[''])
        print("________________")
        print(df)

conect_api_filmes()    