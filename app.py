import mimetypes
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import FileResponse, RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

# Добавляем MIME типы
mimetypes.add_type("text/javascript", ".mjs")
mimetypes.add_type("application/wasm", ".wasm")
mimetypes.add_type("font/woff2", ".woff2")
mimetypes.add_type("image/png", ".png")
mimetypes.add_type("image/webp", ".webp")
mimetypes.add_type("application/font-woff", ".woff")

app = FastAPI()

static_path = Path("nfactorial/static").resolve()

# Монтируем папку static для картинок, шрифтов и т.д.
app.mount("/static", StaticFiles(directory=static_path), name="static")

# Монтируем сам сайт для HTML/JS/CSS
site_path = static_path / "www.nfactorial.school"
app.mount("/www.nfactorial.school", StaticFiles(directory=site_path), name="site")

index_file = site_path / "index.html"

@app.get("/")
async def root():
    return RedirectResponse(url="/www.nfactorial.school/index.html")

@app.get("/{full_path:path}", response_class=HTMLResponse)
async def spa_fallback(full_path: str):
    requested_file = site_path / full_path
    try:
        requested_file.resolve().relative_to(site_path)
    except ValueError:
        raise HTTPException(status_code=403, detail="Доступ запрещен")

    if requested_file.is_file():
        return FileResponse(requested_file)

    # SPA маршруты
    spa_paths = ["b2b", "blog", "courses"]
    if any(full_path.startswith(p) for p in spa_paths):
        return FileResponse(index_file)

    raise HTTPException(status_code=404)
