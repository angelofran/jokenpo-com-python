# Importações
from random import randint
from time import sleep
# Contadores
contj = contc = conte = 0

# Lista do computador

lista1 = ['Pedra', 'Papel', 'Tesoura']
c = randint(0, 2)

# Deixando tudo mais bonito

print('~' * 45)
print('PEDRA, PAPEL E TESOURA - GAME'.center(45))
print('~' * 45)
# Colocando em loop infinito
while True:
    # Configurando a escolha do usuário

    escolhadojogador = str(input('O que você vai jogar? [Pedra, Papel ou Tesoura] ')).capitalize()

    # Criando as condições
    # Caso o usuário joge pedra

    if escolhadojogador == 'Pedra' and c == 0:
        print(f'O computador jogou {lista1[0]} e você jogou {escolhadojogador}, então é um EMPATE!')
        conte += 1
    if escolhadojogador == 'Pedra' and c == 1:
        print(f'O computador jogou {lista1[1]} e você jogou {escolhadojogador}, então é uma  VITÓRIA para o computador!')
        contc += 1
    if escolhadojogador == 'Pedra' and c == 2:
        print(f'O computador jogou {lista1[2]} e você jogou {escolhadojogador}, então é uma VITÓRIA para você!')
        contj += 1

    # Caso o usuário joge papel
    if escolhadojogador == 'Papael' and c == 0:
        print(f'O computador jogou {lista1[0]} e você jogou {escolhadojogador}, então é uma VITÓRIA para o você')
        contj += 1
    if escolhadojogador == 'Papel' and c == 1:
        print(f'O computador jogou {lista1[1]} e você jogou {escolhadojogador}, então é um EMPATE!')
        conte += 1
    if escolhadojogador == 'Papel' and c == 2:
        print(f'O computador jogou {lista1[2]} e você jogou {escolhadojogador}, então é uma VITÓRIA para o computador!')
        contc += 1
    # Caso o usuário joge tesoura
    if escolhadojogador == 'Tesoura' and c == 0:
        print(f'O computador jogou {lista1[0]} e você jogou {escolhadojogador}, então é uma VITÓRIA para o computador!')
        contc += 1
    if escolhadojogador == 'Tesoura' and c == 1:
        print(f'O computador jogou {lista1[1]} e você jogou {escolhadojogador}, então é uma VOTÓRIA para você!')
        contj += 1
    if escolhadojogador == 'Tesoura' and c == 2:
        print(f'O computador jogou {lista1[2]} e você jogou {escolhadojogador}, então é um EMPATE!')
        conte += 1
    # Perguntando se ainda quer continuar
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp in 'N':
        print('Carregando...')
        sleep(3)
        break
print('~' * 45)
print('Tabela Dos Jogos'.center(45))
print('~' * 45)
print('Nomes        Vitória, Derrotas e Empates')
print('~' * 45)
print(f'Jogador         {contj}         {contc}      {conte}')
print(f'coputador       {contc}         {contj}      {conte}')