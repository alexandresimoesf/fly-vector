import numpy as np

class LineInteger():
    def __init__(self):
        '''Cálculo de parametrização'''
        self.p1, self.p2 = [1, 3, -2], [2, -1, 3]

        self.vetoresRo = []
        self.vetoresR1 = []
        for p in range(len(self.p1)):
            value1 = 1 * self.p1[p]
            if ((self.p1[p] > 0)):
                value2 = "-t" + str(self.p1[p])
            else:
                value2 = "+t" + str(self.p1[p] * (-1))
            if (value1 > 0):
                esq = value2 + "+" + str(value1)
            else:
                esq = value2 + "" + str(value1)
            if (p2[p] < 0):
                value11 = "-t"
            else:
                value11 = "+t" + str(self.p2[p])
            self.vetoresRo.append(esq)
            self.vetoresR1.append(value11)

        print(self.vetoresRo)
        print(self.vetoresR1)


    @staticmethod
    def _aceleracao(self):
        pass
    
    @staticmethod
    def _velocidade(self):
        '''Recebe do método aceleração para transformar em vetor velocidade'''
        pass
    
    @staticmethod
    def _distancia(self):
        '''Recebe do método velocidade para transformar em vetor posição'''
        pass


