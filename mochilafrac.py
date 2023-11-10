import random
import time
import matplotlib.pyplot as plt

def mochilafrac(capacidad, objetos):
    
    objetos.sort(key=lambda x: x[0] / x[1], reverse=True)
    total_objetos = 0
    mochila = []

    for valor, peso in objetos:
        if capacidad >= peso:
            mochila.append((valor, peso))
            total_objetos += valor
            capacidad -= peso
        else:
            fracc = capacidad / peso
            mochila.append((valor * fracc, peso * fracc))
            total_objetos += valor * fracc
            break
        
    return total_objetos, mochila

if __name__ == '__main__':

    resultados = []
    tiempos = []

    for i in range(10):
        objetos = []
        for j in range(9): 
            valor = random.randint(1, 10) 
            peso = random.randint(1, 90) 
            objetos.append((valor, peso))
        capacidad = random.randint(10, 100)  

        inicio = time.time()
        total_objetos, mochila = mochilafrac(capacidad, objetos)
        fin = time.time()
        tiempo_ejecutado = fin - inicio

        print(f'{i + 1}: El total de objetos es: {total_objetos} y la mochila quedó {mochila}')
        print("Tiempo ejecutado", tiempo_ejecutado)

        resultados.append(total_objetos)
        tiempos.append(tiempo_ejecutado)

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(range(1, 11), resultados, marker='o')
    plt.xlabel('Ejecución')
    plt.ylabel('Total de Objetos')
    plt.title('Resultados de la Mochila Fraccionaria')

    plt.subplot(1, 2, 2)
    plt.plot(range(1, 11), tiempos, marker='o', color='orange')
    plt.xlabel('Ejecución')
    plt.ylabel('Tiempo de Ejecución (segundos)')
    plt.title('Tiempos de Ejecución')

    plt.tight_layout()
    plt.show()

