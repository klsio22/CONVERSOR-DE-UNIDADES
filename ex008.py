print('\n' + '-#-' * 10 + ' CONVERSOR DE UNIDADES ' + '-#-' * 10 + '\n')

print('ATENÇÃO: Escreva um valor em metros para converte-lo para respectivas unidades:')
print('cm,mm,dm,dam,hm,km\n')

m = float(input('Digite o valor em metros: '))

print('--'*23)
print('Digite 1 para converter para km(kilometro)')
print('--'*23)
print('Digite 2 para converter para hm(hectomentro)')
print('--'*23)
print('Digite 3 para converter para dam(decametro)')
print('--'*23)
print('Digite 4 para converter para dm(decimetro)')
print('--'*23)
print('Digite 5 para converter para cm (centimetros)')
print('--'*23)
print('Digite 6 para converter para mm (milimetros)')
print('--'*23)

medida = float(input('\nUnidade: '))
print('\n')
if medida == 1:
    print('A medida em {}m corresponde a'.format(m))
    print('{}km\n'.format(m/1000))
elif medida == 2:
    print('A medida em {}m corresponde a'.format(m))
    print('{}hm\n'.format(m/100))
elif medida == 3:
    print('A medida em {}m corresponde a'.format(m))
    print('{}dam\n'.format(m/10))
elif medida == 4:
    print('A medida em {}m corresponde a'.format(m))
    print('{}dm\n'.format(m*10))
elif medida == 5:
    print('A medida em {}m corresponde a'.format(m))
    print('{}cm\n'.format(m*100))
elif medida == 6:
    print('A medida em {}m corresponde a'.format(m))
    print('{}mm\n'.format(m*1000))
else:
    print('Tecla invalida\n')
