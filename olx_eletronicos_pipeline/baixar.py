import gzip
from curl_cffi import requests
from bs4 import BeautifulSoup as bs
import os 
import pandas  as pd 

#source olx_eletronicos_pipeline/.venv/bin/activate



def baixar_arquivo():

    sessao = requests.Session(impersonate="chrome")
    pasta = 'xml'

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
        if nome_arq.startswith('.'):
            continue
        arquivo = os.path.join(caminho_xml, nome_arq)

        with open(arquivo) as f:
            conteudo = f.read()

        site = bs(conteudo, "html.parser")

        lista_url = site.find_all('a', href=True)
        for tag in lista_url:

            link = tag['href']
            if link.startswith('https://pe.olx.com.br/') or link.startswith('https://www.olx.com.br/'):
                            # Evita pegar links de páginas institucionais ou repetidos
                            if 'detalhe' in link or '-anuncio-' in link or 'eletronicos-e-celulares' in link: 
                                if link not in lista_link:
                                    lista_link.append(link)
    tam_url = len(lista_link)
    

    return lista_link, tam_url

def extrair(lista_link, tam_url):
    sessao = requests.Session(impersonate="chrome")
    
    
    dados_anuncios = []

    for i in range(0, tam_url):
        print(f"Coletando anúncio {i+1}/{tam_url}...")
        
        try:
            requisicao = sessao.get(lista_link[i])
            if requisicao.status_code != 200:
                continue
                
            site = bs(requisicao.text, "html.parser")
            spans = site.find_all("span")
            
           
            if len(spans) < 65:
                continue

            
            anuncio = {
                "preço": spans[63].text.strip() if len(spans) > 63 else None,
                "marca": spans[46].text.strip() if len(spans) > 46 else None,
                "modelo": spans[48].text.strip() if len(spans) > 48 else None,
                "armazenamento": spans[52].text.strip() if len(spans) > 52 else None,
                "condição": spans[50].text.strip() if len(spans) > 50 else None,
                "cor": spans[54].text.strip() if len(spans) > 54 else None,
                "bateria": spans[56].text.strip() if len(spans) > 56 else None,
                "localização": spans[59].text.strip() if len(spans) > 59 else None,
                "discrição": spans[42].text.strip() if len(spans) > 42 else None
            }
            
            dados_anuncios.append(anuncio)
            
        except Exception as e:
            print(f"Erro ao acessar o link {lista_link[i]}: {e}")
            continue

    
    if dados_anuncios:
        df = pd.DataFrame(dados_anuncios)
       
        df.to_parquet('resultado_anuncios.parquet', index=False)
        print("Arquivo Parquet salvo com sucesso!")
    else:
        print("Nenhum dado válido foi extraído.")


    
baixar_arquivo()
lista_link, tam_url = lista_anuncios()
extrair(lista_link, tam_url)