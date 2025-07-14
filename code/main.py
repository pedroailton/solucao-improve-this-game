from personagem import Personagem
from vilao import Vilao
from configuracoes import *

def main():
    # Criando personagens e vilões
    

    heroi = Personagem('Link', 30, 100)
    npc = Personagem('Zelda', 28, 80)
    vilao = Vilao('Ganon', 45, 120, 'Alta')

    # Mostrando personagens
    print(heroi)
    print(npc)
    print(vilao)

    # Vilão ataca o herói
    vilao.ataque(heroi)

    # Melhorando a vida do herói
    heroi.upgrade_vida(20)
    print(f'{heroi.nome} após upgrade de vida: {heroi.vida}')

    # Mudando nome do NPC
    npc.update_nome('Princesa Zelda')
    print(f'Nome atualizado: {npc.nome}')

def menuInicial():

    # História Introdutória do Jogo

    print('')

    # Escolha do Herói
    print('[1] Espadachim')
    print('[2] Arqueiro')
    print('[3] Mago')
    escolha_heroi = input('Digite sua escolha: ').split()
    if escolha_heroi == '1':
        heroi = Personagem(PERSONAGENS['Espadachim']['poder'], PERSONAGENS['Espadachim']['vida'])
    elif escolha_heroi == '2':
        heroi = Personagem(PERSONAGENS['Arqueiro']['poder'], PERSONAGENS['Arqueiro']['vida'])
    elif escolha_heroi == '3':
        heroi = Personagem(PERSONAGENS['Mago']['poder'], PERSONAGENS['Mago']['vida'])

# Início do programa
if __name__ == "__main__":
    menuInicial()
