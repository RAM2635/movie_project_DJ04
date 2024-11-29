# 🎥 Movie Project

**movie_project** — это Django-приложение для работы с фильмами. Приложение позволяет добавлять фильмы с описанием и отзывами, а также просматривать список добавленных фильмов.

## 📋 Функциональность

- Добавление фильма с его названием, описанием и отзывом.
- Просмотр списка добавленных фильмов.
- Удобный интерфейс с использованием Bootstrap для стилизации.

---

## 🛠 Технологии

Проект разработан с использованием:

- Python 3.11+
- Django 5.1.3
- Bootstrap 5

---

## 🚀 Установка и запуск проекта

### 1. Клонирование репозитория

Склонируйте репозиторий на свой компьютер:

```bash
git clone https://github.com/RAM2635/movie_project.git
cd movie_project
```

### 2. Создание виртуального окружения

Создайте виртуальное окружение и активируйте его:

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/Mac:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Установка зависимостей

Установите необходимые пакеты из `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Применение миграций

Выполните миграции для подготовки базы данных:

```bash
python manage.py migrate
```

### 5. Запуск сервера

Запустите сервер разработки:

```bash
python manage.py runserver
```

Проект будет доступен по адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📂 Структура проекта

```
movie_project/
├── films/                # Приложение для работы с фильмами
│   ├── migrations/       # Миграции базы данных
│   ├── templates/films/  # Шаблоны (HTML)
│   ├── admin.py          # Конфигурация панели администратора
│   ├── apps.py           # Настройки приложения
│   ├── forms.py          # Django-формы
│   ├── models.py         # Модели базы данных
│   ├── urls.py           # Маршруты приложения
│   ├── views.py          # Логика отображения
├── movie_project/        # Главный проект Django
│   ├── settings.py       # Настройки проекта
│   ├── urls.py           # Главные маршруты проекта
│   ├── wsgi.py           # Для деплоя
│   ├── asgi.py           # Для асинхронного сервера
├── manage.py             # Команда для управления проектом
├── requirements.txt      # Зависимости проекта
└── db.sqlite3            # База данных (SQLite)
```

---

## ✨ Пример использования

1. Перейдите на страницу добавления фильма: [http://127.0.0.1:8000/add/](http://127.0.0.1:8000/add/).
2. Заполните форму с названием фильма, описанием и отзывом, затем сохраните.
3. Просмотрите список добавленных фильмов на главной странице: [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## 🛡 Лицензия

Проект распространяется под лицензией MIT. Подробнее в [LICENSE](LICENSE).