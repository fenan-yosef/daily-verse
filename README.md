# Daily Bible Verse – Django Project

This Django-based web application delivers a daily Bible verse to users using the open and free [HelloAO Bible API](https://bible.helloao.org/docs/guide/). The project is designed to provide consistent, reliable access to daily scripture with minimal setup and maximum flexibility.

---

## API Endpoints

All endpoints return JSON. All parameters are GET query params unless otherwise noted.

### 1. Daily Verse
`GET /api/verse/daily/?translation=kjv&theme=encouragement`

**Response:**
```json
{
  "reference": "Genesis 1:1",
  "text": "In the beginning God created the heavens and the earth.",
  "translation": "kjv",
  "book": "GEN"
}
```

### 2. Get Specific Verse
`GET /api/verse/<translation>/<book>/<chapter>/<verse>/`

**Response:**
```json
{
  "book": "GEN",
  "chapter": 1,
  "verse": 1,
  "text": "In the beginning God created the heavens and the earth.",
  "translation": "kjv"
}
```

### 3. Get Entire Chapter
`GET /api/chapter/<translation>/<book>/<chapter>/`

**Response:**
```json
{
  "book": "GEN",
  "chapter": 1,
  "verses": [
    {"verse": 1, "text": "..."},
    {"verse": 2, "text": "..."}
  ],
  "translation": "kjv"
}
```

### 4. Available Books and Chapters
`GET /api/books/`

**Response:**
```json
[
  {"name": "Genesis", "abbreviation": "GEN"}
]
```

`GET /api/books/<book>/chapters/`

**Response:**
```json
{
  "book": "GEN",
  "chapters": 50
}
```

### 5. Search Verse by Keyword
`GET /api/search/?q=faith&translation=kjv`

**Response:**
```json
[
  {
    "reference": "Hebrews 11:1",
    "text": "Now faith is the substance of things hoped for...",
    "translation": "kjv"
  }
]
```

### 6. Commentaries
`GET /api/commentaries/`

**Response:**
```json
[
  {"id": 1, "name": "Matthew Henry"}
]
```

`GET /api/commentaries/<commentary_id>/<book>/<chapter>/<verse>/`

**Response:**
```json
{
  "commentary": "Matthew Henry",
  "text": "Commentary text here...",
  "reference": "Genesis 1:1"
}
```

### 7. Verse of the Day Archive
`GET /api/verse/daily/archive/?month=7&year=2025`

**Response:**
```json
[
  {
    "reference": "Genesis 1:1",
    "text": "...",
    "translation": "kjv",
    "book": "GEN",
    "date_shown": "2025-07-31"
  }
]
```

### 8. Get a Random Verse
`GET /api/verse/random/?translation=kjv`

**Response:**
```json
{
  "book": "GEN",
  "chapter": 1,
  "verse": 1,
  "text": "...",
  "translation": "kjv"
}
```

### 9. Health Check
`GET /api/health/`

**Response:**
```json
{ "status": "ok" }
```

## Overview

- **Project Name**: `src`
- **App Name**: `daily_verse_app`
- **Purpose**: Display one Bible verse per day using a selected public-domain translation.
- **API Source**: [HelloAO Bible API](https://bible.helloao.org/docs/guide/)

---

## Features

- Fetches Bible verses from the HelloAO JSON API
- Displays a daily verse, rotated by the day of the year or selected randomly. 
- Simple integration of translation selection and verse formatting
- Clean and extendable Django app structure

---

## Project Structure

```
daily-verse/
├── daily_verse_app/
│ ├── migrations/
│ │ └── init.py
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ └── views.py
├── src/
│ ├── pycache/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt
```

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone git@github.com:fenan-yosef/daily-verse.git
   cd daily-verse
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the development server:
   ```bash
   python manage.py runserver
   ```

---

