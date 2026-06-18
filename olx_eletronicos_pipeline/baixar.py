import gzip
from curl_cffi import requests
import os 


sessao = requests.Session(impersonate="chrome")


def Baixar_Apple(sessao):

    link = "https://www.olx.com.br/celulares/apple/estado-pe" 

    resposta = sessao.get(link)

    pasta_destino = 'xml'
    arquivo = 'Apple.xml'
    caminho_final = os.path.join(pasta_destino, arquivo)


    if resposta.status_code == 200:
        with open(caminho_final, "wb") as f:
            f.write(resposta.content)
        print("Arquivo extraído e salvo com sucesso!")
    else:
        print("Erro ao tentar baixar o arquivo.")

    

