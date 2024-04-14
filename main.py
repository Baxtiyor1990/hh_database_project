from db_utils import DBManager
from data_loader import load_data_into_database

def main():
    # Загрузка данных в базу данных
    load_data_into_database()

    # Инициализация менеджера базы данных
    db_manager = DBManager("mydatabase", "Baxtiyor", "18071990", "localhost", "5432")

    # Получение списка всех компаний и количества вакансий у каждой компании
    print("Companies and their vacancies count:")
    companies_vacancies_count = db_manager.get_companies_and_vacancies_count()
    for company, vacancy_count in companies_vacancies_count.items():
        print(f"{company}: {vacancy_count}")

    # Получение списка всех вакансий
    print("\nAll vacancies:")
    all_vacancies = db_manager.get_all_vacancies()
    for vacancy in all_vacancies:
        print(f"Company: {vacancy[0]}, Title: {vacancy[1]}, Salary: {vacancy[2]}, Link: {vacancy[3]}")

    # Получение средней зарплаты по вакансиям
    average_salary = db_manager.get_avg_salary()
    print(f"\nAverage Salary: {average_salary}")

    # Получение списка вакансий с зарплатой выше средней
    print("\nVacancies with salary higher than average:")
    higher_salary_vacancies = db_manager.get_vacancies_with_higher_salary()
    for vacancy in higher_salary_vacancies:
        print(f"Company: {vacancy[0]}, Title: {vacancy[1]}, Salary: {vacancy[2]}, Link: {vacancy[3]}")

    # Получение списка вакансий с ключевым словом в названии
    keyword = "python"
    print(f"\nVacancies with keyword '{keyword}':")
    keyword_vacancies = db_manager.get_vacancies_with_keyword(keyword)
    for vacancy in keyword_vacancies:
        print(f"Company: {vacancy[0]}, Title: {vacancy[1]}, Salary: {vacancy[2]}, Link: {vacancy[3]}")

    # Закрытие соединения с базой данных
    db_manager.close_connection()

if __name__ == "__main__":
    main()
