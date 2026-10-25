from models import FoodItem, Menu, Transaction, Customer

import pytest

@pytest.fixture
def red_velvet():   return FoodItem("Red Velvet", 4.50, "Desserts", 4.7)
@pytest.fixture
def marble_cake():   return FoodItem("Marble Cake", 6.00, "Desserts", 4.7)
@pytest.fixture
def soda():     return FoodItem("Tropical Punch", 2.25, "Drinks", 4.1)
@pytest.fixture
def lemonade(): return FoodItem("Lemonade", 3.00, "Drinks", 4.4)
@pytest.fixture
def brownie():  return FoodItem("Brownie", 3.75, "Desserts", 4.9)
@pytest.fixture
def complimentary_cookie():  return FoodItem("Free Cookie", 0.0, "Desserts", 5)

@pytest.fixture
def full_menu(red_velvet, marble_cake, soda, lemonade, brownie):
    menu = Menu()
    for item in [red_velvet, marble_cake, soda, lemonade, brownie]:
        menu.add_item(item)
    return menu

@pytest.fixture
def transaction(red_velvet, marble_cake):
    transaction = Transaction()
    transaction.add_item(red_velvet)
    transaction.add_item(marble_cake)
    return transaction

@pytest.fixture
def empty_transaction():
    return Transaction()

@pytest.fixture
def customer():
    return Customer("Julia")

def test_calculate_total(transaction: Transaction):
    """Verify that the total equals the sum of all item prices (4.50 + 6.00 = 10.50)."""
    result = transaction.compute_total()
    assert result == pytest.approx(10.50)

def test_order_total_is_zero_when_empty(empty_transaction: Transaction):
    """Verify that an empty Transaction totals 0."""
    result = empty_transaction.compute_total()
    assert result == pytest.approx(0.0)

def test_filtering_menu_by_category(full_menu, red_velvet, marble_cake, brownie):
    """Verify that filtering 'Desserts' returns only the dessert items."""
    result = full_menu.filter_by_category("Desserts")
    assert result == [red_velvet, marble_cake, brownie]

def test_customer_verified_after_purchase(customer: Customer, transaction: Transaction):
    """Verify that a Customer becomes verified after one purchase."""
    assert not customer.is_verified()
    customer.add_purchase(transaction)
    assert customer.is_verified()

def test_fooditem_accepts_zero_price(complimentary_cookie):
    """Verify that a free item (price 0.0) is stored and returned as 0.0"""
    assert complimentary_cookie.get_price() == 0.0