#Algoritmo de Dijkstra
#Es un método para encontrar el camino más corto desde un nodo origen a todos los otros nodos en un grafo ponderado 
#(con pesos en las aristas) sin pesos negativos
#Funcionamiento: 
# Se parte desde un nodo inicial.
# Se asigna una distancia de 0 al nodo de inicio y ∞ (infinito) a todos los demás.
# Se visita el nodo con la distancia más baja aún no visitado.
# Se actualizan las distancias a los nodos vecinos si se encuentra un camino más corto.
# Se marca el nodo como "visitado".
# Se repite el proceso hasta visitar todos los nodos o alcanzar el nodo destino.
#Aplicaciones: 
#Gps, redes de comunicación, juegos, optimización de rutas, etc.

#Simulación del algoritmo de Dijkstra

#Librerías necesarias
import heapq #para manejar la cola de prioridad y realizar la búsqueda del camino más corto de manera eficiente
import networkx as nx #para crear y manipular grafos y visualizar el resultado
import matplotlib.pyplot as plt #para graficar el camino más corto encontrado por el algoritmo

#función principal del algoritmo de Dijkstra
def dijkstra(grafo, inicio, fin):
    # Inicialización de distancias y nodos anteriores
    distancias = {nodo: float('inf') for nodo in grafo} #inicializa todas las distancias a infinito
    distancias[inicio] = 0 #la distancia al nodo de inicio es 0
    anteriores = {nodo: None for nodo in grafo} #para reconstruir el camino más corto y almacenar el nodo anterior de cada nodo visitado
    cola = [(0, inicio)] #cola de prioridad para manejar los nodos a visitar, iniciando con el nodo de inicio
    #donde la cola contiene tuplas de (distancia, nodo)

    print(f"\nIniciando Dijkstra desde '{inicio}' hasta '{fin}'\n") #imprime el nodo de inicio y destino

    while cola: #mientras haya nodos en la cola
        distancia_actual, nodo_actual = heapq.heappop(cola) #extrae el nodo con la distancia más baja de la cola y asigna su distancia a distancia_actual y el nodo a nodo_actual
        print(f"Visitando nodo '{nodo_actual}' con distancia acumulada {distancia_actual}") #imprime el nodo actual y su distancia acumulada

        if nodo_actual == fin: #si el nodo actual es el nodo destino
            print("Nodo destino alcanzado.\n") #imprime que se ha alcanzado el nodo destino
            break

        for vecino, peso in grafo[nodo_actual].items(): #para cada vecino del nodo actual y su peso asociado extraido del grafo
            nueva_distancia = distancia_actual + peso #calcula la nueva distancia al vecino sumando la distancia actual y el peso de la arista
            print(f"Vecino '{vecino}' con peso {peso:.2f} → Nueva distancia: {nueva_distancia:.2f}") #imprime el vecino, su peso y la nueva distancia calculada

            if nueva_distancia < distancias[vecino]: #si la nueva distancia es menor que la distancia previamente registrada al vecino
                distancias[vecino] = nueva_distancia #actualiza la distancia al vecino con la nueva distancia
                anteriores[vecino] = nodo_actual #actualiza el nodo anterior del vecino al nodo actual
                heapq.heappush(cola, (nueva_distancia, vecino)) #agrega el vecino a la cola con su nueva distancia para ser visitado posteriormente
                print(f"Actualizado: '{vecino}' ahora tiene distancia {nueva_distancia:.2f}") #imprime que se ha actualizado la distancia del vecino

    # Reconstrucción del camino más corto
    camino = [] #lista para almacenar el camino más corto encontrado
    nodo = fin #inicia el nodo actual como el nodo destino
    while nodo: #mientras haya nodos en el camino
        camino.insert(0, nodo) #inserta el nodo al inicio de la lista del camino
        nodo = anteriores[nodo] #actualiza el nodo actual al nodo anterior del nodo actual para reconstruir el camino hacia atrás

    print("\nRuta más corta encontrada:") 
    print(" ➝ ".join(camino)) #imprime el camino más corto encontrado
    print(f"Distancia total: {distancias[fin]:.2f}") #imprime el camino más corto encontrado y la distancia total

    return camino, distancias[fin] #retorna el camino más corto y la distancia total

#Función para graficar el camino más corto encontrado
def graficar_camino(grafo, camino): #parametros: grafo (diccionario de adyacencia) y camino (lista de nodos en el camino más corto)
    G = nx.Graph() #crea un grafo vacío usando NetworkX

    # Agregar nodos y aristas al grafo
    for nodo, vecinos in grafo.items(): #para cada nodo y sus vecinos en el grafo
        for vecino, peso in vecinos.items(): #para cada vecino y su peso asociado
            G.add_edge(nodo, vecino, weight=round(peso, 2)) #agrega una arista al grafo con el peso redondeado a 2 decimales

    pos = nx.spring_layout(G, seed=42) #posiciones de los nodos para el layout del grafo 
    #spring_layout distribuye los nodos de manera uniforme en un espacio 2D

    # Colores para nodos y aristas
    edge_colors = [] #lista para almacenar los colores de las aristas
    for u, v in G.edges(): #para cada arista (u, v) en el grafo
        if (u in camino and v in camino and abs(camino.index(u) - camino.index(v)) == 1): #si ambos nodos de la arista están en el camino y son adyacentes en el camino
            #.index() devuelve el índice del primer elemento encontrado en la lista
            #abs() devuelve el valor absoluto de la diferencia entre los índices
            edge_colors.append('red') #agrega el color rojo a la lista de colores de aristas
        else: #si la arista no está en el camino o no es adyacente
            edge_colors.append('gray') #agrega el color gris a la lista de colores de aristas

    # Dibujo
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=800) #dibuja los nodos del grafo con color azul claro y tamaño 800
    nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=2) #dibuja las aristas del grafo con los colores definidos y un ancho de 2
    nx.draw_networkx_labels(G, pos, font_weight='bold') #dibuja las etiquetas de los nodos con peso de fuente en negrita
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{d['weight']}" for u, v, d in G.edges(data=True)}) #dibuja las etiquetas de las aristas con sus pesos


    plt.title("Camino más corto usando Dijkstra", fontsize=14)
    plt.axis('off')
    plt.show()


# Grafo
grafo = {
    'A': {'B': 3, 'C': 3},
    'B': {'A': 3, 'D': 3.5, 'E': 2.8},
    'C': {'A': 3, 'E': 2.8, 'F': 3.5},
    'D': {'B': 3.5, 'E': 3.1, 'G': 10},
    'E': {'B': 2.8, 'C': 2.8, 'D': 3.1, 'G': 7},
    'F': {'G': 2.5, 'C': 3.5},
    'G': {'D': 10, 'E': 7, 'F': 2.5}
}

# Ejecutamos el algoritmo
camino, distancia = dijkstra(grafo, 'B', 'F') #nodo de inicio 'B' y nodo destino 'F'

# Mostramos gráficamente el resultado
graficar_camino(grafo, camino) #imprime el camino más corto encontrado en el grafo
