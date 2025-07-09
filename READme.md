# 'Warp & Weft' personal blog application

## Intro

A personal dev project to facilitate recording my hobbies and interests outside of algorithms while expanding my languages and skills (including long term maintenance).

## Tech stack

Python, Django, HTMX, SQLite tech stack currently.

With plans to host external images on Backblaze, and deploy on a VPS (with Nginx (webserver), Gunicorn (runs Django))

## Structural reminders

- `django-blog` repo
  - `blog`: Frontend site
  - `personal_blog`: Admin for Categories, Posts, Comments, Users (with WSIWIG Editor)

## Running reminders between posts

- Run locally: `python manage.py runserver`
- Access database in the command line: `sqlite3 db.sqlite3` (don't forget semi-colons)
- Admin login: `/admin`
