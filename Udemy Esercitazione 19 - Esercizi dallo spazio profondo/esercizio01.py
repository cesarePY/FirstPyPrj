import math
class Astronave:
    def __init__(self, x, y):  # costruttore della classe, riceve coordinate iniziali in entrata (oltre all'oggetto self)
        self.__x = x
        self.__y = y

    def muovi_a(self, dest_x, dest_y):
        self.__x = dest_x
        self.__y = dest_y
        print(f"Nuove coordinate: ({self.__x},{self.__y}).")

    def distanza_da(self, dest_x, dest_y):
        #Ritorna la radice quadrata della somma dei quadrati delle differenze tra le coordinate.
        return math.sqrt(   (dest_x - self.__x)**2 +
                            (dest_y - self.__y)**2
                        )

    def mostra_posizione(self):
        print(f"Posizione X,Y: ({self.__x},{self.__y}).")


espilon = Astronave(0,0)
espilon.mostra_posizione()
espilon.muovi_a(5,5)
espilon.mostra_posizione()
#Ritorna distanza astronave dall'origine (0,0)
distanza = espilon.distanza_da(0,0)
#Arrotonda a 3 cifre decimali
distanza = float("{0:.3f}".format(distanza))


print(f"L'astronave è a {distanza} unità dall'origine.")

