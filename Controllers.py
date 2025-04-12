from Models import *
from DAO import *
from datetime import datetime

class ControllerCategory:

    @classmethod
    def existCategory(cls, categoryName):

        nameTitle = categoryName.title()
        listCategory = DAOCategory.Read_Doc()
        for i in listCategory:
            if i.name == nameTitle:
                return True
        return False

    @classmethod
    def existIdCategory(cls, categoryId):
        listCategory = len(DAOCategory.Read_Doc())
        if categoryId >= 0 and categoryId < listCategory:
            return True
        return False

    
    def registerCategory(self, categoryName):
        
        if self.existCategory(categoryName):
            return f"Category {categoryName} Already Exist"
        
        DAOCategory.Create_Doc(Category(categoryName))
        return f"Category {categoryName} Created"


    def showCategory(self):
        
        listCategory = DAOCategory.Read_Doc()

        for i in listCategory:
            print(f"ID {listCategory.index(i)} - Name: {i.name}")


    def updateCategory(self, itemId, categoryName):
        
        if self.existIdCategory(itemId) == False:
            return f"Category ID {itemId} not Found"
        
        DAOCategory.Update_Doc(itemId, categoryName)
        return f"Category ID {itemId} Updated Successfully"


    def deleteCategory(self, itemId):
        
        if self.existIdCategory(itemId) == False:
            return f"Category ID {itemId} not Found"
        
        DAOCategory.Delete_Doc(itemId)
        return f"Category ID {itemId} Deleted"


class ControllerProduct:

    @classmethod
    def existProduct(cls, productCode):
        listProduct = DAOProduct.Read_Doc()
        for i in listProduct:
            if i.code == productCode:
                return True
        return False
    

    @classmethod
    def existIdProduct(cls, productId):
        listProduct = len(DAOProduct.Read_Doc())
        if productId >= 0 and productId < listProduct:
            return True
        return False
    

    def registerProduct(self, prodName, prodCode, prodPrice, idCategory):
        
        if self.existProduct(prodCode):
            return f"Product Code {prodCode} Already Exist"
        
        if ControllerCategory.existIdCategory(idCategory) == False:
            return f"Category ID {idCategory} not Found"
        
        DAOProduct.Create_Doc(Product(prodName, prodCode, prodPrice, idCategory))
        return f"Product {prodName} Created"
    

    def showProduct(self):
        
        listProduct = DAOProduct.Read_Doc()

        for i in listProduct:
            print(f"ID {listProduct.index(i)} - Name: {i.name}, Code: {i.code}, Price: R$ {i.price}, Category: {i.idCategory}")


    def updateProduct(self, itemId, prodName, prodCode, prodPrice, idCategory):
        
        if ControllerCategory.existIdCategory(idCategory) == False:
            return f"Category ID {idCategory} not Found"
        
        if self.existIdProduct(itemId) == False:
            return f"Product ID {itemId} not Found"
        
        DAOProduct.Update_Doc(itemId, Product(prodName, prodCode, prodPrice, idCategory))
        return f"Product ID {itemId} Updated Successfully"


    def deleteProduct(self, productId):
        
        if self.existIdProduct(productId) == False:
            return f"Product ID {productId} not Found"
        
        DAOProduct.Delete_Doc(productId)
        return f"Product ID {productId} Deleted"
    

class ControllerSupplier:

    @classmethod
    def existSuppier(self, supplierId):
        