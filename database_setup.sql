-- Создание таблицы companies для хранения данных о компаниях
CREATE TABLE IF NOT EXISTS companies (
    company_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    industry VARCHAR(255),
    location VARCHAR(255),
    description TEXT
);

-- Создание таблицы vacancies для хранения данных о вакансиях
CREATE TABLE IF NOT EXISTS vacancies (
    vacancy_id SERIAL PRIMARY KEY,
    company_id INTEGER NOT NULL,
    title VARCHAR(255) NOT NULL,
    salary VARCHAR(255),
    link VARCHAR(255),
    description TEXT,
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);

-- Создание индекса на поле company_id для таблицы vacancies
CREATE INDEX IF NOT EXISTS idx_company_id ON vacancies (company_id);
