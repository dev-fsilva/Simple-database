import json
# import pandas as pd

# Abrir e carregar os dados do arquivo
try:
    # Caminho para o arquivo
    with open('./company.data.json','r') as arquivo_json:
        object_json = json.load(arquivo_json)
except FileNotFoundError:
    print("File not found. Creating a new one")
    object_json = {}  # Cria um dicionário vazio se o arquivo não existir

# Criando CPF aleatorios
adc = input('To add?\n1-Yes\n2-No\n>')
if adc == '1':
    import random
    # Editar os dados
    NameCompany = input("Enter company name: ")
    CnpjCompany = int(input("Enter the CNPJ: "))
    
    code5digts = ''
    for i in range(4):
        code5digts += str(random.randint(0, 5))
        
    # Adicionar as informações ao dicionário
    if code5digts not in object_json:
        object_json[code5digts] = []

    object_json[code5digts].append(
        {
            'Name' : NameCompany,
            'CNPJ' : CnpjCompany
        }
    )
else:
    print(object_json)

# Mostrando empresas cadastradas:
for codes in object_json.keys():
    print("Name:",object_json[codes][0]["Name"],"\nCNPJ:",object_json[codes][0]["CNPJ"])

#delete = object_json.pop("0334")
#print(object_json)

# Salvar os dados de volta no arquivo
with open('./company.data.json', 'w') as arquivo_json:
    json.dump(object_json, arquivo_json, indent=4)

print("File updated successfully!")