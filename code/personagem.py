class Personagem:
    """
    A classe Personagem representa um personagem definido pelo jogador, e todas as suas informações.
    """
    def __init__(self, nome, idade, classe, habilidade, vida, item_inicial):
        self.nome = nome
        self.idade = idade
        self.classe = classe
        self.habilidade = habilidade
        self.vida = vida
        self.item_inicial = item_inicial

        self.PERSONAGENS = {
        'Espadachim': {'poder': 'espada', 'vida': 200},
        'Arqueiro': {'poder': 'arco', 'vida': 140},
        'Mago': {'poder': 'magia', 'vida': 100},
        'Lacaio': {'poder': 'garras', 'vida': 100},
        'O Desertor': {'poder': 'magia', 'vida': 1000},
        }

        self.HABILIDADES = {
        'golpe de espada': {'dano': 50, 'poder': 'espada', 'animation': 'golpe_de_espada'},
        'golpe com as mãos': {'dano': 20, 'poder': 'espada', 'animation': 'golpe_com_maos'},
        'atirar flecha': {'dano': 40, 'poder': 'arco', 'animation': 'arco_e_flecha'},
        'lançar magia': {'dano': 45, 'poder': 'espada', 'animation': 'golpe_com_maos'},
        'arranhar': {'dano': 25, 'poder': 'garras', 'animation': 'arranhar'},
        'meteoro': {'dano': 70, 'poder': 'magia', 'animation': 'meteoro'},
        'lançar raio': {'dano': 100, 'poder': 'magia', 'animation': 'raio'},
        }

    def upgrade_vida(self, item_de_cura):
        """
        Aumenta a vida do personagem. O valor padrão de incremento é 10.
        """
        if item_de_cura == 'Poção de cura':
            incremento = 20
        elif item_de_cura == 'Magia de cura':
            incremento = 10
        elif item_de_cura == 'Ataque regenerativo':
            incremento = 5

        self.vida += incremento

        # Print das informações da vida
        print(f'Vida de {self.nome} após upgrade: {self.vida}')

    def downgrade_vida(self, dano):
        """
        Reduz a vida do personagem, garantindo que não fique negativa.
        """
        # Dano sendo aplicado a vida
        self.vida -= dano

        # Garantia de não negatividade
        if self.vida < 0:
            self.vida = 0

        print(f'Vida do herói {self.nome} após downgrade: {self.vida}')

    def __str__(self):
        return f'Personagem: {self.nome}, Idade: {self.idade}, Vida: {self.vida}'
