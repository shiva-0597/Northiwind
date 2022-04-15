from Models.product import ProductModel,db
from flask import request
from flask_restful import Resource

class ProductsView(Resource):
    def get(self):
        product =ProductModel.query.all()
        return {"Products":[x.output() for x in product]}


class productView(Resource):
    def get(self,ProductID:int) -> dict:
        products=ProductModel.query.filter_by(ProductID=ProductID).first()
        if products:
            return products.output()
        return {"Output_message":"Customer not found"},404

    def put(self,ProductID:int) -> dict:
        req=request.get_json()
        products=ProductModel.query.filterby(productId=ProductID).first()
        if products:
            ProductModel.ProductName=req["ProductName"]
            ProductModel.SupplierID=req["SupplierID"]
            ProductModel.CategoryID=req["CategoryID"]
            ProductModel.Discontinued=req["Discontinued"]
            ProductModel.QuantityPerUnit=req["QuantityPerUnit"]
            ProductModel.UnitPrice=req["UnitPrice"]
            ProductModel.UnitsInStock=req["UnitsInStock"]
            ProductModel.ReorderLevel=req["ReorderLevel"]
            ProductModel.UnitsOnOrder=req["UnitsOnOrder"]
        else:
            product=ProductModel(ProductId=ProductID,SupplierID=req["SupplierID"],CategoryID=req["CategoryID"],
                        QuantityPerUnit=req["QuantityPerUnit"],UnitsInStock=req["UnitsInStock"],
                        ReorderLevel=req["ReorderLevel"],UnitPrice=req["UnitPrice"],Discontinued=req["Discontinued"],
                        ProductName=req["ProductName"],UnitsOnOrder=req["UnitsOnOrder"])
        
        db.session.add(product)
        db.session.commit()
        return {"Output_message":"Input Inserted"}
    def delete(self,ProductID:int):
        product=ProductModel.query.filter_by(ProductID=ProductID).first()
        if product:
            db.session.delete(product)
            db.session.commit()
            return {"output_message":"deleted"}
        return {"Output_message":"product not found"},404