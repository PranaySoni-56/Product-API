from fastapi import APIRouter, HTTPException, status

from app.models import Product, ProductCreate

router = APIRouter()

# Simple in-memory storage. No database is required for this task.
products: list[Product] = []
next_id = 1


@router.post("/products", response_model=Product, status_code=status.HTTP_201_CREATED)
def add_product(product: ProductCreate):
    global next_id

    new_product = Product(
        id=next_id,
        name=product.name,
        price=product.price,
        quantity=product.quantity,
    )

    products.append(new_product)
    next_id += 1

    return new_product


@router.get("/products", response_model=list[Product])
def get_products():
    return products


@router.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product

    raise HTTPException(
        status_code=404,
        detail="Product not found",
    )


@router.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, product_data: ProductCreate):
    for product in products:
        if product.id == product_id:
            product.name = product_data.name
            product.price = product_data.price
            product.quantity = product_data.quantity
            return product

    raise HTTPException(
        status_code=404,
        detail="Product not found",
    )


@router.delete("/products/{product_id}")
def delete_product(product_id: int):
    for product in products:
        if product.id == product_id:
            products.remove(product)
            return {"message": "Product deleted successfully"}

    raise HTTPException(
        status_code=404,
        detail="Product not found",
    )
