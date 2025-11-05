from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import time

from app.api.v1.routes import router as api_router


app = FastAPI(title="One Simple Trade API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health():
    return {"status": "ok", "timestamp": int(time.time() * 1000)}


app.include_router(api_router, prefix="/v1")


