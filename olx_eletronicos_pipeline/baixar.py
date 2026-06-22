import gzip
from curl_cffi import requests
from bs4 import BeautifulSoup as bs
import os 


sessao = requests.Session(impersonate="chrome")
pasta = 'xml'


def baixar_arquivo(sessao, pasta):

    links = ['https://www.olx.com.br/celulares/apple/estado-pe', 'https://www.olx.com.br/celulares/asus/estado-pe', 'https://www.olx.com.br/celulares/huawei/estado-pe', 'https://www.olx.com.br/celulares/infinix/estado_pe', 'https://www.olx.com.br/celulares/lenovo/estado-pe', 'https://www.olx.com.br/celulares/lg/estado-pe', 'https://www.olx.com.br/celulares/motorola/estado-pe', 'https://www.olx.com.br/celulares/samsung/estado-pe',  'https://www.olx.com.br/celulares/xiaomi/estado-pe']
    tam = len(links)
    marcas = [link.split('/')[4] + ".xml" for link in links]
    for i in range(0, tam):

        link = links[i]

        resposta = sessao.get(link)

        arquivo = marcas[i]
        caminho = os.path.join(pasta, arquivo)


        if resposta.status_code == 200:
            with open(caminho, "wb") as f:
                f.write(resposta.content)
            print("Arquivo extraído e salvo com sucesso")
        else:
            print("Erro ao tentar baixar o arquivo")


def lista_anuncios():

    i = 0
    lista_link = []

    caminho = os.path.dirname(os.path.abspath(__file__))
    caminho_xml = os.path.join(caminho,'xml')

    lista_arquivo = os.listdir(caminho_xml)
    tam_lista = len(lista_arquivo)
    

    for i in range(0, tam_lista):
        print("extraindo a lista de anuncios do arquivo:", lista_arquivo[i])

        nome_arq = lista_arquivo[i]
        arquivo = os.path.join(caminho_xml, nome_arq)

        with open(arquivo) as f:
            conteudo = f.read()

        site = bs(conteudo, "html.parser")

        lista_url = site.find_all('a', href=True)
        for tag in lista_url:

            link = tag['href']

            lista_link.append(link)
    

    return lista_link



        
baixar_arquivo(sessao, pasta)

lista_anuncios()



    
