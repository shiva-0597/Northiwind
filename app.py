from distutils.log import debug
from attr import field
from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from flask_restful import Api
from Models.product import db
from View.customers_view import CustomersViews,CustomerViews
from View.products_view import ProductsView,productView
from View.orders_view import OrdersViews,OrderViews,OrderHistoryView
app=Flask(__name__)
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

rest=Api(app)
db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()

rest.add_resource(CustomersViews, '/customers')
rest.add_resource(CustomerViews,'/customer/<string:CustomerID>')

rest.add_resource(OrderHistoryView,'/orderhistory/<string:CustomerID>')

rest.add_resource(OrdersViews,'/orders')
rest.add_resource(OrderViews,'/order/<int:OrderID>')

rest.add_resource(ProductsView,'/product')
rest.add_resource(productView,'/products/<string:ProductID>')

app.debug = True
if __name__ == '__main__':
    app.run(debug=True)



