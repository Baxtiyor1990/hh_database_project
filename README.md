# Проект "hh_database_project"

Этот проект представляет собой базу данных для хранения данных о компаниях и вакансиях, полученных с помощью API HeadHunter.

## Структура проекта

- `data_loader.py`: скрипт для загрузки данных о компаниях и вакансиях в базу данных.
- `db_manager.py`: модуль для управления базой данных (запросы к базе данных).
- `hh_scraper.py`: скрипт для получения данных о вакансиях с использованием API HeadHunter.
- `database_setup.sql`: SQL-скрипт для настройки схемы базы данных PostgreSQL.

## Использование

1. **Загрузка данных:**
   - Запустите `data_loader.py` для загрузки данных о компаниях и вакансиях в базу данных.

2. **Управление базой данных:**
   - Используйте `db_manager.py` для выполнения запросов к базе данных (например, получение информации о компаниях и вакансиях).

3. **Получение данных о вакансиях:**
   - `hh_scraper.py` используется для получения данных о вакансиях с помощью API HeadHunter.

## Требования

- Python 3.x
- Библиотеки: psycopg2, requests

## Настройка

1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
Запуск
Загрузите данные в базу данных:
python data_loader.py
Запустите основной скрипт для управления базой данных:
python main.py
Автор
Baxtiyor1990