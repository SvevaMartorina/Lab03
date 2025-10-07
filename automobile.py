class Automobile:
    def __init__(self, codice, marca, modello, immatricolazione, posti):
        self.codice = codice
        self.marca = marca
        self.modello = modello
        self.anno = 0
        self.num_posti = 0

    def __repr__(self):
        return (f'{type(self).__name__} '
                f'(codice={self.codice},'
                f'marca={self.marca},'
                f'modello={self.modello},'
                f'AnnoImmatricolazione={self.anno},'
                f'NumeroPosti={self.num_posti})')

