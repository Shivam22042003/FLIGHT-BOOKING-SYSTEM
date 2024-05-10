import pandas as pd
from utils.read_data import read_special_occasions

def predict_occasion(date):
    special_occasions = read_special_occasions()

    if date in special_occasions["date"].values:
        return True
    else:
        return False

def predict_festive_season(date):

    christmas_range = pd.date_range(start='2024-12-20', end='2024-12-31')
    new_year_range = pd.date_range(start='2024-12-01', end='2025-01-05')

    if date in christmas_range or date in new_year_range:
        return True
    else:
        return False
