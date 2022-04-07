from django.shortcuts import render
import requests # faz requisições HTTP

"""
def index(request):
    api = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/24/municipios"
    requisicao = requests.get(api)

    try:
        lista = requisicao.json()
    except ValueError:
        print("A resposta não chegou com o formato esperado.")

    dicionario = {}
    for indice, valor in enumerate(lista):
        dicionario[indice] = valor

    contexto = {
        "municipios": dicionario
    }

    return render(request, "index.html", contexto)
"""

def index(request):
    api = "http://127.0.0.1:8000/home/products"
    requisicaoGet = requests.get(api)

    try:
        lista = requisicaoGet.json()

    except ValueError:
        print("A resposta não chegou com o formato esperado.")

    dicionario = {}
    for indice, valor in enumerate(lista):
        dicionario[indice] = valor

    contexto = {
        "products": dicionario
    }

    return render(request, "index.html", contexto)
