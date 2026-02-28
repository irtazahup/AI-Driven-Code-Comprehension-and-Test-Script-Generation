def calculate_discount(price):
    if not isinstance(price, (int, float)):
        raise TypeError("Price must be a number")
    if price > 100:
        return price * 0.8
    return price * 0.9