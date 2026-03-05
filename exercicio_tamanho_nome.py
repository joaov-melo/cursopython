nome = input('Qual seu primeiro nome: ')
try:
    nome_str=str(nome)
    if len(nome_str) <=4:
        print('Seu nome é curto')
    if len(nome_str) >=5 and len(nome_str)<=6:
        print('Seu nome é normal')
    if len(nome_str) >6:
        print('Seu nome é muito grande')
except:
    print('Você não digitou um nome válido')