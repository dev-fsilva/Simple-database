import json

def OpenArque():
    try: 
        with open('./company.data.json','r') as arquivo_json:
            return json.load(arquivo_json)
    except FileNotFoundError:
        return "Erro"


while True:
    try:
        code_user = int(input("Por favor, digite o seu codigo de registro: "))
        break
    except ValueError:
        print("Digite somente numeros")
        continue

dicionario_de_exemplo = (
    [
        {
            "CodigoUser": "4578561", "Senha": "APE1458","NomeUser": "PALOMA ÁGUIAR","Utimos_resgistro": {
                "Data": "10/02/2025", "Hora":"09:12"
            }
        }
    ]
)

code_verificado = dicionario_de_exemplo[0]["CodigoUser"]
if code_verificado == str(code_user):
    nome_user = dicionario_de_exemplo[0]["NomeUser"]
    import CompanyRegistration
    print("Codigo de registro encontrado")
    print(f"Seja bem vindo {nome_user}")
    print("REDIRENCIONANDO - MAIN")
    CompanyRegistration.CompanyRegistration()
else:
    print("Codigo de registro não encontrado")




