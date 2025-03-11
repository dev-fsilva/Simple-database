tentativas_login = 3
while True:
    try:
        code_user = int(input("Por favor, digite o seu codigo de registro: "))
    except ValueError:
        print("Digite somente numeros")
        continue
    dicionario_de_exemplo = (
        [
            {
                "CodigoUser": "22", "Senha": "APE1458","NomeUser": "PALOMA ÁGUIAR","Utimos_resgistro": {
                    "Data": "10/02/2025", "Hora":"09:12"
                }
            }
        ]
    )
    code_verificado = dicionario_de_exemplo[0]["CodigoUser"]
    if code_verificado == str(code_user):
        nome_user = dicionario_de_exemplo[0]["NomeUser"]
        print("Codigo de registro encontrado")
        print(f"Seja bem vindo {nome_user}")
        print("REDIRENCIONANDO - MAIN")
        import CompanyRegistration
        CompanyRegistration.CompanyRegistration()
    else:
        print("Codigo de registro não encontrado")
        tentou = int(input(f"Tenta novamente?\nTENTATIVAS({tentativas_login})\n1-Sim\n2-Não\n>>"))
        if tentou == 1 and tentativas_login > 0 and tentativas_login <= 3:
            entativas_login -= 1
        elif tentou == 2:
            print("Até mais!!!")
            break
        elif tentou > 2:
            print("Numero não legivel")
            continue
        else:
            print("Não a mais tentativas disponiveis, tente mais tarde")
            break
            

"""
1. Difinindo uma função para receber o codigo digitado e validade se foi digitado somente numeros
2. Pego o codigo cadastrado anteriormente se existe
3. Codigo validado eu o redireciono a pagina a proxima pagina
"""


