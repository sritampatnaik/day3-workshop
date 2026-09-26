import os
from datetime import datetime, timezone

import httpx
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, Field

app = FastAPI(title="llm-multiroute")

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://127.0.0.1:11434").rstrip("/")
OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY", "")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "gemma:2b")
DATA_DIR = os.getenv("DATA_DIR", "./data")


class ChatRequest(BaseModel):
    prompt: str = Field(min_length=1)
    model: str | None = None


def _headers() -> dict[str, str]:
    if not OLLAMA_API_KEY:
        return {}
    return {"Authorization": f"Bearer {OLLAMA_API_KEY}"}


def _log(prompt: str, model: str) -> None:
    os.makedirs(DATA_DIR, exist_ok=True)
    stamp = datetime.now(timezone.utc).isoformat()
    with open(os.path.join(DATA_DIR, "requests.log"), "a", encoding="utf-8") as handle:
        handle.write(f"{stamp}\t{model}\t{prompt}\n")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/swagger-ui.html")
def swagger() -> RedirectResponse:
    return RedirectResponse(url="/docs")


@app.post("/chat")
def chat(body: ChatRequest) -> dict[str, str]:
    model = body.model or OLLAMA_MODEL
    _log(body.prompt, model)
    payload = {"model": model, "prompt": body.prompt, "stream": False}
    try:
        with httpx.Client(timeout=120) as client:
            response = client.post(
                f"{OLLAMA_BASE_URL}/api/generate",
                json=payload,
                headers=_headers(),
            )
            response.raise_for_status()
            data = response.json()
    except httpx.HTTPError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc
    return {"model": model, "response": data.get("response", "")}
