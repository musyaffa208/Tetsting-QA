# SimpleCart
implement simple cart and promotion

# Setup Guide


## Install, create and activate virtualenv
https://medium.com/analytics-vidhya/virtual-environment-6ad5d9b6af59

## Install requirements

    pip install -r requirements.txt
## create database
create new database, in this case we're using postgresql

## set env variable

create file .env in the root of the folder, and fill with you credential of your database

      
    DB_USER = ""
    DB_PASSWORD = ""
    DB_HOST = ""
    DB_PORT = ""
    DB_NAME = ""
    FLASK_DEBUG = true

## Create table

run `flask create`to create tables from models.

## Insert data product

run this query from your db client
```
INSERT INTO public.product (sku,brand,"name",description,price,non_discountable) VALUES
	 ('ABCKM5','ABC','kecap manis ABC 500ml','kecap manis abc 500ml',25000.0,false),
	 ('INDOSKM25','Indofood','Susu kental manis 250ml','Susu kental manis 250ml',15000.0,false),
	 ('LIOML1','Lion','Mamalemon 1000ml ','Mamalemon 1000ml ',21000.0,false),
	 ('INDOBR','Indofood','Bumbu racik','Bumbu racik',2500.0,false),
	 ('ABCS25','ABC','Sambal 250ml','Sambal 250ml',15000.0,false),
	 ('INDOIGS','Indofood','Indomie goreng special','Indomie goreng special',3000.0,false),
	 ('MYRLM1','mayora','le minerale 1000ml','le minerale 1000ml',8000.0,true);
```

## Run the app
to run the web app simply  use

    flask run

to access swagger use url `localhost:5000/apidocs`


## Debt

 - Cart Update
 - Same product validation on cart
 - Unit test
 - Unit test coverage
 - CI setup 

# opsi 2 dalam testing routes

import json
import pytest

# Tambahkan decorator @pytest.fixture untuk mendapatkan klien
@pytest.fixture
def client(app):
    return app.test_client()

def test_product_detail_api(client):
    id = 1
    response = client.get(f"/api/products/{id}")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert id == data.get('id')

def test_product_api(client):
    response = client.get("/api/products")  # Perubahan: Ganti f"/api/products/{id}" dengan "/api/products"
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) > 0  # Perubahan: Memastikan bahwa ada setidaknya satu produk dalam daftar

def test_carts_api(client):
    response = client.get("/api/cart")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) > 0  # Perubahan: Memastikan bahwa ada setidaknya satu keranjang dalam daftar

def test_cart_detail_api(client):
    response = client.get("/api/cart/1")
    assert response.status_code == 404  # Perubahan: Memastikan bahwa status_code yang diharapkan adalah 404

def test_create_cart_api(client):
    cart_data = {
        "coupon_code": "DISCOUNT10",
        "cart_items": [{"product_id": 1, "qty": 2}]
    }
    response = client.post("/api/cart", json=cart_data)
    assert response.status_code == 200
    assert response.data == b'data created'  # Perubahan: Memastikan bahwa pesan respons sesuai dengan yang diharapkan
