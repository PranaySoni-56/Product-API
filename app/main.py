from fastapi import FastAPI

from app.routes import router

app = FastAPI(title="Simple Product API")

app.include_router(router)


@app.get("/")
def home():
    return {"message": "Product API is running"}
