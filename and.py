# Operadores lógicos and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras
# Se um valor for considerado falso, a expressão inteira será avaliada naquele valor
# São considerados falsy (que eu já vi)  0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor

# Sistema de senha
entrada = input('[E]ntrar [S]air: ')
if entrada == 'E':
    senha_digitada = input('Senha: ')
elif entrada == 'S':
    print('Sair')
else:
    print('Você não digitou nem [E]ntrar e nem [S]air')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
elif entrada == 'E' and senha_digitada != senha_permitida:
    print('Senha incorreta')

# Avaliação de curto circuito
print(True and False and True)
print(True and 0 and True)