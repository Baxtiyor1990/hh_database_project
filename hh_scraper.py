import requests

def fetch_companies_data():
    companies = [
        "Яндекс",
        "Mail.ru Group",
        "JetBrains",
        "Ozon",
        "Sber",
        "Tinkoff",
        "Wildberries",
        "EPAM Systems",
        "Avito",
        "Lamoda"
    ]

    company_data = []

    for company in companies:
        # Здесь можно реализовать запрос к API для получения дополнительной информации о компании
        # В этом примере просто добавляем статические данные
        industry = "IT"
        location = "Москва"
        description = "Описание компании"

        company_data.append({
            "name": company,
            "industry": industry,
            "location": location,
            "description": description
        })

    return company_data

def fetch_vacancies_data():
    companies = [
        "Яндекс",
        "Mail.ru Group",
        "JetBrains",
        "Ozon",
        "Sber",
        "Tinkoff",
        "Wildberries",
        "EPAM Systems",
        "Avito",
        "Lamoda"
    ]

    vacancies = []

    for company in companies:
        url = "https://api.hh.ru/vacancies"
        params = {
            "text": f'Компания: {company}',  # Поиск по названию компании
            "area": 1,  # Москва (ID региона)
            "per_page": 10  # Количество вакансий на странице
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            for item in data["items"]:
                title = item["name"]
                salary = item["salary"]["from"] if item.get("salary") else "No salary info"
                link = item["alternate_url"]
                description = item["snippet"]["requirement"]

                vacancies.append({
                    "company": company,
                    "title": title,
                    "salary": salary,
                    "link": link,
                    "description": description
                })
        else:
            print(f"Failed to fetch vacancies for {company}. Status code: {response.status_code}")

    return vacancies

if __name__ == "__main__":
    vacancies = fetch_vacancies_data()
    for vacancy in vacancies:
        print(vacancy)
