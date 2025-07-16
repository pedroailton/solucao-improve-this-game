import msvcrt
import os

class Util:
    def lertecla(self):
        self.tecla_lida = msvcrt.getch().decode()
        return self.tecla_lida
    
    def limparTela(self):
        self.os.system('cls' if os.name == 'nt' else 'clear')