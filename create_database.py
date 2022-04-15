import sqlite3
import pandas as pd
from pathlib import Path
Path('my_data.db').touch()
class DataBase:
    def __init__(self):
        self.name ='my_data.db'
        self.conn=sqlite3.connect(self.name)
        self.c = self.conn.cursor()
        self.orders=pd.read_csv('https://raw.githubusercontent.com/shiva-0597/Northiwind/master/orders.csv')
        self.products=pd.read_csv('https://raw.githubusercontent.com/shiva-0597/Northiwind/master/products.csv')
        self.customers=pd.read_csv('https://raw.githubusercontent.com/shiva-0597/Northiwind/master/customers.csv')
    @property
    def create_table(self):
        try:
            self.c.execute('''create table customers (CustomerID varchar(5) primary key,CompanyName varchar(40),ContactName varchar(30),ContactTitle varchar(30),Address varchar(60),City varchar(15),Region varchar(15),PostalCode varchar(10),Country varchar(15),Phone varchar(24),Fax varchar(24));''')
            self.c.execute('''create table products (ProductID integer primary key,ProductName varchar(40),SupplierID integer,CategoryID integer,QuantityPerUnit varchar(20),UnitPrice real,UnitsInStock integer,UnitsOnOrder integer,ReorderLevel integer,Discontinued boolean)''')
            self.c.execute('''create table orders (OrderID integer primary key,CustomerID varchar(5),EmployeeID integer,OrderDate date,RequiredDate date,ShippedDate date,ShipVia integer,Freight real,ShipName varchar(40),ShipAddress varchar(60),ShipCity varchar(15),ShipRegion varchar(15),ShipPostalCode varchar(10),ShipCountry varchar(15))''')
        except:
            print("Table Already Exists")
    def Insert_table(self):
        try:
            self.orders.to_sql('orders', self.conn, if_exists='append', index = False)
            self.products.to_sql('products', self.conn, if_exists='append', index=False)
            self.customers.to_sql('customers', self.conn, if_exists='append', index = False)
        except:
            pass
    def fetch_data(self):
        print(self.c.execute('''SELECT * FROM customers''').fetchall())
    
if __name__=='__main__':
    db=DataBase()
    db.fetch_data()
