import mimetypes
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, PlainTextResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import os
from pathlib import Path

# Добавляем MIME типы
mimetypes.add_type("text/javascript", ".mjs")
mimetypes.add_type("application/wasm", ".wasm")
mimetypes.add_type("font/woff2", ".woff2")
mimetypes.add_type("image/png", ".png")
mimetypes.add_type("image/webp", ".webp")
mimetypes.add_type("application/font-woff", ".woff")

app = FastAPI()

# Нормализуем путь к статическим файлам
static_path = Path("nfactorial/static").resolve()

if not static_path.is_dir():
    raise RuntimeError(f"Директория '{static_path}' не существует")

# Монтируем статические файлы
app.mount(
    "/static",
    StaticFiles(directory=static_path, html=True),
    name="static"
)


@app.post("/send-contact")
async def send_contact(request: Request):
    try:
        form = await request.body()
        # TODO: Добавьте обработку формы
        return PlainTextResponse("ok")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Путь к index.html
index_file = static_path / "www.nfactorial.school" / "index.html"
if not index_file.is_file():
    raise RuntimeError(f"Файл '{index_file}' не существует")


@app.get("/", response_class=HTMLResponse)
async def root():
    return FileResponse(
        index_file,
        headers={"Cache-Control": "no-cache, no-store"}  # Исправлено: используем dict с : вместо set с ,
    )


@app.get("/static/{path:path}")
async def serve_static(path: str):
    static_file = static_path / path

    # Защита от path traversal
    try:
        static_file.resolve().relative_to(static_path)
    except ValueError:
        raise HTTPException(status_code=403, detail="Доступ запрещен")

    if static_file.is_file():
        return FileResponse(static_file)
    raise HTTPException(status_code=404)


@app.get("/{full_path:path}", response_class=HTMLResponse)
async def spa_fallback(full_path: str):
    # Проверяем существование файла
    requested_file = static_path / full_path

    # Защита от path traversal
    try:
        requested_file.resolve().relative_to(static_path)
    except ValueError:
        raise HTTPException(status_code=403, detail="Доступ запрещен")

    if requested_file.is_file():
        return FileResponse(requested_file)

    # Проверяем SPA-маршруты
    spa_paths = ["b2b", "blog", "courses"]
    if any(full_path.startswith(p) for p in spa_paths):
        return FileResponse(index_file)

    raise HTTPException(status_code=404)