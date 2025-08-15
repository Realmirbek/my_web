import os
import re

# Папка с HTML/JS/CSS файлов сайта
SITE_DIR = "nfactorial/static/www.nfactorial.school"

for root, dirs, files in os.walk(SITE_DIR):
    for file in files:
        if file.endswith((".html", ".js", ".css")):
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()

                new_content = content

                # Заменяем пути к картинкам
                new_content = re.sub(
                    r'www\.nfactorial\.school/framerusercontent\.com/images/',
                    '/static/framerusercontent.com/images/',
                    new_content
                )

                # Заменяем .jpeg на .jpg
                new_content = re.sub(r'\.jpeg', '.jpg', new_content, flags=re.IGNORECASE)

                # Заменяем пути к шрифтам
                new_content = re.sub(
                    r'www\.nfactorial\.school/fonts\.gstatic\.com/s/',
                    '/static/fonts.gstatic.com/s/',
                    new_content
                )

                if new_content != content:
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"[UPDATED] {path}")
                else:
                    print(f"[OK] {path} — изменений не было")

            except Exception as e:
                print(f"[FAILED] {path} -> {e}")
