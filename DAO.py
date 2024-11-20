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

        return cls.category

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
            create.writelines(product.name.title(), product.code, product.price, product.category)
            create.writelines('\n')
    
    # Ler o documento
    @classmethod
    def Read_Doc(cls):
        with open(f"{cls.arq_path}Category.txt", "r") as read:
            cls.category = read.readlines()

        cls.category = list(map(lambda x: x.replace('\n', ''), cls.category))

        return cls.category

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