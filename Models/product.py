from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class ProductModel(db.Model):
    __tablename__='products'
    ProductID = db.Column(db.Integer, primary_key=True)
    ProductName = db.Column(db.String(40), nullable=False)
    SupplierID = db.Column(db.Integer, nullable=False)
    CategoryID = db.Column(db.Integer, nullable=False)
    QuantityPerUnit = db.Column(db.String(20), nullable=False)
    UnitPrice = db.Column(db.Float, nullable=False)
    UnitsInStock = db.Column(db.Integer, nullable=False)
    UnitsOnOrder = db.Column(db.Integer, nullable=False)
    ReorderLevel = db.Column(db.Integer, nullable=False)
    Discontinued = db.Column(db.Integer, nullable=False)
    def __init__(self,ProductID,ProductName,SupplierID,CategoryID,QuantityPerUnit,UnitPrice,UnitsInStock,UnitsOnOrder,ReorderLevel,Discontinued):
        self.ProductID=ProductID
        self.ProductName=ProductName
        self.SupplierID=SupplierID
        self.CategoryID=CategoryID
        self.QuantityPerUnit=QuantityPerUnit
        self.UnitPrice=UnitPrice
        self.UnitsInStock=UnitsInStock
        self.UnitsOnOrder=UnitsOnOrder
        self.ReorderLevel=ReorderLevel
        self.Discontinued=Discontinued
    def output(self) -> dict:
        return {
            "productId": self.ProductID,
            "productName":self.ProductName,
            "supplierId": self.SupplierID,
            "categoryId": self.CategoryID,
            "quantityPerUnit": self.QuantityPerUnit,
            "unitPrice": self.UnitPrice,
            "unitsInStock": self.UnitsInStock,
            "unitsOnOrder": self.UnitsOnOrder,
            "reorderLevel": self.ReorderLevel,
            "discontinued":self.Discontinued
        }
    