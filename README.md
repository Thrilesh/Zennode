# Shopping Cart System

This is a simple Python implementation of a shopping cart system. It consists of two classes: `Product` and `ShoppingCart`. The `Product` class represents individual products with their name, price, quantity, and gift wrapping status. The `ShoppingCart` class allows users to add products, calculate discounts based on certain rules, and generate a receipt.

## Classes

### Product

The `Product` class has the following attributes:

- `name`: The name of the product.
- `price`: The price of the product.
- `quantity`: The quantity of the product (initialized to 0 by default).
- `gift_wrapped`: A boolean indicating whether the product is gift-wrapped (initialized to False by default).

### ShoppingCart

The `ShoppingCart` class manages a collection of `Product` instances and provides methods for discount calculation and receipt generation. It has the following methods:

- `__init__(self, products)`: Initializes the shopping cart with a list of `Product` instances.
- `calculate_discount(self)`: Calculates and returns the most beneficial discount based on certain rules.
- `generate_receipt(self)`: Generates and prints a receipt for the products in the shopping cart.

## Example Usage

```python
# Example usage
product_a = Product("Product A", 20)
product_b = Product("Product B", 40)
product_c = Product("Product C", 50)

cart = ShoppingCart([product_a, product_b, product_c])

# Accept user input for quantity and gift wrapping (Sample input)
product_a.quantity = 5
product_b.quantity = 12
product_c.quantity = 10
product_c.gift_wrapped = True

# Calculate discounts and generate the receipt
cart.generate_receipt()
