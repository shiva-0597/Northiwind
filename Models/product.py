from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class ProductModel(db.Model):
    __tablename__='products'
    productId = db.Column(db.String(30), primary_key=True)
    productName = db.Column(db.String(40), nullable=False)
    supplierId = db.Column(db.Integer, nullable=False)
    categoryId = db.Column(db.Integer, nullable=False)
    quantityPerUnit = db.Column(db.String(20), nullable=False)
    unitPrice = db.Column(db.Float, nullable=False)
    unitsInStock = db.Column(db.Integer, nullable=False)
    unitsOnOrder = db.Column(db.Integer, nullable=False)
    reorderLevel = db.Column(db.Integer, nullable=False)
    discontinued = db.Column(db.Integer, nullable=False)
    def __init__(self,productId,productName,supplierId,categoryId,quantityPerUnit,unitPrice,unitsInStock,unitsOnOrder,reorderLevel,discontinued):
        self.productId=productId
        self.productName=productName
        self.supplierId=supplierId
        self.categoryId=categoryId
        self.quantityPerUnit=quantityPerUnit
        self.unitPrice=unitPrice
        self.unitsInStock=unitsInStock
        self.unitsOnOrder=unitsOnOrder
        self.reorderLevel=reorderLevel
        self.discontinued=discontinued
    def output(self) -> dict:
        return {
            "productId": self.productId,
            "productName":self.productName,
            "supplierId": self.supplierId,
            "categoryId": self.categoryId,
            "quantityPerUnit": self.quantityPerUnit,
            "unitPrice": self.unitPrice,
            "unitsInStock": self.unitsInStock,
            "unitsOnOrder": self.unitsOnOrder,
            "reorderLevel": self.reorderLevel,
            "discontinued":self.discontinued
        }
    