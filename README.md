# CamposAguado_Algoritmo_de_Dijkstra

# Simulador del Algoritmo de Dijkstra (Consola + Visualización Gráfica)

Este proyecto implementa el **Algoritmo de Dijkstra** en Python, simulando paso a paso en consola el proceso de búsqueda del camino más corto, y mostrando una visualización gráfica del resultado final utilizando `NetworkX` y `Matplotlib`.

---------------------------------------------------------------------------------------------

## Parte Teórica

### ¿Qué es?

El **Algoritmo de Dijkstra** es una técnica de búsqueda utilizada para encontrar el **camino más corto** entre un nodo origen y los demás nodos de un grafocomo encontrar el camino más rápido en un mapa, comprobando y actualizando las distancias paso a paso. Fue propuesto por el científico holandés **Edsger Dijkstra** en 1956. 

----------------------------------------------------------------------------------------------

### ¿Para qué sirve?

Dijkstra se usa principalmente en:
- **Redes**: encontrar rutas óptimas para transmitir datos.
- **Mapas**: calcular rutas más cortas entre dos ubicaciones.
- **Planificación**: optimizar tiempos y recursos.
- **Videojuegos**: navegación de personajes.

----------------------------------------------------------------------------------------------

### ¿Cómo se implementa en el mundo?

- **Google Maps y Waze**: para calcular rutas más rápidas evitando tráfico.
- **Sistemas de logística**: para optimizar recorridos de entrega.
- **Telecomunicaciones**: elegir el canal más rápido para la transmisión de datos.
- **Industria de manufactura**: para rutas óptimas de producción y materiales.

----------------------------------------------------------------------------------------------

### ¿Cómo lo implementaría en mi vida?

En la vida cotidiana, Dijkstra puede aplicarse a la **organización personal**. Por ejemplo:
- Planificar rutas más eficientes al ir a la escuela o trabajo.
- Organizar actividades optimizando tiempos y desplazamientos.

----------------------------------------------------------------------------------------------

### ¿Cómo lo implementaría en mi trabajo o en mi trabajo de ensueño?

**Como futura ingeniera que se desenvuelve en una empresa de suplementos alimenticios**, podría aplicar el algoritmo de Dijkstra para:

- **Optimizar rutas de distribución de productos** entre almacenes, puntos de venta y clientes.
- **Mejorar procesos logísticos internos**, minimizando tiempos entre estaciones de producción.
- **Modelar una red de transporte y suministro**, reduciendo costos y tiempos de entrega.

----------------------------------------------------------------------------------------------

## Funcionamiento del Algoritmo

1. Se parte desde un nodo inicial con una distancia acumulada de 0.
2. Se visitan todos los nodos vecinos, actualizando la distancia más corta a ellos si se encuentra una mejor ruta.
3. Se repite el proceso hasta visitar todos los nodos o llegar al destino.
4. Se reconstruye el camino más corto a partir de los nodos anteriores almacenados.

El programa:
- Muestra paso a paso cómo visita nodos y actualiza rutas.
- Al final, imprime la ruta más corta y su distancia total.
- Visualiza el grafo con el camino resaltado en rojo.

----------------------------------------------------------------------------------------------

## Librerías utilizadas

| Librería     | Descripción                                                                                           |
|--------------|-------------------------------------------------------------------------------------------------------|
| `heapq`      | Maneja una **cola de prioridad**, esencial para siempre elegir el nodo con menor distancia acumulada. |
| `networkx`   | Permite construir y manipular grafos en Python, y facilita la visualización de redes.                 |
| `matplotlib` | Librería de gráficos que nos permite **dibujar el grafo y el camino más corto** con nodos y aristas.  |

