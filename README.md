# Product API

A simple REST API built with FastAPI for managing products.

## What does this project do?

This API allows users to:

- Add a product
- View all products
- Find a product by ID
- Update a product
- Delete a product

## Product information

Each product contains:

- ID
- Name
- Price
- Quantity

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/products` | Add a product |
| GET | `/products` | Get all products |
| GET | `/products/{id}` | Get one product |
| PUT | `/products/{id}` | Update a product |
| DELETE | `/products/{id}` | Delete a product |

## Validation

The API checks that:

- Product name is not empty
- Price is greater than 0
- Quantity is not negative

If a product does not exist, the API returns a 404 error.

## How to run

Install the required packages:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload


## Example Product

```json
{
  "name": "Laptop",
  "price": 55000,
  "quantity": 5
}


```text
docs: add product API example
