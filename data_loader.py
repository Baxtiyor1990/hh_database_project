import psycopg2
from hh_scraper import fetch_companies_data, fetch_vacancies_data

def load_data_into_database():
    # Получаем данные о компаниях и вакансиях
    companies_data = fetch_companies_data()
    vacancies_data = fetch_vacancies_data()

    # Подключение к базе данных
    conn = psycopg2.connect(dbname="mydatabase", user="Baxtiyor", password="18071990", host="localhost", port="5432")
    cur = conn.cursor()

    try:
        # Заполнение таблицы companies данными
        for company in companies_data:
            cur.execute("""
                INSERT INTO companies (name, industry, location, description)
                VALUES (%s, %s, %s, %s)
            """, (company.get('name'), company.get('industry'), company.get('location'), company.get('description')))

        # Заполнение таблицы vacancies данными
        for vacancy in vacancies_data:
            company_id = vacancy.get('company_id')
            title = vacancy.get('title')
            salary = vacancy.get('salary')
            link = vacancy.get('link')
            description = vacancy.get('description')

            # Обработка значения salary
            if salary == "No salary info":
                salary = None  # Или другое значение, которое нужно использовать в случае отсутствия информации о зарплате

            cur.execute("""
                INSERT INTO vacancies (company_id, title, salary, link, description)
                VALUES (%s, %s, %s, %s, %s)
            """, (company_id, title, salary, link, description))

        # Завершение транзакции и сохранение изменений
        conn.commit()
        print("Данные успешно загружены в базу данных.")
    except Exception as e:
        conn.rollback()
        print(f"Произошла ошибка при загрузке данных: {e}")
    finally:
        # Закрытие соединения
        cur.close()
        conn.close()

if __name__ == "__main__":
    load_data_into_database()
