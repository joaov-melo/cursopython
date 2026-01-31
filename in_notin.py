# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3
#  J o ã o
# -4-3-2-1

# nome = 'João'
# print(nome[2])
# print(nome[-2])
# print('oão' in nome)
# print('z' in nome)
# print(10 * '-')
# print('z' not in nome)
# print('oão' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')