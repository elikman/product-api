from fastapi import FastAPI
from fastapi.responses import JSONResponse
from .routers import products, categories
from .database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def root():
    return JSONResponse(content={"message": "Welcome to the Product API"})

app.include_router(products.router, prefix="/products", tags=["products"])
app.include_router(categories.router, prefix="/categories", tags=["categories"])
