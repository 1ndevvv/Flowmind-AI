 
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import httpx
import os
from dotenv import load_dotenv
from prompts import WORKFLOW_PROMPTS
 
load_dotenv()
 
app = FastAPI(title="FlowMind AI API", version="1.0.0")
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # tighten this to your frontend URL in production
    allow_methods=["*"],
    allow_headers=["*"],
)
 
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
 
 
# ── Request / Response schemas ──────────────────────────────────────────────
 
class Message(BaseModel):
    role: str        # "user" | "assistant"
    content: str
 
class ChatRequest(BaseModel):
    workflow: str          # e.g. "email", "summary", "plan" …
    messages: List[Message]
 
class ChatResponse(BaseModel):
    reply: str
    workflow: str
    tokens_used: int = 0
 
 
# ── Health check ─────────────────────────────────────────────────────────────
 
@app.get("/")
def root():
    return {"status": "FlowMind AI backend is running 🚀"}
 
@app.get("/health")
def health():
    return {"status": "ok", "gemini_configured": bool(GEMINI_API_KEY)}
 
@app.get("/workflows")
def list_workflows():
    return {"workflows": list(WORKFLOW_PROMPTS.keys())}
 
 
# ── Main chat endpoint ────────────────────────────────────────────────────────
 
@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    if not GEMINI_API_KEY:
        raise HTTPException(status_code=500, detail="GEMINI_API_KEY not set on server.")
 
    workflow = req.workflow.lower()
    system_prompt = WORKFLOW_PROMPTS.get(workflow, WORKFLOW_PROMPTS["chat"])
 
    # Build Gemini contents array
    contents = [
        {
            "role": "model" if m.role == "assistant" else "user",
            "parts": [{"text": m.content}]
        }
        for m in req.messages
    ]
 
    payload = {
        "system_instruction": {"parts": [{"text": system_prompt}]},
        "contents": contents,
        "generationConfig": {
            "temperature": 0.85,
            "maxOutputTokens": 1200
        }
    }
 
    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.post(
            f"{GEMINI_URL}?key={GEMINI_API_KEY}",
            json=payload
        )
 
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
 
    data = response.json()
 
    if "error" in data:
        raise HTTPException(status_code=400, detail=data["error"]["message"])
 
    reply = data["candidates"][0]["content"]["parts"][0]["text"]
    tokens = data.get("usageMetadata", {}).get("totalTokenCount", 0)
 
    return ChatResponse(reply=reply, workflow=workflow, tokens_used=tokens)
 