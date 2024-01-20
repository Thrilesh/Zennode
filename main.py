class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.quantity = 0
        self.gift_wrapped = False


class ShoppingCart:
    def __init__(self, products):
        self.products = products

    def calculate_discount(self):
        total_quantity = sum(product.quantity for product in self.products)
        max_quantity_product = max(self.products, key=lambda x: x.quantity)

        # Apply the most beneficial discount
        discount = 0
        if total_quantity > 30 and max_quantity_product.quantity > 15:
            discount = 0.5
        elif max_quantity_product.quantity > 10:
            discount = 0.05
        elif total_quantity > 20:
            discount = 0.1
        elif total_quantity > 200:
            discount = 10

        return discount

    def generate_receipt(self):
        total_quantity = 0
        subtotal = sum(product.quantity *
                       product.price for product in self.products)
        discount = self.calculate_discount()
        discount_amount = subtotal * discount
        shipping_fee = (total_quantity // 10) * 5
        gift_wrap_fee = sum(
            product.quantity for product in self.products if product.gift_wrapped) * 1

        total = subtotal - discount_amount + shipping_fee + gift_wrap_fee

        # Display the receipt
        print("Product\tQuantity\tTotal Amount")
        for product in self.products:
            print(
                f"{product.name}\t{product.quantity}\t\t{product.quantity * product.price}")

        print("\nSubtotal:", subtotal)
        print("Discount Applied:", f"{discount * 100}%")
        print("Discount Amount:", discount_amount)
        print("Shipping Fee:", shipping_fee)
        print("Gift Wrap Fee:", gift_wrap_fee)
        print("\nTotal:", total)


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
