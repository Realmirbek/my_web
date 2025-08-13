import mimetypes
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, PlainTextResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import os

# Добавляем типы, которых Python может не знать
mimetypes.add_type("text/javascript", ".mjs")
mimetypes.add_type("application/wasm", ".wasm")

app = FastAPI()

# Правильный путь до статических файлов
static_path = os.path.abspath("nfactorial/static")
if not os.path.isdir(static_path):
    raise RuntimeError(f"Directory '{static_path}' does not exist")

# Монтируем статические файлы
app.mount("/static", StaticFiles(directory=static_path), name="static")

# API-роут для формы (ставим ДО статических, чтобы не перекрыть)
@app.post("/send-contact")
async def send_contact(request: Request):
    form = await request.body()
    # TODO: распарсить form и сделать свою логику (почта/БД/телега)
    return PlainTextResponse("ok")

# Отдаём index.html как корень
index_file = os.path.join(static_path, "site", "index.html")
@app.get("/", response_class=HTMLResponse)
async def root():
    return FileResponse(index_file)

# SPA fallback — чтобы /about и т.п. тоже открывались локально
@app.get("/{full_path:path}", response_class=HTMLResponse)
async def spa_fallback(full_path: str):
    return FileResponse(index_file)
