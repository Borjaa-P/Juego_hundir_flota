import numpy as np
import Tablero

class Juego:
    tablero_jugador = ""
    tablero_maquina = ""
    vidas = 20
    turno= " " # Lo voy a cambiar desde la funcion comienzo

    # iniciar crear tableros de los dos jugadores, barcos, jugadores.
    def inicializar(self):
        self.tablero_jugador = Tablero.Tablero("jugador")
        self.tablero_maquina = Tablero.Tablero("maquina")
        self.tablero_jugador.imprimir()
        self.tablero_maquina.imprimir()

    def añadir_barcos(self):
        self.tablero_jugador.crear_barco()
        self.tablero_maquina.crear_barco()

    def batalla(self):#


        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            try:
            x, y = input("¿Que posicion quieres atacar?").split()
            x = int(x)
            y = int(y)
            if tablero[x, y] == "O":
                tablero[x, y] = "X"
            elif tablero[x, y] == " ":
                tablero[x, y] = "~"

            print(tablero)

            continuar = input("¿Quieres atacar otra vez? (S/N)")
            if continuar == "N" or continuar == "n":
                break

        except:
            print("Formato no valido")

    print(tablero)
# -----------------------------------------------


if __name__ == "__main__" :
    juego = Juego()
    juego.inicializar()



