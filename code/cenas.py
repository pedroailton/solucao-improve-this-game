class Cenas:
    def __init__(self, heroi, util):
        self.heroi = heroi
        self.util = util

    def tutorial(self):

        while True:
            self.util.limparTela()
            print('Você já sabe como chamar o comando Configuraçõs no jogo Exímio?')
            print('[1] Sim. Continuar o jogo.')
            print('[2] Não. Ver tutorial.')
            tecla_lida = lerTecla()
            if tecla_lida == 1:
            
            elif tecla_lida == 2:

            else:
                print('Dígito inválido. Digite novamente, por favor.')
        
        '''
        Demonstração do comando de chamada das configurações, que funcionará a qualquer momento, mesmo que não apareça na tela.
        '''
        print('Antes de começar, é importante que você saiba abrir as Configurações.')
        print('Ela estará disponível a qualquer momento pressionando o botão')
        print('Abrir Configurações')

    def cena1(self):
        '''
        Entrando na vila, após seguir as pegadas dO Grande
        '''
    def cena2(self):
        '''
        Seguindo pista do velho pescador, conhecendo uma costureira de crochê
        '''
    def cena3(self):
        '''
        Batalha contra os Lacaios dO Grande, que fizeram de refém a costureira. Tumulto na cidade. Mensagem à rainha, informando a localização do fétuo, seu filho.
        '''
    def batalha_final(self):
        '''
        Achando o grande, conversando e iniciando uma batalha. Surge a rainha junto da comitiva real à vila, assitindo agora a batalha.
        '''
