# randomgraphics.py

import random
import matplotlib.pyplot as plt

class Diegraphic:
    """"Clase para graficar lanzamientos con uno o m�s dados"""

    def __init__(self, nlanz=0, ndies=1, nfaces=6):
        self.ndies = ndies
        self.nfaces = nfaces
        self.nlanz = nlanz

        posibles_resultados = []
        frecuencias = []
        resultado = 0

        for i in range(ndies*nfaces):
            posibles_resultados.append(i+1)
            frecuencias.append(0)
        #print(posibles_resultados)
        #print(frecuencias)

        for k in range(nlanz):
            resultado = 0
            for m in range(ndies):
                resultado += random.randrange(1, nfaces + 1)
                #print(resultado, end=' ')
            frecuencias[resultado - 1] += 1

        x = posibles_resultados
        y = frecuencias

        plt.plot(x, y, color='r')
        plt.scatter(x, y, color='b')
        plt.grid()
        plt.show()

