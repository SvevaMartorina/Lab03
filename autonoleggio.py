import csv
from automobile import Automobile
from noleggio import Noleggio

class Autonoleggio:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self._responsabile = responsabile

        self.automobili = [] #creo lista in cui inserirò le automobili
        self.noleggi = [] #creo lista in cui inserirò i noleggi

        self.indice_auto = 1
        self.indice_noleggio = 1

#tramite le funzioni getter e setter posso modificare il valore responsabile
    @property #getter
    def responsabile(self):
        return self._responsabile
    @responsabile.setter #setter
    def responsabile(self, valore):
        if valore != "":
            self._responsabile = valore
        else:
            raise ValueError("Nome non valido")



    def carica_file_automobili(self, file_path):
        """Carica le auto dal file"""
        try:
            with open(file_path, encoding='utf-8' ) as f:
                reader = csv.reader(f)
                for field in reader:
                    if len(field) != 5: #se i campi non sono 5 la riga non è valida
                        print(f'Riga non valida: {field}')
                        continue
                    codice = field[0]
                    #carico l'oggetto auto nella classe Automobile
                    auto = Automobile(field[0], field[1], field[2], field[3], field[4])
                    self.automobili.append(auto)
                    self.indice_auto += 1
        except FileNotFoundError:
            print("File non trovato")
            return None


    def aggiungi_automobile(self, marca, modello, anno, num_posti):
        """Aggiunge un'automobile nell'autonoleggio: aggiunge solo nel sistema e non aggiorna il file"""
        codice = 'A' + str(self.indice_auto)
        new_auto = Automobile(codice, marca, modello, anno, num_posti)
        # itero nella lista di impiegati e verifico che il codice dell'auto non sia già presente
        for auto in self.automobili:
            if auto.id_automobile == codice:
                raise Exception ("Automobile già presente nell'autonoleggio")
        #se passo i controlli sul codice posso aggiungere la nuova auto alla lista
        self.automobili.append(new_auto)
        self.indice_auto += 1

        return new_auto



    def automobili_ordinate_per_marca(self):
        """Ordina le automobili per marca in ordine alfabetico"""
        auto_ordinate = sorted(self.automobili, key=lambda a: a.marca)
        return auto_ordinate

    def nuovo_noleggio(self, data_inizio, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio"""
        auto_esiste = False
        for auto in self.automobili: #itero sulle auto presenti nella lista
            if auto.id_automobile == id_automobile: #verifico che l'auto scelta sia presente
                auto_esiste = True
        if not auto_esiste:
            raise Exception ("Automobile non trovata")

        for n in self.noleggi: #itero sui noleggi e verifico che l'automobile sia disponibile
            if n.id_automobile == id_automobile:
                raise Exception('automobile già noleggiata')

        id_noleggio = 'N' + str(self.indice_noleggio)
        #aggiungo l'oggetto noleggio alla classe Noleggio
        new_noleggio = Noleggio(id_noleggio,data_inizio, id_automobile,cognome_cliente)
        self.noleggi.append(new_noleggio)
        self.indice_noleggio +=1
        return new_noleggio


    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""
        da_rimuovere = False
        for i,n in enumerate(self.noleggi):
            if n.id_noleggio == id_noleggio:
                self.noleggi.pop(i) #rimuovo la lista dalla lista di liste
                da_rimuovere = True
        if not da_rimuovere:
            raise Exception("ID noleggio non trovato")

        return self.noleggi
