import json
from pathlib import Path


class Translator:
    def __init__(self, locale: str = "en"):
        self.locale = locale
        self.translations = self.load_translations(locale)

    def load_translations(self, locale: str):
        path = Path(__file__).parent.parent / "locales" / f"{locale}.json"
        if path.exists():
            with open(path, "r", encoding="utf-8") as file:
                return json.load(file)
        return {}

    def get(self, key: str, **kwargs):
        text = self.translations.get(key, key)
        return text.format(**kwargs)


translator = Translator()  # Default: English


def set_locale(locale: str):
    global translator
    translator = Translator(locale)
