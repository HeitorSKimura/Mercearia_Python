from Models import *

class DAOCategory:
    
    arq_path = 'Arquivos/'
    category = ''

    # Salvar arquivo
    @classmethod
    def Create_Doc(cls, category: Category):
        # with open abre um documento e apos o uso, é fechado o documento
        with open(f'{cls.arq_path}Category.txt', 'a') as create:
            # writelines escreve uma lista em cada linha
            create.writelines(category.name.title())
            create.writelines('\n')
    
    # Ler o documento
    @classmethod
    def Read_Doc(cls):
        with open(f"{cls.arq_path}Category.txt", "r") as read:
            # Para cada linha retorna uma lista de categoria
            cls.category = read.readlines()

        # Retirar \n da lista de categorias
        cls.category = list(map(lambda x: x.replace('\n', ''), cls.category))
        list_category = []
        for i in cls.category:
            list_category.append(Category(i))
        return list_category

    # Atualizar Categoria
    @classmethod
    def Update_Doc(cls, line_number, new_category):

        # lê o arquivo
        with open(f"{cls.arq_path}Category.txt", "r") as read:
            lines = read.readlines()
        
        # Sobrescrever
        lines[line_number] = new_category.title() + '\n'

        # Reescrever o arquivo
        with open(f"{cls.arq_path}Category.txt", "w") as recreate:
            recreate.writelines(lines)
        
    # Deletar Catagoria
    @classmethod
    def Delete_Doc(cls, line_number):
        # lê o arquivo
        with open(f"{cls.arq_path}Category.txt", "r") as read:
            lines = read.readlines()
        
        # Remove a linha
        lines.pop(line_number)

        # Reescrever o arquivo
        with open(f"{cls.arq_path}Category.txt", "w") as recreate:
            recreate.writelines(lines)

class DAOProduct:
    
    arq_path = 'Arquivos/'
    product = ''

    # Salvar arquivo
    @classmethod
    def Create_Doc(cls, product: Product):
        with open(f'{cls.arq_path}Product.txt', 'a') as create:
            create.writelines(f"{product.name.title()},{product.code},{product.price},{product.idCategory}")
            create.writelines('\n')
    
    # Ler o documento
    @classmethod
    def Read_Doc(cls):
        with open(f"{cls.arq_path}Product.txt", "r") as read:
            cls.product = read.readlines()

        cls.product = list(map(lambda x: x.replace('\n', ''), cls.product))
        cls.product = list(map(lambda x: x.split(','), cls.product))
        list_product = []
        for i in cls.product:
            list_product.append(Product(i[0], i[1], i[2], i[3]))
        return list_product
        

    @classmethod
    def Update_Doc(cls, line_number, new_product: Product):

        # lê o arquivo
        with open(f"{cls.arq_path}Product.txt", "r") as read:
            lines = read.readlines()
        
        # Sobrescrever
        lines[line_number] = f"{new_product.name.title()},{new_product.code},{new_product.price},{new_product.idCategory}\n"

        # Reescrever o arquivo
        with open(f"{cls.arq_path}Product.txt", "w") as recreate:
            recreate.writelines(lines)
        
    # Deletar Catagoria
    @classmethod
    def Delete_Doc(cls, line_number):
        # lê o arquivo
        with open(f"{cls.arq_path}Product.txt", "r") as read:
            lines = read.readlines()
        
        # Remove a linha
        lines.pop(line_number)

        # Reescrever o arquivo
        with open(f"{cls.arq_path}Product.txt", "w") as recreate:
            recreate.writelines(lines)

class DAOSupplier:
    
    arq_path = 'Arquivos/'
    supplier = ''

    # Salvar arquivo
    @classmethod
    def Create_Doc(cls, supplier: Supplier):
        with open(f'{cls.arq_path}Supplier.txt', 'a') as create:
            create.writelines(f"{supplier.name},{supplier.cpf_cnpj},{supplier.phoneNumber},{supplier.address},{supplier.email},{supplier.product_id}")
            create.writelines('\n')
    
    # Ler o documento
    @classmethod
    def Read_Doc(cls):
        with open(f"{cls.arq_path}Supplier.txt", "r") as read:
            cls.supplier = read.readlines()

        cls.supplier = list(map(lambda x: x.replace('\n', ''), cls.supplier))
        cls.supplier = list(map(lambda x: x.split(','), cls.supplier))
        list_supplier = []
        for i in cls.supplier:
            list_supplier.append(Supplier(i[0], i[1], i[2], i[3], i[4], i[5]))
        return list_supplier
        

    @classmethod
    def Update_Doc(cls, line_number, new_sup: Supplier):

        # lê o arquivo
        with open(f"{cls.arq_path}Supplier.txt", "r") as read:
            lines = read.readlines()
        
        # Sobrescrever
        lines[line_number] = f"{new_sup.name},{new_sup.cpf_cnpj},{new_sup.phoneNumber},{new_sup.address},{new_sup.email},{new_sup.product_id}\n"

        # Reescrever o arquivo
        with open(f"{cls.arq_path}Supplier.txt", "w") as recreate:
            recreate.writelines(lines)
        
    # Deletar Catagoria
    @classmethod
    def Delete_Doc(cls, line_number):
        # lê o arquivo
        with open(f"{cls.arq_path}Supplier.txt", "r") as read:
            lines = read.readlines()
        
        # Remove a linha
        lines.pop(line_number)

        # Reescrever o arquivo
        with open(f"{cls.arq_path}Supplier.txt", "w") as recreate:
            recreate.writelines(lines)

class DAOCustomer:
    
    arq_path = 'Arquivos/'
    customer = ''

    # Salvar arquivo
    @classmethod
    def Create_Doc(cls, customer: Customer):
        with open(f'{cls.arq_path}Customer.txt', 'a') as create:
            create.writelines(f"{customer.name},{customer.cpf_cnpj},{customer.phoneNumber},{customer.address},{customer.email},{customer.delivery_address}")
            create.writelines('\n')
    
    # Ler o documento
    @classmethod
    def Read_Doc(cls):
        with open(f"{cls.arq_path}Customer.txt", "r") as read:
            cls.customer = read.readlines()

        cls.customer = list(map(lambda x: x.replace('\n', ''), cls.customer))
        cls.customer = list(map(lambda x: x.split(','), cls.customer))
        list_customer = []
        for i in cls.customer:
            list_customer.append(Customer(i[0], i[1], i[2], i[3], i[4], i[5]))
        return list_customer
        

    @classmethod
    def Update_Doc(cls, line_number, new_cust: Customer):

        # lê o arquivo
        with open(f"{cls.arq_path}Customer.txt", "r") as read:
            lines = read.readlines()
        
        # Sobrescrever
        lines[line_number] = f"{new_cust.name},{new_cust.cpf_cnpj},{new_cust.phoneNumber},{new_cust.address},{new_cust.email},{new_cust.delivery_address}\n"

        # Reescrever o arquivo
        with open(f"{cls.arq_path}Customer.txt", "w") as recreate:
            recreate.writelines(lines)
        
    # Deletar Catagoria
    @classmethod
    def Delete_Doc(cls, line_number):
        # lê o arquivo
        with open(f"{cls.arq_path}Customer.txt", "r") as read:
            lines = read.readlines()
        
        # Remove a linha
        lines.pop(line_number)

        # Reescrever o arquivo
        with open(f"{cls.arq_path}Customer.txt", "w") as recreate:
            recreate.writelines(lines)

class DAOEmployee:
    
    arq_path = 'Arquivos/'
    employee = ''

    # Salvar arquivo
    @classmethod
    def Create_Doc(cls, employee: Employee):
        with open(f'{cls.arq_path}Employee.txt', 'a') as create:
            create.writelines(f"{employee.name},{employee.cpf_cnpj},{employee.phoneNumber},{employee.address},{employee.email},{employee.salary}")
            create.writelines('\n')
    
    # Ler o documento
    @classmethod
    def Read_Doc(cls):
        with open(f"{cls.arq_path}Employee.txt", "r") as read:
            cls.employee = read.readlines()

        cls.employee = list(map(lambda x: x.replace('\n', ''), cls.employee))
        cls.employee = list(map(lambda x: x.split(','), cls.employee))
        list_employee = []
        for i in cls.employee:
            list_employee.append(Employee(i[0], i[1], i[2], i[3], i[4], i[5]))
        return list_employee
        

    @classmethod
    def Update_Doc(cls, line_number, new_emplo: Employee):

        # lê o arquivo
        with open(f"{cls.arq_path}Employee.txt", "r") as read:
            lines = read.readlines()
        
        # Sobrescrever
        lines[line_number] = f"{new_emplo.name},{new_emplo.cpf_cnpj},{new_emplo.phoneNumber},{new_emplo.address},{new_emplo.email},{new_emplo.salary}\n"

        # Reescrever o arquivo
        with open(f"{cls.arq_path}Employee.txt", "w") as recreate:
            recreate.writelines(lines)
        
    # Deletar Catagoria
    @classmethod
    def Delete_Doc(cls, line_number):
        # lê o arquivo
        with open(f"{cls.arq_path}Employee.txt", "r") as read:
            lines = read.readlines()
        
        # Remove a linha
        lines.pop(line_number)

        # Reescrever o arquivo
        with open(f"{cls.arq_path}Employee.txt", "w") as recreate:
            recreate.writelines(lines)

class DAOStock:
    
    arq_path = 'Arquivos/'
    stock = ''

    # Salvar arquivo
    @classmethod
    def Create_Doc(cls, stock: Stock):
        with open(f'{cls.arq_path}Stock.txt', 'a') as create:
            create.writelines(f"{stock.product_id},{stock.quantity}")
            create.writelines('\n')
    
    # Ler o documento
    @classmethod
    def Read_Doc(cls):
        with open(f"{cls.arq_path}Stock.txt", "r") as read:
            cls.stock = read.readlines()

        cls.stock = list(map(lambda x: x.replace('\n', ''), cls.stock))
        cls.stock = list(map(lambda x: x.split(','), cls.stock))
        list_stock = []
        for i in cls.stock:
            list_stock.append(Stock(i[0], i[1]))
        return list_stock
        

    @classmethod
    def Update_Doc(cls, line_number, new_stock: Stock):

        # lê o arquivo
        with open(f"{cls.arq_path}Stock.txt", "r") as read:
            lines = read.readlines()
        
        # Sobrescrever
        lines[line_number] = f"{new_stock.product_id},{new_stock.quantity}\n"

        # Reescrever o arquivo
        with open(f"{cls.arq_path}Stock.txt", "w") as recreate:
            recreate.writelines(lines)
        
    # Deletar Catagoria
    @classmethod
    def Delete_Doc(cls, line_number):
        # lê o arquivo
        with open(f"{cls.arq_path}Stock.txt", "r") as read:
            lines = read.readlines()
        
        # Remove a linha
        lines.pop(line_number)

        # Reescrever o arquivo
        with open(f"{cls.arq_path}Stock.txt", "w") as recreate:
            recreate.writelines(lines)

class DAOSale:
    
    arq_path = 'Arquivos/'
    sale = ''

    # Salvar arquivo
    @classmethod
    def Create_Doc(cls, sale: Sale):
        with open(f'{cls.arq_path}Sale.txt', 'a') as create:
            create.writelines(f"{sale.customer_id},{sale.employee_id},{sale.product_id},{sale.dataCompra},{sale.quantity}")
            create.writelines('\n')
    
    # Ler o documento
    @classmethod
    def Read_Doc(cls):
        with open(f"{cls.arq_path}Sale.txt", "r") as read:
            cls.sale = read.readlines()

        cls.sale = list(map(lambda x: x.replace('\n', ''), cls.sale))
        cls.sale = list(map(lambda x: x.split(','), cls.sale))
        list_sale = []
        for i in cls.sale:
            list_sale.append(Sale(i[0], i[1], i[2], i[3], i[4]))
        return list_sale
        

    @classmethod
    def Update_Doc(cls, line_number, new_sale: Sale):

        # lê o arquivo
        with open(f"{cls.arq_path}Sale.txt", "r") as read:
            lines = read.readlines()
        
        # Sobrescrever
        lines[line_number] = f"{new_sale.customer_id},{new_sale.employee_id},{new_sale.product_id},{new_sale.dataCompra},{new_sale.quantity}\n"

        # Reescrever o arquivo
        with open(f"{cls.arq_path}Sale.txt", "w") as recreate:
            recreate.writelines(lines)
        
    # Deletar Catagoria
    @classmethod
    def Delete_Doc(cls, line_number):
        # lê o arquivo
        with open(f"{cls.arq_path}Sale.txt", "r") as read:
            lines = read.readlines()
        
        # Remove a linha
        lines.pop(line_number)

        # Reescrever o arquivo
        with open(f"{cls.arq_path}Sale.txt", "w") as recreate:
            recreate.writelines(lines)

