import csv
from automobile import Automobile
from noleggio import Noleggio

class Autonoleggio:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile = responsabile

        self.automobili = []
        self.noleggi = []

        self.indice_auto = 1
        self.indice_noleggio = 1

    def carica_file_automobili(self, file_path):
        """Carica le auto dal file"""
        try:
            with ((open(file_path, encoding='utf-8' ) as f)):
                reader = csv.reader(f)
                for line in reader:
                    line = line.strip()
                    field = line.split(',')
                    auto = Automobile(field[0], field[1], field[2], field[3], field[4])
                    self.automobili.append(auto)
                    self.indice_auto +=1
        except FileNotFoundError:
            print("File non trovato")
            return None


    def aggiungi_automobile(self, marca, modello, anno, num_posti):
        """Aggiunge un'automobile nell'autonoleggio: aggiunge solo nel sistema e non aggiorna il file"""
        codice = 'A' + str(self.indice_auto +1)
        new_auto = Automobile(codice, marca, modello, anno, num_posti)
        if new_auto in self.automobili:
            print("Automobile già presente nell'autonoleggio")
            return None
        else:
            self.automobili.append(new_auto)
        return self.automobili


    def automobili_ordinate_per_marca(self):
        """Ordina le automobili per marca in ordine alfabetico"""
        auto_ordinate = sorted(self.automobili, key=lambda a: a.marca)
        return auto_ordinate

    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio"""
        new_noleggio = Noleggio(codice,data,id_automobile,cognome_cliente)
        self.noleggi.append(new_noleggio)


    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""
        # TODO
