from random import randrange

# class to generate random number
class NumberGenerator:
    
    def generate(self):
        total  = self.jogo * self.qtde
        while total > 0:
            number = randrange(1, self.tipo)

            if (number not in self.res):
                self.res.append(number)
                total -= 1
                
                if len(self.res) is self.jogo:
                    print('\n', sorted(self.res))
                    self.res.clear()


class Printer:
    def printer(any):
        print('-------------------------------------------------',
            '\n Numeros randomicos \n',
            '-------------------------------------------------')


# class to call the right function for the right input from main.py
# this class extends props from NumberGenerator and Printer
class FuncaoLoteria(NumberGenerator, Printer):
    def __init__(self, qtde):
        self.qtde = qtde
        self.jogo = int
        self.tipo = int
        self.res = []
        
        # dictionary to compare the value and do a function
        # use dictionary so you don´t need to use a (if else) chain
        self.loteria = {
            'megasena': self.megasena,
            'lotofacil': self.lotofacil
        }

    def megasena(self):
        self.jogo = 6
        self.tipo = 60
        return self.generate()

    def lotofacil(self):
        self.jogo = 15
        self.tipo = 25
        return self.generate()