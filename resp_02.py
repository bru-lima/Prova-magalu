numero = int(input('Innsira o numero de sua escolha: '))
resto= numero % 2

if numero < 10:
    print(f'O número: {numero} é menor que 10.')
if resto == 0:
     print(f'O número: {numero} é par.')
if numero >= 8 and numero <= 16:
    print(f'O número: {numero} está entre 8 e 16.')
if numero == 51 or numero == 80:
    print(f'O número: {numero} é 51 ou 80.')