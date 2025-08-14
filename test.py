import os
import re

static_root = "nfactorial/static"

# Список доменов/папок для локализации
domains = [
    "www.nfactorial.school",
    "framerusercontent.com",
    "fonts.gstatic.com",
    "i.ytimg.com",
    "logo.clearbit.com",
    "www.googletagmanager.com"
]

# Только текстовые расширения
text_extensions = (".html", ".js", ".css", ".mjs", ".json", ".txt")

pattern = re.compile(r'(["\'(])(' + '|'.join(domains) + r')([^"\')]+)(["\')])')

for root, dirs, files in os.walk(static_root):
    for file in files:
        if file.endswith(text_extensions):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except UnicodeDecodeError:
                print(f"Skipped (not UTF-8 text) {file_path}")
                continue

            new_content = pattern.sub(r'\1/static/\2\3\4', content)

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated paths in {file_path}")
