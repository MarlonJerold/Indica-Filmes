import requests

class Conexao:
    
    def top200filmesAPI():
        conect = requests.get("https://imdb-api.com/en/API/Top250Movies/k_l89y0mfu")
        valor_requisicao = conect.json()
        return valor_requisicao


