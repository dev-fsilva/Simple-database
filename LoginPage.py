login_attempts = 3
while True:
    try:
        code_user = int(input("Please enter your access code: "))
    except ValueError:
        print("Enter numbers only!")
        continue
    example_dictionary = (
        [
            {
                "CodeUser": "22", "Senha": "APE1458","NameUser": "PALOMA ÁGUIAR","Last_Registration": {
                    "Date": "10/02/2025", "Time":"09:12"
                }
            }
        ]
    )
    code_verified = example_dictionary[0]["CodeUser"]
    if code_verified == str(code_user):
        noma_user = example_dictionary[0]["NameUser"]
        print("Registration code found!!")
        print(f"Welcome ;-) {noma_user}")
        print("REDIRENCIONANDO - MAIN")
        import CompanyRegistration
        CompanyRegistration.CompanyRegistration()
        break
    else:
        print("Registration code not found")
        tentou = int(input(f"Try again?\nATTEMPTS({login_attempts})\n1-Yes\n2-No\n>>"))
        if tentou == 1 and login_attempts > 0 and login_attempts <= 3:
            login_attempts -= 1
        elif tentou == 2:
            print("Until later!!!")
            break
        elif tentou > 2:
            print("Number not readable")
            continue
        else:
            print("No more attempts available, please try again later")
            break
            

"""
1. Difinindo uma função para receber o codigo digitado e validade se foi digitado somente numeros
2. Pego o codigo cadastrado anteriormente se existe
3. Codigo validado eu o redireciono a pagina a proxima pagina
"""


