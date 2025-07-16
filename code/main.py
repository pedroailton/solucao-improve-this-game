from personagem import Personagem
from vilao import Vilao
from cenas import Cenas
from util import Util
from configuracoes import PERSONAGENS, HABILIDADES
import msvcrt
import time


"""
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
    """

def introducao():

    # Início
    print('INICIAR JORNADA')
    input('Pressione qualquer tecla para começar')

    # Escolha do Herói
    print('Escolher Exímio\n')
    print('[1] Espadachim')
    print('[2] Arqueiro')
    print('[3] Mago\n')
    escolha_heroi = input('Digite sua escolha: ').split()
    if escolha_heroi == '1':
        heroi = Personagem(PERSONAGENS['Espadachim']['poder'], HABILIDADES['Espadachim']['vida'])
    elif escolha_heroi == '2':
        heroi = Personagem(PERSONAGENS['Arqueiro']['poder'], HABILIDADES['Arqueiro']['vida'])
    elif escolha_heroi == '3':
        heroi = Personagem(PERSONAGENS['Mago']['poder'], HABILIDADES['Mago']['vida'])

    # História Introdutória do Jogo
    print('Há muito tempo, quando as esperanças do Reino quase já se dissipavam, nasceu uma última chance…\nUm feto, amaldiçoado por forças sombrias, mas destinado a restaurar a luz ao trono da Rainha Aurora."\n"A ele, deu-se o nome de Exímio — o Prometido, carregado pelos braços do grupo Sigma… os heróis de maior coragem, honra e fé do reino.')

    '''
    [Imagens de uma caravana de heróis cruzando desertos, rios e florestas com o feto em uma cúpula mágica.]
    '''

    print('Sua missão era clara: trazer o Exímio de volta à capital, onde seu toque quebraria a maldição que assolava o reino.\nMas… no limiar da vitória, às portas da cidade, encontraram a ruína.')

    '''
    [Aparece O Grande – uma figura imensa, envolta por um manto negro que ondula mesmo sem vento. Seus olhos brilham como brasas.]
    '''

    print('O Grande — mago ancestral da raça dos gigantes — emboscou Sigma com um poder além da compreensão.\nA batalha foi curta. Cruel. Injusta.')

    '''
    [Explosão de luz negra. Gritos abafados. Os corpos dos heróis caem. A cúpula mágica permanece, intacta.]
    '''

    print("Mas o feto… sobreviveu.")

    '''
    [Câmera foca na energia negra se esvaindo, e o braço de O Grande caindo no chão.]
    '''

    print("Mesmo vitorioso, O Grande deixou um pedaço de si naquela guerra.\nE fugiu… ferido… escondido entre os aldeões da esquecida Vila de Hein, na vastidão da floresta.")

    '''
    [Silêncio. Imagem do corpo do Exímio, ainda jovem, envolto por luz. A respiração acelera. Seus olhos se abrem, ardendo em chamas azuis. O inferno azulado.]
    '''

    print('Agora… ele desperta.\nNão mais um feto.\nNão mais uma promessa.')

    '''
    [Surge a silhueta do Exímio, empunhando uma arma. Flashs dos membros de Sigma sorrindo para ele em memórias.]
    '''

    print("Mas sim… a vingança feita de carne. O último suspiro de um mundo que se recusa a tombar nas sombras.")

    '''
    [Fade-out. Título surge com música épica:]
    '''

    #Preciso saber como vou colocar o texto editado no terminal: aumentar o tamanho da letra e colocar efeitos

    '''
    O Exímio: A Vingança
    '''
    input('Pressione qualquer tecla')
    time.sleep(3)

    # Incializando a classe Cenas e chamando a cena 1 (método de Cenas)
    util = Util()   # Objeto para acessar a classe Util do arquivo utils.py
    game = Cenas(heroi, util)   # Objeto para acessar a classe Cenas do arquivo cenas.py
    game.tutorial()

# Início do programa
if __name__ == "__main__":
    try:
        introducao()
    except Exception as e:
        print(f'Erro no código: {e}. Corrigir.')
