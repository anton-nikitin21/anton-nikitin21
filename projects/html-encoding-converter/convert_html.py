from __future__ import annotations

import re
from pathlib import Path

from charset_normalizer import from_bytes


BASE_DIR = Path(__file__).resolve().parent

SOURCE_DIR = BASE_DIR / "input_html"

OUTPUT_DIR = BASE_DIR / "output_utf8"

HTML_EXTENSIONS = {".htm", ".html"}


# ищет кодировку внутри HTML
CHARSET_SEARCH_RE = re.compile(
    rb"""charset\s*=\s*["']?\s*([a-zA-Z0-9._-]+)""",
    re.IGNORECASE,
)

# заменяет кодировку на utf-8
CHARSET_REPLACE_RE = re.compile(
    r"""charset\s*=\s*(?:"[^"]*"|'[^']*'|[a-zA-Z0-9._-]+)""",
    re.IGNORECASE,
)

# ищет тег <head>
HEAD_RE = re.compile(
    r"<head\b[^>]*>",
    re.IGNORECASE,
)

# приводит названия кодировок к нормальномк виду 
def normalize_encoding_name(encoding: str) -> str:

    normalized = encoding.strip().lower().replace("_", "-")

    aliases = {
        "utf8": "utf-8",
        "utf-8": "utf-8",
        "utf-8-sig": "utf-8-sig",
        "windows-1251": "cp1251",
        "win-1251": "cp1251",
        "win1251": "cp1251",
        "cp-1251": "cp1251",
        "cp1251": "cp1251",
        "1251": "cp1251",
        "koi8-r": "koi8-r",
        "koi8r": "koi8-r",
        "cp866": "cp866",
        "ibm866": "cp866",
    }

    return aliases.get(normalized, normalized)

# ищет кодировку в метачарсет
def find_declared_encoding(raw: bytes) -> str | None:
    

    match = CHARSET_SEARCH_RE.search(raw[:16_384])

    if match is None:
        return None

    try:
        encoding = match.group(1).decode("ascii")
    except UnicodeDecodeError:
        return None

    return normalize_encoding_name(encoding)


# определяет кодировку файла и декодирует его
def decode_html(raw: bytes) -> tuple[str, str]:
    

    # UTF-8 с BOM
    if raw.startswith(b"\xef\xbb\xbf"):
        return raw.decode("utf-8-sig"), "utf-8-sig"

    # UTF-16
    if raw.startswith((b"\xff\xfe", b"\xfe\xff")):
        return raw.decode("utf-16"), "utf-16"

    # сначала пробует обычный UTF-8
    try:
        return raw.decode("utf-8"), "utf-8"
    except UnicodeDecodeError:
        pass

    # затем пробуем кодировку из meta charset
    declared_encoding = find_declared_encoding(raw)

    if declared_encoding:
        try:
            return raw.decode(declared_encoding), declared_encoding
        except (UnicodeDecodeError, LookupError):
            pass

    # автоматическое определение
    detected = from_bytes(raw).best()

    if detected is not None and detected.encoding:
        detected_encoding = normalize_encoding_name(detected.encoding)

        try:
            return raw.decode(detected_encoding), detected_encoding
        except (UnicodeDecodeError, LookupError):
            pass

    # резервные кодировки для старых документов на русском
    for encoding in ("cp1251", "koi8-r", "cp866"):
        try:
            return raw.decode(encoding), encoding
        except UnicodeDecodeError:
            continue

    raise UnicodeError("не удалось определить кодировку файла")

# меняет существующию кодировку на UTF-8
def set_utf8_meta(text: str) -> str:
    

    if CHARSET_REPLACE_RE.search(text):
        return CHARSET_REPLACE_RE.sub(
            "charset=utf-8",
            text,
            count=1,
        )

    head_match = HEAD_RE.search(text)

    if head_match:
        position = head_match.end()

        return (
            text[:position]
            + '\n<meta charset="utf-8">'
            + text[position:]
        )

    return '<meta charset="utf-8">\n' + text

# собирает все HTML-файлы из входной папки
def collect_html_files() -> list[Path]:


    return sorted(
        path
        for path in SOURCE_DIR.rglob("*")
        if path.is_file()
        and path.suffix.lower() in HTML_EXTENSIONS
    )

# конвертирует один HTML-файл в UTF-8 и сохраняет
def process_file(source_file: Path) -> str:
    

    raw = source_file.read_bytes()

    text, original_encoding = decode_html(raw)

    text = set_utf8_meta(text)

    relative_path = source_file.relative_to(SOURCE_DIR)
    output_file = OUTPUT_DIR / relative_path

    output_file.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    output_file.write_text(
        text,
        encoding="utf-8",
        newline="\n",
    )

    return original_encoding


def main() -> None:
    SOURCE_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    html_files = collect_html_files()

    if not html_files:
        print("HTML-файлы не найдены.")
        print(f"Положи файлы в папку:\n{SOURCE_DIR}")
        input("\nНажми Enter для выхода...")
        return

    print(f"Исходная папка: {SOURCE_DIR}")
    print(f"Папка результата: {OUTPUT_DIR}")
    print(f"Найдено файлов: {len(html_files)}")
    print("-" * 70)

    successful = 0
    failed = 0

    for number, source_file in enumerate(html_files, start=1):
        relative_path = source_file.relative_to(SOURCE_DIR)

        try:
            encoding = process_file(source_file)
            successful += 1

            print(
                f"[{number}/{len(html_files)}] "
                f"[OK] {relative_path} | "
                f"{encoding} -> UTF-8"
            )

        except Exception as error:
            failed += 1

            print(
                f"[{number}/{len(html_files)}] "
                f"[ОШИБКА] {relative_path}: {error}"
            )

    print("-" * 70)
    print("Обработка завершена.")
    print(f"Успешно: {successful}")
    print(f"С ошибками: {failed}")
    print(f"Результат находится здесь:\n{OUTPUT_DIR}")

    input("\nНажми Enter для выхода...")


if __name__ == "__main__":
    main()