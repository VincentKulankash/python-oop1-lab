#!/usr/bin/env python3

class Coffee:
    """
    Represents a coffee sold at the bookstore.
    Attributes:
        size (str): Small, Medium, or Large.
        price (float): The price of the coffee.
    """

    def __init__(self, size, price):
        # Initialize the coffee with size and price
        self.size = size
        self.price = price

    @property
    def size(self):
        """Getter for size."""
        return self._size

    @size.setter
    def size(self, value):
        """Setter validates size is Small, Medium, or Large."""
        if value not in ("Small", "Medium", "Large"):
            print("size must be Small, Medium, or Large")
        else:
            self._size = value

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1