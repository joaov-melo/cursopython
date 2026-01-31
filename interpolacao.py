'''

Interpolação básica de strings
s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789)

'''

nome = 'João'
preco = 1000.95897643
# variavel = '%s, o preço é R$%.2f' %(nome, preco)
variavel = f'{nome}, o preço é {preco:.2f}'
print(variavel)


