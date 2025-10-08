class Automobile:
    def __init__(self, id_automobile, marca, modello, anno, num_posti):
        self.id_automobile = id_automobile
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.num_posti = num_posti

    def __repr__(self):
        return (f'{type(self).__name__} '
                f'(id_automobile={self.id_automobile},'
                f'marca={self.marca},'
                f'modello={self.modello},'
                f'AnnoImmatricolazione={self.anno},'
                f'NumeroPosti={self.num_posti})')

