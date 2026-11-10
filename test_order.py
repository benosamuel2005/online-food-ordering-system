# Programming Language: Python

import unittest
from order import Order


class TestOrder(unittest.TestCase):
    """
    Unit test class for testing the Order class.
    These tests validate business rules related to
    order item validation and order status transitions.
    """

    def setUp(self):
        """
        Creates a new Order object before each test case.
        """
        self.order = Order(order_id=1, customer="TestCustomer")

    def test_add_item_with_valid_values(self):
        """
        Test Case TC-01:
        Verify that an item with valid price and quantity
        is added successfully and total amount is calculated correctly.
        """
        self.order.add_item("Pizza", 200, 2)
        self.assertEqual(self.order.total_amount, 400)

    def test_add_item_with_negative_price(self):
        """
        Test Case TC-02:
        Verify that adding an item with a negative price
        raises a ValueError.
        """
        with self.assertRaises(ValueError):
            self.order.add_item("Burger", -100, 1)

    def test_valid_status_transition(self):
        """
        Test Case TC-03:
        Verify that a valid order status transition
        from Created to Confirmed is allowed.
        """
        self.order.update_status("Confirmed")
        self.assertEqual(self.order.status, "Confirmed")

    def test_invalid_status_transition(self):
        """
        Test Case TC-04:
        Verify that an invalid order status transition
        from Created to Paid raises a ValueError.
        """
        with self.assertRaises(ValueError):
            self.order.update_status("Paid")


if __name__ == "__main__":
    unittest.main()
