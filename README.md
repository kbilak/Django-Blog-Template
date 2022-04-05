# Django Blog Template

This repo can be used as a template for blog apps in django.

NOTE: this repo contains only the back-end without view templates.

## Features

- adding posts in admin panel - with ck text editor,
- category and tag can be assigned to post,
- user management - login, registration, password handling,
- comment and rating systems - each post can be commented and rated by the user,
- replies to comments,
- post searching,
- about, policy, cookies, contact pages etc.,
- multiple languages - django-parler,
- pagination,

## Technologies

- Django
- (Django modules)
- Docker
- PostgreSQL
- ...

## Config

For the template to work properly, you need to make some configuration settings yourself.

### Templates

In main app foleder create new folder and name it `Templates`.

In `Templates` folder create all folders and files from all views files from all apps folders.

For example:

In `posts` app folder there's `views` file. In `views` there's `index` function, which have the `views/index.html` parameter.

You need to provide `Templates` folder with new path to the `views/index.html` file.

### Translations

In order to add / delete language from the project you need to update the `config/settings.py` file.

In `Internationalization` section you can add and delete languages by example.

#### Rosetta

By going to the `127.0.0.1:8000/{language_code}/rosetta/` path you can translate the templates, models, urls etc.

### Pagination

For pagination to work properly, you need to equip your templates with the right elements:

```
{% for v in venues %}
...
{% endfor %}
```

And below that:

```
{% if venues.has_previous %}
    {{ venues.previous_page_number }}
{% endif %}
...

{% if venues.has_next %}
    {{ venues.next_page_number }}
{% endif %}
```

## Setup

```
docker-compose up -d --build
```
