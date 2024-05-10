def predict_price(flight_graph, source, destination, date, stops, special_occasion, holiday_indicator, festive_season_indicator):
    base_price = flight_graph.get_price(source, destination)
    
    # Check if there's a direct flight between the cities
    if base_price == float('inf'):
        return "No direct flight available"
    
    # Adjust price based on special occasion, holiday, and festive season
    if special_occasion or holiday_indicator or festive_season_indicator:
        adjusted_price = base_price * 1.2  
    else:
        adjusted_price = base_price

    # Adjust price based on number of stops
    adjusted_price += stops * 100

    return adjusted_price
