# Automation QA Pet Project

Automation testing project with **UI, API and database testing** using Python and Pytest.

This project uses modern tools like **Selenium, Playwright, API testing, Docker/CI**.

---

## Tech stack

* Python
* Pytest
* Selenium
* Playwright
* Requests
* Pydantic
* MySQL
* Docker / Docker Compose
* GitHub Actions
* Allure Reports
* Faker
* pytest-xdist

---

## What is covered in this project

### UI Tests

UI tests are implemented using **Selenium and Playwright**.

Features:

* Page Object Model
* navigation between pages
* product and basket validation
* positive and negative test scenarios

---

### API Tests

API tests are written using **requests**.

Features:

* service layer for API calls
* response validation using **Pydantic**
* payload factories
* positive and negative tests

---

### Database Tests

Simple tests that verify database data after API actions using **MySQL**.

---

## Project structure

```
api_tests/
ui_tests_selenium/
ui_tests_playwright/
db_tests/

.github/workflows/

docker-compose.yml
requirements.txt
```

---

## Run tests locally

```
pytest -v
```

Run tests in parallel:

```
pytest -n auto
```

---

## Run with Docker

```
docker compose up --build
```

This will start MySQL and run tests inside the container.

---

## Allure report

Run tests with report generation:

```
pytest --alluredir=allure-results
```

Open report:

```
allure serve allure-results
```

---

## CI

The project uses **GitHub Actions** to run tests automatically on push.

---