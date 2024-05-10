from heapq import heappop, heappush

def dijkstra(graph, source):
    distances = {city: float("inf") for city in graph.graph}
    distances[source] = 0
    visited = set()
    pq = [(0, source)]

    while pq:
        dist, current_city = heappop(pq)
        if current_city in visited:
            continue
        visited.add(current_city)

        if current_city not in graph.graph:
            continue

        for neighbor, price in graph.graph[current_city].items():
            new_dist = dist + price
            if new_dist < distances.get(neighbor, float('inf')):
                distances[neighbor] = new_dist
                heappush(pq, (new_dist, neighbor))

    return distances
