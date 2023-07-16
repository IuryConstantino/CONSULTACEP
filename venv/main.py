#Consulta CEP:

import requests


def buscar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    data = response.json()
    return data

cep = input("Digite o CEP: ")
endereco = buscar_cep(cep)

if "erro" not in endereco:
    print("CEP:", endereco["cep"])
    print("Logradouro:", endereco["logradouro"])
    print("Complemento:", endereco["complemento"])
    print("Bairro:", endereco["bairro"])
    print("Cidade:", endereco["localidade"])
    print("Estado:", endereco["uf"])
else:
    print("CEP não encontrado.")