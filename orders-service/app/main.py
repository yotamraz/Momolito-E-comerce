from fastapi import FastAPI

app = FastAPI(title="Orders Service")


@app.get("/")
def read_root():
    return {"status": "ok", "service": "orders-service", "docs": "/docs"}
