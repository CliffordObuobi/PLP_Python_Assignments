# --- Parent Class: Product ---
class Product:
    """
    A class to represent a generic product in a grocery shop.
    """

    # Constructor method to initialize the object's attributes
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    # Method to display information about the product
    def display_info(self):
        print(f"Product: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Current Stock: {self.stock}")

# --- Child Class: FreshProduce ---
class FreshProduce(Product):
    """
    A class to represent fresh produce, inheriting from the Product class.
    It adds an 'expiration_date' attribute.
    """

    # Constructor for FreshProduce. It calls the parent's constructor
    # and then adds its unique attribute.
    def __init__(self, name, price, stock, expiration_date):
        # Call the constructor of the parent class (Product)
        super().__init__(name, price, stock)
        # Add the unique attribute for FreshProduce
        self.expiration_date = expiration_date

    # This method OVERRIDES the one in the parent class, demonstrating polymorphism.
    def display_info(self):
        print(f"--- Fresh Produce Item ---")
        print(f"Product: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Current Stock: {self.stock}")
        print(f"Expiration Date: {self.expiration_date}")

# --- Example Usage ---
if __name__ == "__main__":
    print("Creating a generic product...")
    # Creating an instance of the parent class
    cereal = Product("Breakfast Cereal", 3.99, 50)
    cereal.display_info()
    print("-" * 20)

    print("\nCreating a fresh produce item...")
    # Creating an instance of the child class
    apple = FreshProduce("Red Apple", 0.75, 120, "2025-09-15")
    # Calling the method. The child class's method is used automatically!
    apple.display_info()
    print("-" * 20)
    
    # Another example of a fresh produce item
    banana = FreshProduce("Banana", 0.50, 80, "2025-09-05")
    banana.display_info()