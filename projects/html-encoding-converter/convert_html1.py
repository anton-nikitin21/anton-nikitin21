from __future__ import annotations

import re
import shutil
from datetime import datetime
from pathlib import Path

from charset_normalizer import from_bytes


BASE_DIR = Path(__file__).resolve().parent

HTML_EXTENSIONS = {".htm", ".html"}

BACKUP_PREFIX = "_html_backup_"

# папки, которые скрипт не будет проверять
SKIP_DIR_NAMES = {
    "UTF8",
    "output_utf8",
    "__pycache__",
    ".git",
    ".venv",
    "venv",
}


# ищет кодировку внутри HTML
CHARSET_BYTES_RE = re.compile(
    rb"""charset\s*=\s*["']?\s*([a-zA-Z0-9._-]+)""",
    re.IGNORECASE,
)

# заменяет кодировку на utf-8
CHARSET_TEXT_RE = re.compile(
    r"""charset\s*=\s*(?:"[^"]*"|'[^']*'|[a-zA-Z0-9._-]+)""",
    re.IGNORECASE,
)

# ищет тег <head>
HEAD_OPEN_RE = re.compile(
    r"<head\b[^>]*>",
    re.IGNORECASE,
)

HEAD_CLOSE_RE = re.compile(
    r"</head\s*>",
    re.IGNORECASE,
)

# ищет encoding в XML-заголовке
XML_ENCODING_RE = re.compile(
    r"""(<\?xml\b[^>]*\bencoding\s*=\s*)(["'])[^"']+\2""",
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

        "koi8r": "koi8-r",
        "koi8-r": "koi8-r",

        "ibm866": "cp866",
        "cp866": "cp866",
    }

    return aliases.get(normalized, normalized)

# ищет кодировку в метачарсет
def find_declared_encoding(raw: bytes) -> str | None:
   
    match = CHARSET_BYTES_RE.search(raw[:65_536])

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

    # UTF-16 с BOM
    if raw.startswith((b"\xff\xfe", b"\xfe\xff")):
        return raw.decode("utf-16"), "utf-16"

    # проверка обычного UTF-8
    try:
        return raw.decode("utf-8"), "utf-8"
    except UnicodeDecodeError:
        pass

    # кодировка, указанная внутри HTML
    declared_encoding = find_declared_encoding(raw)

    # автоматическое определение кодировки
    detected = from_bytes(raw).best()

    candidates: list[str] = []

    if detected is not None and detected.encoding:
        candidates.append(
            normalize_encoding_name(detected.encoding)
        )

    if declared_encoding:
        candidates.append(declared_encoding)

    # резервные кодировки для старых документов на русском
    candidates.extend(
        (
            "cp1251",
            "koi8-r",
            "cp866",
        )
    )

    checked: set[str] = set()

    for encoding in candidates:
        if encoding in checked:
            continue

        checked.add(encoding)

        try:
            return raw.decode(encoding), encoding
        except (UnicodeDecodeError, LookupError):
            continue

    raise UnicodeError(
        "не удалось определить исходную кодировку"
    )

# меняет существующию кодировку на UTF-8
def set_utf8_declaration(text: str) -> str:

    head_close = HEAD_CLOSE_RE.search(text)

    if head_close:
        header_end = head_close.end()
    else:
        header_end = min(len(text), 65_536)

    header = text[:header_end]
    remainder = text[header_end:]

# заменяет 

    header = XML_ENCODING_RE.sub(
        lambda match: (
            f"{match.group(1)}"
            f"{match.group(2)}"
            f"utf-8"
            f"{match.group(2)}"
        ),
        header,
    )

    # если чарсет уже существует, то заменяем его
    if CHARSET_TEXT_RE.search(header):
        header = CHARSET_TEXT_RE.sub(
            "charset=utf-8",
            header,
        )

        return header + remainder

    # если чарсет отсутствует, то добавляем его после <head>
    head_open = HEAD_OPEN_RE.search(header)

    if head_open:
        position = head_open.end()

        header = (
            header[:position]
            + '\n<meta charset="utf-8">'
            + header[position:]
        )

        return header + remainder

    # если <head> отсутствует,то добавляем meta в начало
    return '<meta charset="utf-8">\n' + text

# проверяет, находится ли файл в папке, которую нужно пропустить
def is_skipped(file_path: Path) -> bool:
    
    relative_parts = file_path.relative_to(
        BASE_DIR
    ).parts[:-1]

    return any(
        part in SKIP_DIR_NAMES
        or part.startswith(BACKUP_PREFIX)
        for part in relative_parts
    )

# рекурсивно ищет все файлы .htm и .html
def collect_html_files() -> list[Path]:
    
    return sorted(
        file_path
        for file_path in BASE_DIR.rglob("*")
        if file_path.is_file()
        and file_path.suffix.lower() in HTML_EXTENSIONS
        and not is_skipped(file_path)
    )

# создает резервную копию файла 
def create_backup(
    source_file: Path,
    backup_dir: Path,
) -> None:
    
    relative_path = source_file.relative_to(BASE_DIR)
    backup_file = backup_dir / relative_path

    backup_file.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    shutil.copy2(
        source_file,
        backup_file,
    )


def write_atomically(
    file_path: Path,
    data: bytes,
) -> None:
    """
    Безопасно записывает результат.

    Сначала создаёт временный файл,
    затем заменяет им оригинал.
    """

    temporary_file = file_path.with_name(
        file_path.name + ".utf8_tmp"
    )

    try:
        temporary_file.write_bytes(data)
        temporary_file.replace(file_path)

    finally:
        if temporary_file.exists():
            temporary_file.unlink()

# конвертирует один HTML-файл в UTF-8 и сохраняет
def process_file(
    source_file: Path,
    backup_dir: Path,
) -> tuple[str, str]:
   
    raw = source_file.read_bytes()
    text, source_encoding = decode_html(raw)
    fixed_text = set_utf8_declaration(text)

    # кодирует результат в настоящий UTF-8
    utf8_data = fixed_text.encode("utf-8")

    # если байты полностью совпадают, значит файл уже правильный
    if raw == utf8_data:
        return "skipped", source_encoding

    
    create_backup(
        source_file,
        backup_dir,
    )

    # заменяет исходный файл версией UTF-8
    write_atomically(
        source_file,
        utf8_data,
    )

    # если файл уже был UTF-8, но нужно исправить charset или BOM
    if source_encoding in {"utf-8", "utf-8-sig"}:
        return "meta", source_encoding

    return "converted", source_encoding


def main() -> None:

    # сначала собираем окончательный список файлов
    html_files = collect_html_files()

    if not html_files:
        print("Файлы .htm и .html не найдены.")
        print(f"Проверенная папка:\n{BASE_DIR}")

        input("\nНажми Enter для выхода...")
        return

    # отдельная резервная папка для каждого запуска
    backup_dir = BASE_DIR / (
        BACKUP_PREFIX
        + datetime.now().strftime("%Y%m%d_%H%M%S")
    )

    print(f"Папка сканирования: {BASE_DIR}")
    print(f"Найдено HTML-файлов: {len(html_files)}")
    print("-" * 80)

    skipped = 0
    metadata_fixed = 0
    converted = 0
    failed = 0

    for number, source_file in enumerate(
        html_files,
        start=1,
    ):
        relative_path = source_file.relative_to(BASE_DIR)

        try:
            status, source_encoding = process_file(
                source_file,
                backup_dir,
            )

            if status == "skipped":
                skipped += 1
                message = "уже UTF-8, изменений нет"

            elif status == "meta":
                metadata_fixed += 1
                message = "исправлен charset или удалён BOM"

            else:
                converted += 1
                message = f"{source_encoding} -> UTF-8"

            print(
                f"[{number}/{len(html_files)}] "
                f"[OK] {relative_path} | {message}"
            )

        except Exception as error:
            failed += 1

            print(
                f"[{number}/{len(html_files)}] "
                f"[ОШИБКА] {relative_path}: {error}"
            )

    print("-" * 80)
    print("Обработка завершена.")
    print(f"Без изменений: {skipped}")
    print(f"Исправлен charset/BOM: {metadata_fixed}")
    print(f"Перекодировано в UTF-8: {converted}")
    print(f"Ошибок: {failed}")

    if metadata_fixed or converted:
        print(f"Резервные копии:\n{backup_dir}")
    else:
        print(
            "Файлы не изменялись, "
            "резервная папка не создавалась."
        )

    input("\nНажми Enter для выхода...")


if __name__ == "__main__":
    main()