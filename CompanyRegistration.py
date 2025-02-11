import json
import pandas as pd

def toReceiveCategory(numr):
    categories = {
        '1': "Logistics",
        '2': "Carrier",
        '3': "Food",
        '4': "Cleaning"
    }
    return categories.get(numr, "Not defined")

def OpenAndCloseen(x,y=None):
    # Abrir e carregar os dados do arquivo
    if x == 'A':
        try:
            # Caminho para o arquivo
            with open('./company.data.json','r') as arquivo_json:
                return json.load(arquivo_json)
            
        except FileNotFoundError:
            # Cria um dicionário vazio se o arquivo não existir    
            return {}
    elif x == 'F':
        # Salvar os dados de volta no arquivo
        if y is not None:
            with open('./company.data.json', 'w') as arquivo_json:
                json.dump(y, arquivo_json, indent=4)
            return "File updated successfully!"
        return "No data to save."
    else:
        return "Invalid option."
    
# Abrindo ou criando arquivo JSON
object_json = OpenAndCloseen(x='A')

# Abrir e carregar os dados do arquivo
try:
    # Caminho para o arquivo
    with open('./company.data.json','r') as arquivo_json:
        object_json = json.load(arquivo_json)
except FileNotFoundError:
    print("File not found. Creating a new one")
    object_json = {}  # Cria um dicionário vazio se o arquivo não existir


adc = input('To add?\n1-Yes\n2-No\n>')
if adc == "1":

    # Editar os dados
    NameCompany = input("Enter company name: ").strip()
    while True:
        CnpjCompany = input("Enter the CNPJ: (14 digits): ").strip()
        if CnpjCompany.isdigit() and len(CnpjCompany) == 14:
            break
        print("Invalid CNPJ! Please enter exactly 14 digits.")   

        if len(str(CnpjCompany)) == 14:
            break

        else:
            print("Enter numbers only!!!")
            continue

    Add = input("Enter the number corresponding to the category:\n1|>Logistics\n2|>Carrier\n3|>Food\n4|>Cleaning\n|>")
    Category = toReceiveCategory(Add[0])

    # Cria o codigo de 5 digitos
    import random
    code5digts = ''
    for i in range(5):
        code5digts += str(random.randint(0, 5))
        
    # Adiciona as informações ao dicionário
    if code5digts not in object_json:
        object_json.update(
            {   
                f"RegistrationCode-{code5digts}":
                {
                    'NAME' : NameCompany,
                    'CNPJ' : CnpjCompany,
                    'CATEGORY': Category,
                }
            }
        )
else:
    # Mostra empresas cadastradas:
    json_index = json.dumps(object_json)
    print(pd.read_json(json_index, orient = 'index'))

# Salvar os dados de volta no arquivo
with open('./company.data.json', 'w') as arquivo_json:
    json.dump(object_json, arquivo_json, indent=4)

print("File updated successfully!")

"""CRIAR CATEGORIAS - TESTA POSSIVEIS ERROS DE USUARIOS"""