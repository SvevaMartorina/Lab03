class Noleggio:
    def __init__(self, id_noleggio, data_inizio, id_automobile, cognome_cliente):
        self.id_noleggio = id_noleggio
        self.data_inizio = data_inizio
        self.id_automobile = id_automobile
        self.cognome_cliente = cognome_cliente

    def __repr__(self):
        return (f'{type(self).__name__} '
                f'(id_noleggio={self.id_noleggio},'
                f'data={self.data_inizio},'
                f'id_automobile={self.id_automobile},'
                f'cognome_cliente={self.cognome_cliente})')
