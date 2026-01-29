a = 'AAAAAA'
b = 'BBBBBB'
c = 1.1
string = 'x={nome2} y={nome1} z={nome2} w={nome3:.3f}'
formato = string.format(nome1=a, nome2=b, nome3=c)  

print(formato) 