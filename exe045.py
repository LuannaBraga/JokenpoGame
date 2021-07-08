from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA ''')
jogador = int(input('Qual é sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('Computador Jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador ==0:# computador jogou pedra
    if jogador==0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:# computador jogou papel
    if jogador==0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:  # computador jogou tesoura
        if jogador == 0:
            print('EMPATE')
        elif jogador == 1:
            print('JOGADOR VENCE')
        elif jogador == 2:
            print('COMPUTADOR VENCE!')
        else:
            print('JOGADA INVÁLIDA!')



