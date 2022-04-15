from Models.product import ProductModel,db
from flask import request
from flask_restful import Resource

class ProductsView(Resource):
    def get_all_products(self):
        products =ProductModel.query.all()
        print(products)
        return {"customers":[x.output() for x in products]}


class productView(Resource):
    def get_products(self,productId:str) -> dict:
        products=ProductModel.query.filter(productId=productId).first()
        if products:
            return ProductModel.output()
        return {"Output_message":"Customer not found"},404

    def put_product(self,productId:str) -> dict:
        req=request.get_json()
        products=ProductModel.query.filterby(productId=productId).first()
        if products:
            ProductModel.productName=req["productName"]
            ProductModel.supplierId=req["supplierId"]
            ProductModel.categoryId=req["categoryId"]
            ProductModel.discontinued=req["discontinued"]
            ProductModel.quantityPerUnit=req["quantityPerUnit"]
            ProductModel.unitPrice=req["unitPrice"]
            ProductModel.unitsInStock=req["unitsInStock"]
            ProductModel.reorderLevel=req["reorderLevel"]
            ProductModel.unitsOnOrder=req["unitsOnOrder"]
        else:
            product=ProductModel(ProductId=productId,supplierId=req["supplierId"],categoryId=req["categoryId"],
                        quantityPerUnit=req["quantityPerUnit"],unitsInStock=req["unitsInStock"],
                        reorderLevel=req["reorderLevel"],unitPrice=req["unitPrice"],discontinued=req["discontinued"],
                        productName=req["productName"],unitsOnOrder=req["unitsOnOrder"])
        
        db.session.add(product)
        db.session.commit()
        return {"Output_message":"Input Inserted"}
    def delete_products(self,productId:str):
        product=ProductModel.query.filterby(productId=productId).first()
        if product:
            db.session.delete(product)
            db.commit()
            return {"output_message":"deleted"}
        return {"Output_message":"product not found"},404