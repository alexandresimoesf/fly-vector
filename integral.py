import numpy as np

class LineInteger():
    def __init__(self):
        self.p = None
        self.q = None
        self.p1 = np.poly1d([-1, 1], variable = 't')
        self.r = None
    

    @property
    def _aceleracao(self):
        pass
    
    @property
    def _velocidade(self):
        pass
    
    @property
    def _desitancia(self):
        pass

