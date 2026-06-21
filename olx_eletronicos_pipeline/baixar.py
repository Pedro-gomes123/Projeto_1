import gzip
from curl_cffi import requests
import os 


sessao = requests.Session(impersonate="chrome")
pasta = 'xml'


def baixar_Apple(sessao, pasta):

    link = 'https://www.olx.com.br/celulares/apple/estado-pe'

    resposta = sessao.get(link)

    arquivo = 'Apple.xml'
    caminho = os.path.join(pasta, arquivo)


    if resposta.status_code == 200:
        with open(caminho, "wb") as f:
            f.write(resposta.content)
        print("Arquivo extraído e salvo com sucesso")
    else:
        print("Erro ao tentar baixar o arquivo")

    
def baixar_asus(sessao, pasta):
    
    link = 'https://www.olx.com.br/celulares/asus/estado-pe'

    resposta = sessao.get(link)

    
    arquivo = 'Asus.xml'
    caminho = os.path.join(pasta, arquivo)

    if resposta.status_code == 200:
        with open(caminho, 'wb') as f:
            f.write(resposta.content)
        print("Arquivo extraido e salvo com sucesso")
    else:
        print("Erro ao tentar baixar o arquivo")

def baixar_huawei(sessao, pasta):
    
    link = 'https://www.olx.com.br/celulares/huawei/estado-pe'

    resposta = sessao.get(link)
    arquivo = 'huawei'
    caminho = os.path.join(pasta,arquivo)

    if resposta.status_code == 200:
        with open(caminho, 'wb') as f:
            f.write(resposta.content)
        print("Arquivo extraido com sucesso")
    else:
        print("Erro ao tentar baixar o arquivo")

def baixar_infinix(sessao, pasta):

    link = 'https://www.olx.com.br/celulares/infinix/estado_pe'

    resposta = sessao.get(link)
    arquivo = 'infinix'
    caminho = os.path.join(pasta, arquivo)

    if resposta.status_code == 200:
        with open(caminho, 'wb') as f:
            f.write(resposta.content)
        print("Arquivo extraido com sucesso")
    else:
        print("Erro ao tentar baixar o arquivo")

def baixar_lenovo(sessao, pasta):

    link = 'https://www.olx.com.br/celulares/lenovo/estado-pe'

    resposta = sessao.get(link)
    arquivo = 'lenovo'
    caminho = os.path.join(pasta, arquivo)

    if resposta.status_code() == 200:
        with open(caminho, 'wb') as f:
            f.write(resposta.content)
    else:
        print("Erro ao tentar baixar o arquivo")


def baixar_lg(sessao, pasta):
    
    link = 'https://www.olx.com.br/celulares/lg/estado-pe'

    resposta = sessao.get(link)
    arquivo = 'lg'
    caminho = os.path.join(pasta, arquivo)

    if resposta.status_code() == 200:
        with open(caminho, 'wb') as f:
            f.write(resposta.content)
    else:
        print("Erro ao tentar baixar o arquivo")

def baixar_motorola(sessao, pasta):

    link = 'https://www.olx.com.br/celulares/motorola/estado-pe'

    resposta = sessao.get(link)
    arquivo = 'motorola'
    caminho = os.path.join(pasta, arquivo)
    
    if resposta.status_code() == 200:
        with open(caminho, 'wb') as f:
            f.write(resposta.content)
    else:
        print("Erro ao tentar baixar o arquivo")

def baixar_samsung(sessao, pasta):

    link = 'https://www.olx.com.br/celulares/samsung/estado-pe'

    resposta = sessao.get(link)
    arquivo = 'samsung'
    caminho = os.path.join(pasta, arquivo)

    if resposta.status_code() == 200:
        with open(caminho, 'wb') as f:
            f.write(resposta.content)
    else:
        print("Erro ao baixar o arquivo")

def baixar_xiaomi(sessao, pasta):

    link = 'https://www.olx.com.br/celulares/xiaomi/estado-pe'

    resposta = sessao.get(link)
    arquivo = 'xiaomi'
    caminho = os.path.join(pasta, arquivo)

    if resposta.status_code() == 200:
        with open(caminho,'wb') as f:
            f.write(resposta.contnt)
    else:
        print("Erro ao baixar o arquivo")       





    
