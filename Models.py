class Category:
    def __init__(self, name):
        self.name = name

class Product:
    def __init__(self, name, code, price, category: Category):
        self.name = name
        self.code = code
        self.price = price
        self.category = category

class People:
    def __init__(self, name, cpf_cnpj, phoneNumber, address, email):
        self.name = name
        self.cpf_cnpj = cpf_cnpj
        self.phoneNumber = phoneNumber
        self.address = address
        self.email = email

class Supplier(People):
    def __init__(self, name, cpf_cnpj, phoneNumber, address, email, *products:Product):
        super().__init__(name, cpf_cnpj, phoneNumber, address, email)
        self.product = products

class Customer(People):
    def __init__(self, name, cpf_cnpj, phoneNumber, address, email, lastBuy):
        super().__init__(name, cpf_cnpj, phoneNumber, address, email)
        self.lastBuy = lastBuy

class Employee(People):
    def __init__(self, name, cpf_cnpj, phoneNumber, address, email, salary):
        super().__init__(name, cpf_cnpj, phoneNumber, address, email)
        self.salary = salary

class Stock:
    def __init__(self, product: Product, quantity):
        self.product = product
        self.quantity = quantity

class Sale:
    def __init__(self, customer: Customer, *products: Product):
        self.customer = customer
        self.products = products