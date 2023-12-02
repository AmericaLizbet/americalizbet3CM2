import heapq
import timeit
import matplotlib.pyplot as plt
import networkx as nx


class Graph: 
    #Constructor de la clase
    def __init__(self):
        self.grafo = {}  #Diccionario para almacenar la estructura del grafo

    def add_vertex(self, vertice):     #Funcion que agrega un vertice al grafo
        if vertice not in self.grafo:  #Verifica si el vertice ya existe
            self.grafo[vertice] = {}   #Si no lo agrega como clave (vacio) al diccionario

    def add_edge(self, inicio, fin, peso):               #Funcion que agrega una arista al grafo
        if inicio in self.grafo and fin in self.grafo:   #Verifica si el vertice ya existe
            self.grafo[inicio][fin] = peso               #Este método agrega una arista ponderada entre dos vértices del grafo siempre y cuanto existan, asi mismo agrega el peso de la arista al diccionario. 

        else:
            print("¡Los vertices no existen!")

    def imprimir_grafo(self):
        for vertice, vecinos in self.grafo.items():
            print(f"Vertice {vertice}: {vecinos}")
    
    def visualizar_grafo(self):
        G = nx.DiGraph()
        for inicio, vecinos in self.grafo.items():
            for fin, peso in vecinos.items():
                G.add_edge(inicio, fin, weight=peso)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=700, node_color="pink", font_size=8, font_color="purple", font_weight="bold", arrowsize=10)
        etiquetas_aristas = {(inicio, fin): peso for inicio, vecinos in self.grafo.items() for fin, peso in vecinos.items()}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas_aristas, font_color="red")


        plt.show()


#Implementar el metodo pedido en la practica
def dijkstra(grafo, vertice_inicio):
    distancias = {nodo: float('infinity') for nodo in grafo}
    distancias[vertice_inicio] = 0
    cola = [(0, vertice_inicio)]

    while cola:
        distancia_actual, nodo_actual = heapq.heappop(cola)
        if distancia_actual > distancias[nodo_actual]:
            continue
        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_actual + peso
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heapq.heappush(cola, (distancia, vecino))

    return distancias

# Ejemplo de uso
grafo = Graph()

grafo.add_vertex("A")
grafo.add_vertex("B")
grafo.add_vertex("C")
grafo.add_vertex("D")
grafo.add_vertex("E")

grafo.add_edge("A", "B", 4)
grafo.add_edge("A", "C", 2)
grafo.add_edge("B", "C", 5)
grafo.add_edge("C", "D", 3)
grafo.add_edge("D", "E", 1)
grafo.add_edge("E", "A", 4)





# Imprimir el grafo
grafo.imprimir_grafo()

# Calcular caminos mínimos desde un vértice de inicio
inicio = timeit.default_timer()
start_vertex = 'A'
resultado = dijkstra(grafo.grafo, start_vertex)

print(f"Distancias más cortas desde el nodo {start_vertex}: {resultado}")
fin = timeit.default_timer()
tiempo_ejecutado = fin - inicio
print("Tiempo ejecutado", tiempo_ejecutado)

# Visualizar el grafo
grafo.visualizar_grafo()


