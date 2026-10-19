# Classes
# Customer: Manage customers, track names and purchase histories, and verify user authenticity.
# FoodItem: A single food item; item name, price, category, and popularity rating.
# Menu: A list of all available food items. Items can be filtered by category.
# Transaction: A single transaction object stores the items added by a customer. Compute the total cost of the transaction.


class FoodItem:
    """A single food item; item name, price, category, and popularity rating."""

    def __init__(self, name: str, price: float, category: str, popularity_rating: float):
        self._name = name
        self._price = price
        self._category = category
        self._popularity_rating = popularity_rating


class Menu:
    """A list of all available food items. Items can be filtered by category."""

    def __init__(self):
        self._items: list[FoodItem] = []



class Transaction:
    """Stores the items added by a customer and computes the total cost."""

    def __init__(self):
        self._items: list[FoodItem] = []


class Customer:
    """Tracks a customer's name and purchase history and verifies user authenticity."""

    def __init__(self, name: str):
        self._name = name
        self._purchase_history: list[Transaction] = []