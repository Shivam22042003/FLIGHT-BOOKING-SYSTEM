from collections import defaultdict


class FlightGraph:
    def __init__(self):
        self.graph = defaultdict(dict)

    def add_edge(self, departure_city, arrival_city, price):
        self.graph[departure_city][arrival_city] = price

    def get_price(self, departure_city, arrival_city):
        return self.graph[departure_city].get(arrival_city, float('inf'))
