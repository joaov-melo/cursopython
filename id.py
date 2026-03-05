'''
Flag (Bandeira) - Marcar um local
None - Não valor
is e is not - é ou não é (tipo, valor, identidade)
id = identidade
'''
condição = True  
passou_no_if = None

if condição:
    print('Faça algo')
    passou_no_if = True 

else: 
    print('Não faça algo')

if passou_no_if is None:
    print('Não passou no if')
if passou_no_if is not None:
    print('Passou no if')