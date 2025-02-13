import json
import pandas as pd
import sys

def toReceiveCategory(numr):
    categories = {
        '1': "Logistics",
        '2': "Carrier",
        '3': "Food",
        '4': "Cleaning"
    }
    return categories.get(numr, "Not defined")
    
# 1.2.
def OpenAndCloseen(x,y=None):
  # 1.2.1
    if x == 'A': 
        try: 
            with open('./company.data.json','r') as arquivo_json:
                return json.load(arquivo_json)
    # 1.2.2
        except FileNotFoundError:
            return {}
    # 3.1.
    elif x == 'F':
        # 3.2.
        if y is not None:
            with open('./company.data.json', 'w') as arquivo_json:
                json.dump(y, arquivo_json, indent=4)
            return "File updated successfully!"
        # 3.3.
        return "No data to save."
    else:
        return "Invalid option."
    
# 1.1
object_json = OpenAndCloseen(x='A')
print("File opened successfully" if object_json != {} else "File not found. Creating a new one")

# 2. 
adc = input('To add?\n1-Yes\n2-No\n3-Data Base\n>')
# 2.1.
if adc == "1":
    # 2.1.1.
    NameCompany = input("Enter company name: ").strip()
    # 2.1.2
    while True:
        CnpjCompany = input("Enter the CNPJ: (14 digits): ").strip()
        caracter_repedito = CnpjCompany != CnpjCompany[0]*len(CnpjCompany)
        if caracter_repedito and CnpjCompany.isdigit() and len(CnpjCompany) == 14:
            break
        else:
            print("Invalid CNPJ! Please enter exactly 14 digits.") 
            print("Enter numbers only!!!")
            continue
        
     # 2.1.3
    Add = input("Enter the number corresponding to the category:\n"
                "1 -> Logistics\n2 -> Carrier\n3 -> Food\n4 -> Cleaning\n> ").strip()
    Category = toReceiveCategory(Add[0])
    
    # 2.1.4.
    import random
    code5digts = ''
    for i in range(5):
        code5digts += str(random.randint(0, 5))
        
    # 2.1.5.
    object_json.update(
        {   
            f"RegistrationCode-{code5digts}":
            {
                'NAME' : NameCompany,
                'CNPJ' : CnpjCompany,
                'CATEGORY': Category
            }
        }
    )
# 2.2.
elif adc == '2':
    print("See you later, Thank you")
# 2.3.
elif adc == '3':
    # Mostra empresas cadastradas:
    json_index = json.dumps(object_json)
    print(pd.read_json(json_index, orient = 'index'))
# 2.4. 
else:
    print("Numero invalido\nPrograma encerrado")
    SystemExit()
    
# 3.
print(OpenAndCloseen(x="F", y=object_json))

# Comenterios do fluxo do programa em Portugues.
""" 
1. Abertura e Carregamento dos Dados
1.1. A variável recebe o valor retornado pela função responsável pelo gerenciamento dos dados.
1.2. A função processa os dados fornecidos e realiza uma das seguintes ações:
    1.2.1. Se a ação for abrir um arquivo existente:
            Define o caminho do arquivo.
            Converte o conteúdo do JSON para um objeto Python (dicionário ou lista) e o retorna.
    1.2.2. Se o arquivo não existir:
            Retorna um dicionário vazio para armazenar novos dados.

2. Interação com o Usuário
2.1. Opção: Adicionar uma nova empresa
    2.1.1. Solicita o nome da empresa e armazena na variável correspondente.
    2.1.2. Solicita o CNPJ e realiza as seguintes validações:
        ✔ Verifica se o CNPJ tem exatamente 14 dígitos.
        ✔ Verifica se o número não é composto apenas por um único dígito repetido.
        ✔ Verifica se todos os caracteres inseridos são números.
    2.1.3. Solicita a categoria do serviço prestado, exibindo as opções disponíveis.
    2.1.4. Gera um código único de registro para a empresa.
    2.1.5. Armazena os dados tratados no objeto Python (dicionário).

2.2. Opção: Sair e fechar o programa
        Encerra a execução e grava os dados no arquivo JSON.

2.3. Opção: Exibir empresas já cadastradas
        Converte o dicionário Python para JSON.
        Carrega os dados em um DataFrame do Pandas para exibição estruturada.

2.4. Se o usuário digitar uma opção inválida
        O programa será encerrado e os dados serão gravados no arquivo JSON antes de finalizar.

3. Salvamento dos Dados
3.1. A função recebe o valor fornecido no parâmetro correspondente.
3.2. Se a instrução for salvar os dados e encerrar o programa:
        Se houver dados a serem salvos, converte o dicionário Python para JSON e grava no arquivo.
        Utiliza formatação (indent=4) para tornar o arquivo JSON mais legível.
3.3. Se não houver dados (y is None), retorna uma mensagem informando que não há nada para salvar.

"""


"""TESTA POSSIVEIS ERROS DE USUARIOS - REQUISITOS FUNCIONAIS E NÃO FUNCIONAIS"""
"""Organizar gits por etapas alteradas"""