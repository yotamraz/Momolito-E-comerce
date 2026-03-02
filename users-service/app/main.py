from fastapi import FastAPI
from shared.database import Base, engine
from .router import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Users Service")

app.include_router(router)


@app.get("/")
def read_root():
    return {"status": "ok", "service": "users-service", "docs": "/docs"}
