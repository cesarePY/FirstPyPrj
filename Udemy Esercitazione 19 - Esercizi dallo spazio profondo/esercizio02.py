class Pianeta:
    def __init__(self, nome,
                 risorse):  # costruttore della classe, riceve coordinate iniziali in entrata (oltre all'oggetto self)
        self.__nome = nome
        self.__risorse = risorse

    def mostra_nome(self):
        return self.__nome

    def mostra_risorse(self) -> dict:
        return self.__risorse


class Astronave:
    def __init__(self,
                 capacita_carico):  # costruttore della classe, riceve coordinate iniziali in entrata (oltre
        # all'oggetto self)
        self.__capacita_carico = capacita_carico
        self.__carico_attuale = 0
        self.__risorse_raccolte = {}

    def mostra_risorse(self) -> dict:
        return self.__risorse_raccolte

    @classmethod
    def astronave_standard(cls):
        return cls(capacita_carico=150)

    def capacita_rimanente(self) -> int:
        return self.__capacita_carico - self.__carico_attuale

    def __puo_caricare(self, pesorisorsa) -> bool:
        return self.__carico_attuale + pesorisorsa <= self.__capacita_carico

    @staticmethod
    def messaggio_esplorazione(self, nomepianeta):
        return f"Sto esplorando il pianeta {nomepianeta}..."

    def esplora(self, pianeta):
        print()
        print(self.messaggio_esplorazione(self, pianeta.mostra_nome()))

        # Scorre tutte le risorse del pianeta ricevuto in esplorazione
        for risorsa, massa in pianeta.mostra_risorse().items():
            # Se c'è spazio per la massa di risorsa attuale presente sul pianeta
            if self.__puo_caricare(massa):
                # Ottiene l'ammontare già presente in stiva per la risorsa attuale, in caso
                # questa risorsa non sia presente fa escape a 0, e vi somma la massa
                # di risorsa presente sul pianeta.
                self.__risorse_raccolte[risorsa] = self.__risorse_raccolte.get(risorsa, 0) + massa
                # Aumenta il livello di carico a comprendere la nuova massa acquisita
                self.__carico_attuale += massa
                print(f"#Caricato#{pianeta.mostra_nome()}#\033[92m[{risorsa},{massa}]\033[0m>")
            else:
                print(
                    f"Impossibile raccogliere ulteriormente \033[91m[{risorsa},{massa}]\033[0m a causa della capacità "
                    f"di carico.")

        print(F"Risorse a bordo: \033[94m[{self.__risorse_raccolte}]\033[0m")
        print(f"Carico totale: {self.__carico_attuale}")
        print(f"Capacità rimanente: {self.capacita_rimanente()}")
        return 10


#################


# epsilon = Astronave.astronave_standard()

epsilon = Astronave(50)

print(f"Capacità rimanente: {epsilon.capacita_rimanente()}")

mercurio = Pianeta("Mercurio", {"ferro": 2, "silice": 4})
venere = Pianeta("Venere", {"carbone": 10, "alluminio": 1})
terra = Pianeta("Terra", {"ferro": 1, "litio": 10})
marte = Pianeta("Marte", {"ferro": 15, "silice": 1})
giove = Pianeta("Giove", {"idrogeno": 10, "elio": 5})
saturno = Pianeta("Saturno", {"argon": 8, "idrogeno": 3})
urano = Pianeta("Urano", {"idrogeno": 5, "radon": 1})

epsilon.esplora(mercurio)
epsilon.esplora(venere)
epsilon.esplora(terra)
epsilon.esplora(marte)
epsilon.esplora(giove)
epsilon.esplora(saturno)
epsilon.esplora(urano)

print("\n#Carico finale a bordo:")
for myrisorsa, mymassa in epsilon.mostra_risorse().items():
    print(f"\033[94m[{myrisorsa},{mymassa}]\033[0m")
