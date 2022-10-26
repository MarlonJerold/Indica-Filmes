import smtplib
import email.message
import requests

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
    password = '****'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )
    
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

if(cotacao < 6):
    envioemail()