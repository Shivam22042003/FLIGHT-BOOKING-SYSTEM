import pandas as pd

def preprocess_flight_data(flight_data):
    relevant_columns = ["departure_city", "arrival_city", "date", "stops", "price"]
    preprocessed_data = flight_data[relevant_columns]

    return preprocessed_data
