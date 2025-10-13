from autonoleggio import Autonoleggio
from datetime import datetime

def menu():
    print("\n--- MENU AUTONOLEGGIO ---")
    print("1. Modifica nome del responsabile dell’autonoleggio")
    print("2. Carica automobili da file")
    print("3. Aggiungi nuova automobile (da tastiera)")
    print("4. Visualizza automobili ordinate per marca")
    print("5. Noleggia automobile")
    print("6. Termina noleggio automobile")
    print("7. Esci")
    return input("Scegli un'opzione >> ")
def main():
    autonoleggio = Autonoleggio("Polito Rent", "Alessandro Visconti")

    while True:
        scelta = menu()

        if scelta == "1":
            nuovo_responsabile = input("Inserisci il nuovo responsabile: ").strip()
            try:
                # con getter/setter imposto il nuovo responsabile
                autonoleggio._responsabile = nuovo_responsabile
                print(f'Responsabile aggiornato: {nuovo_responsabile}')
            except ValueError:
                print("Nuovo responsabile non valido")



        elif scelta == "2":
            while True:
                try:
                    file_path = input("Inserisci il path del file da caricare: ").strip()
                    autonoleggio.carica_file_automobili(file_path) #chiamo la funzione
                    print('File caricato correttamente')
                    break
                except Exception as e: #eventuali errori riscontrati nella funzione
                    print(e)

        elif scelta == "3":
            marca = input("Marca: ")
            modello = input("Modello: ")
            try:
                anno = int(input("Anno di Immatricolazione: ").strip())
                posti = int(input("Numero di posti: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue
            #aggiungo l'oggetto automobile alla classe autonoleggio, tramite la funzione
            #aggiungi_automobile che si trova nel file autonoleggio
            automobile = autonoleggio.aggiungi_automobile(marca, modello, anno, posti)
            print(f"Automobile aggiunta: id_automobile = {automobile.id_automobile}, marca = {automobile.marca}, "
                  f"modello = {automobile.modello}, "
                  f"anno di immatricolazione = {automobile.anno}, numero di posti = {automobile.num_posti}")

        elif scelta == "4":
            automobili_ordinate = autonoleggio.automobili_ordinate_per_marca()
            for a in automobili_ordinate: #nella funzione creo una lista di automobili ordinate
                print(f'- {a}')

        elif scelta == "5":
            id_auto = input("ID automobile: ")
            cognome_cliente = input("Cognome cliente: ")
            data = datetime.now().date() #imposta la data di oggi
            try:
                #aggiungo un nuovo noleggio (oggetto) alla classe noleggio tramite la funzione
                #nuovo_noleggio che si trova nel file autonoleggio
                noleggio = autonoleggio.nuovo_noleggio(data, id_auto, cognome_cliente)
                print(f"Noleggio andato a buon fine: {noleggio}")
            except Exception as e:
                print(e)

        elif scelta == "6":
            id_noleggio = input("ID noleggio da terminare: ")
            try:
                autonoleggio.termina_noleggio(id_noleggio)
                print(f"Noleggio {id_noleggio} terminato con successo.")
            except Exception as e:
                print(e)

        elif scelta == "7":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida!")

if __name__ == "__main__":
    main()
