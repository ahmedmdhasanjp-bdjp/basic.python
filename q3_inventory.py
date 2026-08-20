class Product:
    next_id = 1

    def __init__(self, name, price, stock=0):
        self.product_id = Product.next_id
        Product.next_id += 1

        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Price: {self.price} yen, Stock: {self.stock}"

class Inventory:

    def __init__(self):
        self.products = []

    def add_product(self, name, price, stock=0):
        product = Product(name, price, stock)
        self.products.append(product)
        print("Product added successfully.")

    def view_products(self):
        for product in self.products:
            print(product)

    def search_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                print(product)
                return
        print("Product not found.")

    def update_product(self, product_id, new_price, new_stock):
        for product in self.products:
            if product.product_id == product_id:
                product.price = new_price
                product.stock = new_stock
                print("Product updated successfully.")
                return
        print("Product not found.")

    def delete_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                print("Product deleted successfully.")
                return
        print("Product not found.")

    def restock(self, product_id, quantity):
        for product in self.products:
            if product.product_id == product_id:
                product.stock += quantity
                print("Product restocked successfully.")
                return
        print("Product not found.")

inventory = Inventory()

inventory.add_product("Onigiri", 150, 20)

inventory.add_product("Green Tea", 120, 15)

inventory.add_product("Bento Box", 500, 10)

inventory.view_products()

print("\n-- Restock --")

inventory.restock(2, 30)

print("\n-- Update --")

inventory.update_product(3, 550, 8)

print("\n-- Delete --")

inventory.delete_product(1)

inventory.view_products()