import random
import time
import matplotlib.pyplot as plt

def quicksort(n, izq, der):
    i, j = izq, der
    piv = sum(n[izq:der+1]) / (der - izq + 1)

    while i <= j:
        while n[i] < piv:
            i += 1
        while n[j] > piv:
            j -= 1
        if i <= j:
            n[i], n[j] = n[j], n[i]
            i += 1
            j -= 1

    if izq < j:
        quicksort(n, izq, j)
    if i < der:
        quicksort(n, i, der)

tamaños_arreglos = []
tiempos_ejecucion = []

for i in range(0, 100):
    n = random.randint(10, 1000)
    aleatorios = [random.randint(0, 1000) for _ in range(n)]
    print("Lista Desordenada")
    print(aleatorios)
    
    inicio = time.time()
    quicksort(aleatorios, 0, len(aleatorios) - 1)
    fin = time.time()
    tiempo_ejecutado = fin - inicio
    print("Tiempo ejecutado", tiempo_ejecutado)
    
    print("Lista Ordenada")
    print(aleatorios)
    
    tamaños_arreglos.append(len(aleatorios))
    tiempos_ejecucion.append(tiempo_ejecutado)

plt.plot(tiempos_ejecucion)
plt.title("Tiempo de Ejecución vs. Tamaño del Arreglo")
plt.xlabel("Tamaño del Arreglo")
plt.ylabel("Tiempo de Ejecución (segundos)")
plt.grid()
plt.show()



