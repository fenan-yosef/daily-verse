# Mapping from common abbreviations to jsdelivr book names
BOOK_NAME_MAP = {
    "GEN": "genesis",
    "EXO": "exodus",
    "LEV": "leviticus",
    "NUM": "numbers",
    "DEU": "deuteronomy",
    "JOS": "joshua",
    "JDG": "judges",
    "RUT": "ruth",
    "1SA": "1-samuel",
    "2SA": "2-samuel",
    "1KI": "1-kings",
    "2KI": "2-kings",
    "1CH": "1-chronicles",
    "2CH": "2-chronicles",
    "EZR": "ezra",
    "NEH": "nehemiah",
    "EST": "esther",
    "JOB": "job",
    "PSA": "psalms",
    "PRO": "proverbs",
    "ECC": "ecclesiastes",
    "SNG": "song-of-solomon",
    "ISA": "isaiah",
    "JER": "jeremiah",
    "LAM": "lamentations",
    "EZK": "ezekiel",
    "DAN": "daniel",
    "HOS": "hosea",
    "JOL": "joel",
    "AMO": "amos",
    "OBA": "obadiah",
    "JON": "jonah",
    "MIC": "micah",
    "NAM": "nahum",
    "HAB": "habakkuk",
    "ZEP": "zephaniah",
    "HAG": "haggai",
    "ZEC": "zechariah",
    "MAL": "malachi",
    "MAT": "matthew",
    "MRK": "mark",
    "LUK": "luke",
    "JHN": "john",
    "ACT": "acts",
    "ROM": "romans",
    "1CO": "1-corinthians",
    "2CO": "2-corinthians",
    "GAL": "galatians",
    "EPH": "ephesians",
    "PHI": "philippians",
    "COL": "colossians",
    "1TH": "1-thessalonians",
    "2TH": "2-thessalonians",
    "1TI": "1-timothy",
    "2TI": "2-timothy",
    "TIT": "titus",
    "PHM": "philemon",
    "HEB": "hebrews",
    "JAS": "james",
    "1PE": "1-peter",
    "2PE": "2-peter",
    "1JN": "1-john",
    "2JN": "2-john",
    "3JN": "3-john",
    "JUD": "jude",
    "REV": "revelation"
}

# Map translation codes to jsdelivr version codes
VERSION_MAP = {
    "kjv": "en-kjv",
    "asv": "en-asv",
    # add more as needed
}
import requests
from datetime import date
import random
from .models import Verse, ShownVerse
from django.db import transaction


# List of 100 daily verses (sample selection, can be customized)
DAILY_VERSES = [
    {"book": "GEN", "chapter": 1, "verse": 1},
    {"book": "PSA", "chapter": 23, "verse": 1},
    {"book": "ROM", "chapter": 8, "verse": 28},
    {"book": "JHN", "chapter": 3, "verse": 16},
    {"book": "ISA", "chapter": 40, "verse": 31},
    {"book": "PHI", "chapter": 4, "verse": 13},
    {"book": "PRO", "chapter": 3, "verse": 5},
    {"book": "MAT", "chapter": 6, "verse": 33},
    {"book": "JOS", "chapter": 1, "verse": 9},
    {"book": "HEB", "chapter": 11, "verse": 1},
    # ... add up to 100 references ...
]

JSDELIVR_VERSE_API_URL = "https://cdn.jsdelivr.net/gh/wldeh/bible-api/bibles/{version}/books/{book}/chapters/{chapter}/verses/{verse}.json"

class VerseManager:
    def __init__(self, translation="kjv", book=None):
        self.translation = translation
        self.book = book


    def get_daily_verse(self):
        # Pick a verse from the static list based on the day of the year
        today = date.today()
        idx = (today.timetuple().tm_yday - 1) % len(DAILY_VERSES)
        ref = DAILY_VERSES[idx]
        translation = (self.translation or "kjv").lower()
        version = VERSION_MAP.get(translation, f"en-{translation}")
        book_abbr = ref["book"].upper()
        book = BOOK_NAME_MAP.get(book_abbr, book_abbr.lower())
        url = JSDELIVR_VERSE_API_URL.format(
            version=version,
            book=book,
            chapter=ref["chapter"],
            verse=ref["verse"]
        )
        response = requests.get(url)
        if response.status_code == 200:
            try:
                data = response.json()
                return {
                    "book": book_abbr,
                    "chapter": ref["chapter"],
                    "verse": ref["verse"],
                    "text": data.get("text", "Verse not found."),
                    "translation": translation,
                    "reference": f"{book_abbr} {ref['chapter']}:{ref['verse']}"
                }
            except Exception:
                pass
        # fallback if API fails
        return {
            "book": book_abbr,
            "chapter": ref["chapter"],
            "verse": ref["verse"],
            "text": "Verse not found (API error).",
            "translation": translation,
            "reference": f"{book_abbr} {ref['chapter']}:{ref['verse']}"
        }

    def _get_or_fetch_verse(self):
        # Try to get a random verse not shown recently
        verses = Verse.objects.filter(translation=self.translation)
        if self.book:
            verses = verses.filter(book=self.book)
        shown_verses = ShownVerse.objects.filter(translation=self.translation, book=self.book).values_list('verse_id', flat=True)
        available = verses.exclude(id__in=shown_verses)
        if available.exists():
            verse = random.choice(list(available))
            return verse
        # If all verses shown, pick any
        if verses.exists():
            return random.choice(list(verses))
        # If no verses in DB, fetch from API
        return self.fetch_and_store_verse()

    def fetch_and_store_verse(self):
        params = {"translation": self.translation}
        if self.book:
            params["book"] = self.book
        response = requests.get(HELLOAO_API_URL, params=params)
        if response.status_code == 200:
            try:
                data = response.json()
            except Exception:
                return Verse(reference="N/A", text="Invalid response from API.", translation=self.translation, book=self.book)
            verse, _ = Verse.objects.get_or_create(
                reference=data.get("reference"),
                translation=self.translation,
                book=self.book,
                defaults={"text": data.get("text")}
            )
            return verse
        return Verse(reference="N/A", text="Verse not found (API error).", translation=self.translation, book=self.book)

    def _verse_to_dict(self, verse):
        return {
            "reference": verse.reference,
            "text": verse.text,
            "translation": verse.translation,
            "book": verse.book,
        }
        return key

    def set_translation(self, translation):
        self.translation = translation

    def set_book(self, book):
        self.book = book
