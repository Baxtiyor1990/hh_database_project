from db_manager import DBManager

def main():
    db_manager = DBManager("mydatabase", "Baxtiyor", "18071990", "localhost", "5432")
    # Получить список всех компаний и количества вакансий у каждой компании
    companies_and_vacancies_count = db_manager.get_companies_and_vacancies_count()
    print("Companies and their vacancies count:")
    for company, vacancy_count in companies_and_vacancies_count.items():
        print(f"{company}: {vacancy_count} vacancies")

    # Получить список всех вакансий
    all_vacancies = db_manager.get_all_vacancies()
    print("\nAll vacancies:")
    for vacancy in all_vacancies:
        print(vacancy)

    # Получить среднюю зарплату по вакансиям
    avg_salary = db_manager.get_avg_salary()
    print(f"\nAverage salary across all vacancies: {avg_salary}")

    # Получить список вакансий с зарплатой выше средней
    high_salary_vacancies = db_manager.get_vacancies_with_higher_salary()
    print("\nVacancies with salary higher than average:")
    for vacancy in high_salary_vacancies:
        print(vacancy)

    # Получить список вакансий, в названии которых содержатся ключевые слова
    keyword = "python"
    keyword_vacancies = db_manager.get_vacancies_with_keyword(keyword)
    print(f"\nVacancies with keyword '{keyword}':")
    for vacancy in keyword_vacancies:
        print(vacancy)

if __name__ == "__main__":
    main()
