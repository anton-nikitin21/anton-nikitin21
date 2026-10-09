# HTML Encoding Converter

Я разработал утилиты преобразования HTML в UTF-8: обнаружение кодировки, обновление charset и обработку с резервными копиями.

## Запуск

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python convert_html.py
```

## Устройство проекта

`convert_html.py`: читает `input_html/`, пишет в `output_utf8/`. `convert_html1.py`: вариант обработки с резервными копиями; перед запуском ознакомьтесь с его настройками. Рабочие документы и чужие HTML-материалы не включены.

Я публикую исходный код и необходимые пояснения к запуску.

## Автор

Антон Никитин — [anton-nikitin21](https://github.com/anton-nikitin21).
