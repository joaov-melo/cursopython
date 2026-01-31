# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

# Exemplo
print(not True)
print(not 0)

# Sistema de senha
senha = input('Senha: ')
senha_permitida = '123456'
if not senha:
    print('Você não digitou nada')
elif senha == senha_permitida:
    print('Você entrou')
else:
    print('Senha incorreta')