# if / elif      / else
# se / se não se / se não

condicao1 = False
condicao2 = True
condicao3 = True # Apenas a primeira verdadeira é executada
condicao4 = False


if condicao1:
    print('Código para condição 1')
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    # print('Código para condição 4')
    pass # Para deixar espaço vazio sem dar erro
else:
    print('Nenhuma condição foi satisfeita')

if 10 == 10:
    print('Outro if')
print('Fora do if')