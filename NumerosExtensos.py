# pip install num2words

from num2words import num2words
from os import system

while True:
    system('color e')
    system('cls')
    print('-='*20)
    numero = int(input('Digite um numero: '))
    system('cls')
    print('-='*20)
    lingua = input('Qual lingua deseja exibir os numeros? (PT/EN/ES/FR/RU/JA/DE/IT) ').strip().lower()[0:2]
    system('cls')

    if lingua not in ('pt','en','es','fr','ru','ja','de','it'):
        system('color 4')
        print('-='*30)
        print('Opção inválida! Tente novamente!\n')
        system('pause')
        continue

    if lingua == 'pt':
        extenso = num2words(numero, lang='pt-br')
    else:
        extenso = num2words(numero, lang=lingua)

    system('color a')
    print('-='*25)
    print(f'O numero {numero} em {lingua.upper()} por extenso fica "{extenso}"')
    print('-='*25,'\n')

    repetir = ' '
    while repetir not in 'SN':
        repetir = input('Deseja repetir o programa? (S/N) ').strip().upper()[0]
    if repetir == 'N':
        break