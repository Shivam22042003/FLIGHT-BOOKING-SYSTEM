import pandas as pd

def read_flight_data():
    return pd.read_csv("data/flights.csv")

def read_special_occasions():
    return pd.read_csv("data/special_occasions.csv")

def read_holidays():
    return pd.read_csv("data/holidays.csv")
