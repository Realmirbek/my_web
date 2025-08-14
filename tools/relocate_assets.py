import os
import re

ROOT = os.path.join(os.path.dirname(__file__), "..", "nfactorial")

# Ищем именно /static/site/framerusercontent.com
replacements = {
    r"/static/site/framerusercontent\.com": "framerusercontent.com"
}

exts = {".html", ".htm", ".css", ".js", ".mjs", ".json"}


def process_file(path):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            data = f.read()

        original = data
        total_replacements = 0

        for pattern, repl in replacements.items():
            data, count = re.subn(pattern, repl, data)
            total_replacements += count

        if total_replacements > 0:
            with open(path, "w", encoding="utf-8") as f:
                f.write(data)
            print(f"rewritten: {path} ({total_replacements} replacements)")

    except Exception as e:
        print(f"skip: {path} ({e})")


for root, _, files in os.walk(ROOT):
    for name in files:
        if os.path.splitext(name)[1].lower() in exts:
            process_file(os.path.join(root, name))
