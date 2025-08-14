import os
import re
from bs4 import BeautifulSoup

PROJECT_DIR = "nfactorial/static"
EXTERNAL_DOMAINS = [
    "fonts.gstatic.com",
    "framerusercontent.com",
    "i.ytimg.com",
    "logo.clearbit.com",
    "www.googletagmanager.com",
]


def is_text_file(file_path):
    """Проверяем, является ли файл текстовым по расширению"""
    text_extensions = ['.html', '.htm', '.css', '.js', '.mjs', '.txt']
    return any(file_path.lower().endswith(ext) for ext in text_extensions)


def process_css_content(content, file_path):
    """Обрабатывает CSS-контент, заменяя URL"""

    def replace_url(match):
        url = match.group(1).strip('\'"')
        if "www.nfactorial.school" in url:
            local_path = re.sub(r'^https?://www\.nfactorial\.school', '', url)
            return f"url('/static{local_path}')"
        elif any(domain in url for domain in EXTERNAL_DOMAINS):
            return match.group(0)
        elif url.startswith(('http://', 'https://', 'data:', '#')):
            return match.group(0)
        else:
            return match.group(0)

    return re.sub(r"url\((.*?)\)", replace_url, content)


def process_html_file(file_path):
    """Обрабатывает HTML файлы, заменяя внешние ссылки на локальные пути"""
    if not is_text_file(file_path):
        print(f"Skipping non-text file: {file_path}")
        return

    try:
        # Пробуем разные кодировки
        for encoding in ['utf-8', 'latin-1', 'windows-1252', 'utf-16']:
            try:
                with open(file_path, "r", encoding=encoding) as f:
                    content = f.read()
                break
            except UnicodeDecodeError:
                continue
        else:
            print(f"Failed to decode {file_path} with any encoding")
            return

        # Проверка, что файл похож на HTML
        if not content.lstrip().startswith(('<!DOCTYPE', '<html', '<!doctype')):
            print(f"File {file_path} doesn't appear to be valid HTML")
            return

        soup = BeautifulSoup(content, 'html.parser')
        modified = False

        # Обработка всех тегов с атрибутами src/href
        tags_to_process = {
            'link': 'href',
            'script': 'src',
            'img': 'src',
            'a': 'href',
            'iframe': 'src',
            'source': 'src',
            'use': 'xlink:href'
        }

        for tag, attr in tags_to_process.items():
            for element in soup.find_all(tag):
                if element.get(attr):
                    url = element[attr]
                    if "www.nfactorial.school" in url:
                        local_path = re.sub(r'^https?://www\.nfactorial\.school', '', url)
                        element[attr] = f'/static{local_path}'
                        modified = True
                    elif url.startswith('http') and not any(domain in url for domain in EXTERNAL_DOMAINS):
                        print(f"Found external resource in {file_path}: {url}")

        # Обработка style-тегов
        for style in soup.find_all('style'):
            if style.string:
                new_content = process_css_content(style.string, file_path)
                if new_content != style.string:
                    style.string.replace_with(new_content)
                    modified = True

        if modified:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(str(soup))
            print(f"Updated paths in {file_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")


def process_css_file(file_path):
    """Обрабатывает отдельные CSS файлы"""
    if not is_text_file(file_path):
        print(f"Skipping non-text file: {file_path}")
        return

    try:
        for encoding in ['utf-8', 'latin-1', 'windows-1252', 'utf-16']:
            try:
                with open(file_path, "r", encoding=encoding) as f:
                    content = f.read()
                break
            except UnicodeDecodeError:
                continue
        else:
            print(f"Failed to decode {file_path} with any encoding")
            return

        new_content = process_css_content(content, file_path)

        if new_content != content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated paths in {file_path}")

    except Exception as e:
        print(f"Error processing CSS {file_path}: {str(e)}")


# Основной цикл обработки файлов
for root, dirs, files in os.walk(PROJECT_DIR):
    for file in files:
        file_path = os.path.join(root, file)

        if file.endswith(".css"):
            process_css_file(file_path)
        elif file.endswith((".html", ".htm")):
            process_html_file(file_path)
        elif file.endswith(".js"):
            # Можно добавить обработку JS файлов при необходимости
            pass