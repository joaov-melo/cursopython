hora = input('Digite a hora atual (ignore os minutos): ')
try:
    hora_int = int(hora) 
    if hora_int >=0<=11:
        print('Bom dia')
    if hora_int >=12<=17:
        print('Boa tarde')
    if hora_int >= 18<=23:
        print('Boa noite')
except:
    print('Você não digitou uma hora válida')