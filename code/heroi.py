from personagem import Personagem
import msvcrt

class Heroi(Personagem):
    def __init__(self):

        # Conjunto de falas do herói, com todas as opções, em dicionário.
        self.SOZINHO = {'fala1': {'opcao1' : '', 'opcao2': ''}, 'fala2': '', 'fala3': ''}
        self.COMPESCADOR = {'fala1': '', 'fala2': '', 'fala3': ''}
        self.COMCOSTUREIRA = {'fala1': '', 'fala2': '', 'fala3': ''}
        self.COMLACAIO = {'fala1': '', 'fala2': '', 'fala3': ''}
        self.COMVILAO = {'fala1': '', 'fala2': '', 'fala3': ''}

    # Sistema de procura de fala no dicionário e impressão por busca
    def conversar(self, interlocutor, fala, opcao):
        print('EXIMIO:')
        if interlocutor == 'sozinho':
            print(f'- {self.SOZINHO[fala][opcao]}')
        elif interlocutor == 'pescador':
            print(f'- {self.COMPESCADOR[fala][opcao]}')
        elif interlocutor == 'costureira':
            print(f'- {self.COMCOSTUREIRA[fala][opcao]}')
        elif interlocutor == 'lacaio':
            print(f'- {self.COMLACAIO[fala][opcao]}')
        elif interlocutor == 'vilao':
            print(f'- {self.COMVILAO[fala][opcao]}')
        

    def historico(self):
        '''
        Exibe o histórico de atividade do personagem
        '''