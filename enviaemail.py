import smtplib
import email.message
from email import encoders
from email.mime.base import MIMEBase    
from email.mime.multipart import MIMEMultipart
from email.mime.audio import MIMEAudio
from email.mime.text import MIMEText
from filmes import*

class Email(Top200filmes):        
    def envioemail():
        top200filmes = Top200filmes
        filmealeatorio = top200filmes.filme200aleatorio(Top200filmes.apiJson)   
        
        corpo_email = f"""
        <p>Se liga nesse filme aqui {filmealeatorio}</p>
        """    
        msg = email.message.Message()
        msg['Subject'] = "Python"
        msg['From'] = 'jeroldmarlon12@gmail.com'
        msg['To'] = 'jeroldmarlon12@gmail.com'
        password = 'svspztowavhmvlgp'
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo_email )

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        print('Email enviado')
    
    envioemail()        