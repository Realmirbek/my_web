import os, re

ROOT = os.path.join(os.path.dirname(__file__), "..", "nfactorial")

# ЗАМЕНИ на реальный корневой домен твоего зеркалимого сайта:
ORIG_SITE = "https://www.nfactorial.school/"

replacements = {
    # Всё, что шло на framerusercontent, теперь из /static/site/framerusercontent.com/...
    r"https://framerusercontent\.com": "/static/site/framerusercontent.com",
    # А всё, что шло на edit.framer.com — локально:
    r"https://edit\.framer\.com": "/static/site/edit.framer.com",
    # На всякий случай уберём абсолют на сам сайт (если встречается) → относительный корень
    re.escape(ORIG_SITE): "",
}

exts = {".html", ".htm", ".css", ".js", ".mjs", ".json"}

def process_file(path):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            data = f.read()
        original = data
        for pattern, repl in replacements.items():
            data = re.sub(pattern, repl, data)
        if data != original:
            with open(path, "w", encoding="utf-8") as f:
                f.write(data)
            print("rewritten:", path)
    except Exception as e:
        print("skip:", path, e)

for root, _, files in os.walk(ROOT):
    for name in files:
        if os.path.splitext(name)[1].lower() in exts:
            process_file(os.path.join(root, name))
