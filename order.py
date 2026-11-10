# Programming Language: Python

class Order:
    """
    The Order class represents a customer order in the Online Food Ordering System.
    It is responsible for managing order items, calculating the total amount,
    and controlling valid order status transitions.
    """

    def __init__(self, order_id, customer):
        """
        Initializes a new Order instance.

        :param order_id: Unique identifier for the order
        :param customer: Customer who placed the order
        """
        self.order_id = order_id
        self.customer = customer
        self.items = []              # List to store order items
        self.total_amount = 0.0      # Total price of the order
        self.status = "Created"      # Initial order status

    def add_item(self, item_name, price, quantity):
        """
        Adds an item to the order after validating price and quantity.

        :param item_name: Name of the food item
        :param price: Price of a single item (must be positive)
        :param quantity: Quantity of the item (must be positive)
        :raises ValueError: If price or quantity is not positive
        """
        # Validation rule: price and quantity must be positive
        if price <= 0 or quantity <= 0:
            raise ValueError("Price and quantity must be positive values")

        # Create item as a dictionary
        item = {
            "name": item_name,
            "price": price,
            "quantity": quantity
        }

        # Add item to the order
        self.items.append(item)

        # Recalculate total amount after adding the item
        self.calculate_total()

    def calculate_total(self):
        """
        Calculates and updates the total amount of the order.

        :return: Total order amount
        """
        self.total_amount = sum(
            item["price"] * item["quantity"] for item in self.items
        )
        return self.total_amount

    def update_status(self, new_status):
        """
        Updates the order status based on valid state transitions.

        :param new_status: New status to be assigned to the order
        :raises ValueError: If the status transition is invalid
        """
        # Define valid order state transitions
        valid_transitions = {
            "Created": ["Confirmed", "Cancelled"],
            "Confirmed": ["Paid", "Cancelled"],
            "Paid": ["Delivered"],
        }

        # Check if the requested transition is allowed
        if new_status in valid_transitions.get(self.status, []):
            self.status = new_status
        else:
            raise ValueError(
                f"Invalid status transition from {self.status} to {new_status}"
            )
