# Operadores lógicos and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia toda a expressão como verdadeira
# Se um valor for considerado verdadeiro, a expressão será avaliada naquele valor
# São considerados falsy (que eu já vi) 0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor

# Sistema de senha
entrada = input('[E]ntrar [S]air: ')
if entrada == 'E' or entrada == 'e': 
    senha_digitada = input('Senha: ')
elif entrada == 'S' or entrada == 's':
    print('Sair')
else:
    print('Você não digitou nem [E]ntrar e nem [S]air')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
elif (entrada == 'E' or entrada == 'e') and senha_digitada != senha_permitida:
    print('Senha incorreta')

# Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)    