class Category:
    def __init__(self, name):
        self.name = name

class Product:
    def __init__(self, name, code, price, idCategory):
        self.name = name
        self.code = code
        self.price = price
        self.idCategory = idCategory

class People:
    def __init__(self, name, cpf_cnpj, phoneNumber, address, email):
        self.name = name
        self.cpf_cnpj = cpf_cnpj
        self.phoneNumber = phoneNumber
        self.address = address
        self.email = email

class Supplier(People):
    def __init__(self, name, cpf_cnpj, phoneNumber, address, email, product_id):
        super().__init__(name, cpf_cnpj, phoneNumber, address, email)
        self.product_id = product_id

class Customer(People):
    def __init__(self, name, cpf_cnpj, phoneNumber, address, email, delivery_address=None):
        super().__init__(name, cpf_cnpj, phoneNumber, address, email)
        self.delivery_address = delivery_address

class Employee(People):
    def __init__(self, name, cpf_cnpj, phoneNumber, address, email, salary):
        super().__init__(name, cpf_cnpj, phoneNumber, address, email)
        self.salary = salary

class Stock:
    def __init__(self, product_id, quantity):
        self.product_id = product_id
        self.quantity = quantity

class Sale:
    def __init__(self, customer_id, employee_id, product_id, dataCompra, quantity):
        self.customer_id = customer_id
        self.employee_id = employee_id
        self.product_id = product_id
        self.dataCompra = dataCompra
        self.quantity = quantity
