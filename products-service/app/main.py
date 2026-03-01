from fastapi import FastAPI

app = FastAPI(title="Products Service")


@app.get("/")
def read_root():
    return {"status": "ok", "service": "products-service", "docs": "/docs"}
