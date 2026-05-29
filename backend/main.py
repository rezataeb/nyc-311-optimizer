from __future__ import annotations

from contextlib import asynccontextmanager
from pathlib import Path
from typing import AsyncIterator

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from .database import DB_PATH, get_crm_data, initialize_database

ROOT = Path(__file__).resolve().parents[1]


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    initialize_database()
    yield


app = FastAPI(title="Pipeline Pulse CRM", lifespan=lifespan)


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok", "database": str(DB_PATH)}


@app.get("/api/crm")
def crm() -> dict:
    return get_crm_data()


app.mount("/src", StaticFiles(directory=ROOT / "src"), name="src")
app.mount("/data", StaticFiles(directory=ROOT / "data"), name="data")


@app.get("/")
def index() -> FileResponse:
    return FileResponse(ROOT / "index.html")
