import tkinter as tk
from tkinter import ttk
from datetime import datetime
from utils.read_data import read_flight_data, read_special_occasions, read_holidays
from utils.preprocess_data import preprocess_flight_data
from utils.graph import FlightGraph
from utils.dijkstra import dijkstra
from utils.price_predictor import predict_price
from utils.predict_occasion import predict_occasion, predict_festive_season

class FlightBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flight Booking")
        self.root.geometry("400x300")

        # Departure City
        self.departure_label = ttk.Label(root, text="Departure City:")
        self.departure_label.grid(row=0, column=0, padx=10, pady=10)
        self.departure_entry = ttk.Entry(root)
        self.departure_entry.grid(row=0, column=1, padx=10, pady=10)

        # Destination City
        self.destination_label = ttk.Label(root, text="Destination City:")
        self.destination_label.grid(row=1, column=0, padx=10, pady=10)
        self.destination_entry = ttk.Entry(root)
        self.destination_entry.grid(row=1, column=1, padx=10, pady=10)

        # Date of Travel
        self.date_label = ttk.Label(root, text="Date of Travel (YYYY-MM-DD):")
        self.date_label.grid(row=2, column=0, padx=10, pady=10)
        self.date_entry = ttk.Entry(root)
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.date_entry.grid(row=2, column=1, padx=10, pady=10)

        # Number of Stops
        self.stops_label = ttk.Label(root, text="Number of Stops:")
        self.stops_label.grid(row=3, column=0, padx=10, pady=10)
        self.stops_entry = ttk.Entry(root)
        self.stops_entry.grid(row=3, column=1, padx=10, pady=10)

        # Predicted Price
        self.predicted_price_label = ttk.Label(root, text="Predicted Price:")
        self.predicted_price_label.grid(row=4, column=0, padx=10, pady=10)
        self.predicted_price_value = tk.StringVar()
        self.predicted_price_entry = ttk.Label(root, textvariable=self.predicted_price_value)
        self.predicted_price_entry.grid(row=4, column=1, padx=10, pady=10)

        # Submit Button
        self.submit_button = ttk.Button(root, text="Submit", command=self.submit)
        self.submit_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def submit(self):
        departure_city = self.departure_entry.get().strip()
        destination_city = self.destination_entry.get().strip()
        date = self.date_entry.get().strip()
        stops = int(self.stops_entry.get().strip())

        # Read flight data
        flight_data = read_flight_data()

        # Preprocess flight data
        preprocessed_data = preprocess_flight_data(flight_data)

        # Create flight graph
        flight_graph = FlightGraph()

        # Populate flight graph using preprocessed_data
        for _, row in preprocessed_data.iterrows():
            dep_city, arr_city, price = row["departure_city"], row["arrival_city"], row["price"]
            flight_graph.add_edge(dep_city, arr_city, price)

        # Predict Special Occasion, Holiday, and Festive Season
        is_special_occasion = predict_occasion(date)
        is_holiday = date in read_holidays()["date"].values
        is_festive_season = predict_festive_season(date)

        # Perform Dijkstra's algorithm
        shortest_path = dijkstra(flight_graph, departure_city)

        # Predict price
        predicted_price = predict_price(flight_graph, departure_city, destination_city, date, stops, is_special_occasion, is_holiday, is_festive_season)

        # Display predicted price
        self.predicted_price_value.set(f"₹{predicted_price:.2f}")

def main():
    root = tk.Tk()
    app = FlightBookingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
