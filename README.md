# Daily Bible Verse – Django Project

This Django-based web application delivers a daily Bible verse to users using the open and free [HelloAO Bible API](https://bible.helloao.org/docs/guide/). The project is designed to provide consistent, reliable access to daily scripture with minimal setup and maximum flexibility.

---

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

