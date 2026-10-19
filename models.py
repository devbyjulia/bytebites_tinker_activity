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

    def get_name(self) -> str:
        """Return the name of the FoodItem."""
        return self._name

    def get_price(self) -> float:
        """Return the price of the FoodItem."""
        return self._price

    def get_category(self) -> str:
        """Return the category of the FoodItem."""
        return self._category

    def get_popularity_rating(self) -> float:
        """Return the popularity rating of the FoodItem."""
        return self._popularity_rating


class Menu:
    """A list of all available food items. Items can be filtered by category."""

    def __init__(self):
        self._items: list[FoodItem] = []

    def add_item(self, item: FoodItem) -> None:
        """Add an item to the Menu."""
        self._items.append(item)

    def get_all_items(self) -> list[FoodItem]:
        """Get all the items in the Menu."""
        return self._items

    def filter_by_category(self, category: str) -> list[FoodItem]:
        """Filter items in the Menu by category."""
        return [item for item in self._items if item.get_category() == category]


class Transaction:
    """Stores the items added by a customer and computes the total cost."""

    def __init__(self):
        self._items: list[FoodItem] = []

    def add_item(self, item: FoodItem) -> None:
        self._items.append(item)

    def get_items(self) -> list[FoodItem]:
        return self._items

    def compute_total(self) -> float:
        return sum(item.get_price() for item in self._items)


class Customer:
    """Tracks a customer's name and purchase history, and verifies user authenticity."""

    def __init__(self, name: str):
        self._name = name
        self._purchase_history: list[Transaction] = []

    def get_name(self) -> str:
        return self._name

    def get_purchase_history(self) -> list[Transaction]:
        return self._purchase_history

    def add_purchase(self, transaction: Transaction) -> None:
        self._purchase_history.append(transaction)

    def is_verified(self) -> bool:
        return len(self._purchase_history) > 0
