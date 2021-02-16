import numpy as np


class Tablero:
    filas = 10
    columnas = 10

    tablero = np.full((filas, columnas), ' ')

    def __init__(self, id):
        self.id = id

    def imprimir(self):
        print(self.tablero)

    #def crear_barco(self):
        # Ejercicio 5, colocar barco aleatorio
        x = np.random.randint(10)
        y = np.random.randint(10)
 b
        nrows, ncol = tablero.shape
        # Comprobamps si no hay ya un barco
        if tablero[x, y] != "O":
            # Genereamos un sentido aleatorio
            sentido = random.choice(["Norte", "Sur", "Este", "Oeste"])
            if (sentido == "Norte"):
                if x >= 3:  # Esto sirve para comprobar que hay espacio en el norte para noner el barco, es 3 ya que el tamaño del baroc es 4(0,3).
                    # Haria falta comprobar que en las posiciones que se va a poner el barco no hay otro barco. Aqui no lo hacemos
                    tablero[x, y] = "O"
                    tablero[x - 1, y] = "O"
                    tablero[x - 2, y] = "O"
                    tablero[x - 3, y] = "O"
                    return

            elif (sentido == "Sur"):
                if x <= (nrows - 4):  # Esto sirve para comprobar que hay espacio en el norte para noner el barco, es 3 ya que el tamaño del baroc es 4(0,3).
                    # Haria falta comprobar que en las posiciones que se va a poner el barco no hya otro barco. Aqui no lo hacemos
                    tablero[x, y] = "O"
                    tablero[x + 1, y] = "O"
                    tablero[x + 2, y] = "O"
                    tablero[x + 3, y] = "O"
                    return

            elif (sentido == "Este"):
                if y <= (ncol - 4):  # Esto sirve para comprobar que hay espacio en el norte para noner el barco, es 3 ya que el tamaño del baroc es 4(0,3).
                    # Haria falta comprobar que en las posiciones que se va a poner el barco no hya otro barco. Aqui no lo hacemos
                    tablero[x, y] = "O"
                    tablero[x, y + 1] = "O"
                    tablero[x, y + 2] = "O"
                    tablero[x, y + 3] = "O"
                    return
            elif (sentido == "Oeste"):
                if y >= 3:  # Esto sirve para comprobar que hay espacio en el norte para noner el barco, es 3 ya que el tamaño del baroc es 4(0,3).
                    # Haria falta comprobar que en las posiciones que se va a poner el barco no hya otro barco. Aqui no lo hacemos
                    tablero[x, y] = "O"
                    tablero[x, y - 1] = "O"
                    tablero[x, y - 2] = "O"
                    tablero[x, y - 3] = "O"
                    return
        crear_barco()

        def crear_barcos(self) # Barcos estaticos, crear diccionario

        #4 posiciones
         tab_maq[3:4:,5:9] = "h"
        # Barco 3 posiciones

        tab_maq[1:2:,3:6] = "x"
        tab_maq[4:5:,1:4] = "x"

        #Barco 2 posiciones
        tab_maq[7:9:,0:1] = "y"
        tab_maq[:2:,8:9] = "y"
        tab_maq[7:9:,8:9] = "y"

        #Barco 1 posicion
        tab_maq[3,3] = "O"
        tab_maq[6,2] = "O"
        tab_maq[9,4] = "O"
        tab_maq[5,7] = 'O'

        # Barco 4 posiciones
        tablero[1:2:,3:7] = "O"
        #Barcos 3 posiciones
        tablero[7:8:,6:9] = "O"
        tablero[5:6:,1:4] = "O"
        #Barcos 2 posiciones
        tablero[1:3:,8:9] = "O"
        tablero[1:3:,8:9] = "O"
        tablero[7:9:,3:4] = "O"
        #Barco 1 posicion
        tablero[2,2] = "O"
        tablero[5,7] = "O"
        tablero[9,5] = "O"
        tablero[3,4] = 'O'