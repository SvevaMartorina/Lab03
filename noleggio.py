class Noleggio:
    def __init__(self, codice, data, id_automobile, cognome_cliente):
        self.codice = codice
        self.data = 0
        self.id_automobile = id_automobile
        self.cognome_cliente = cognome_cliente

    def __repr__(self):
        return (f'{type(self).__name__} '
                f'(codice={self.codice},'
                f'data={self.data},'
                f'id_automobile={self.id_automobile},'
                f'cognome_cliente={self.cognome_cliente})')
