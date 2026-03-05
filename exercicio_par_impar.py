numero = input('Digite um número inteiro: ')
try:
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print('O número é par')
    if numero_int % 2 != 0:
        print('O número é ímpar')
except:
    print('Você não digitou um número inteiro')
