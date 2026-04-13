# Automation QA Pet Project

Portfolio automation testing project focused on practical QA skills: UI, API, and DB testing with Python and Pytest.

The goal of this project is to practice and demonstrate real-world QA automation skills across UI, API, and DB testing.

## Tech Stack

- Python 3.11
- Pytest
- Selenium
- Playwright
- Requests
- Pydantic
- PyMySQL + MySQL
- Docker + Docker Compose
- Allure Report
- GitHub Actions and GitLab CI

## Test Scope

- **UI Selenium**: page object flow, login, basket, product checks.
- **UI Playwright**: same core UI scenarios for cross-tool coverage.
- **API**: users endpoint CRUD-like checks and schema validation.
- **DB**: simple checks for user creation/query in MySQL.

## Project Structure

```text
.
├── api_tests/
│   ├── client/
│   ├── data/
│   ├── models/
│   ├── services/
│   ├── tests/
│   └── conftest.py
├── ui_tests_selenium/
│   ├── pages/
│   ├── tests/
│   └── conftest.py
├── ui_tests_playwright/
│   ├── pages/
│   ├── tests/
│   └── conftest.py
├── db_tests/
│   ├── init.sql
│   ├── db_client.py
│   ├── test_user_created_in_db.py
│   └── conftest.py
├── utils/
│   └── logging_config.py
├── .github/workflows/tests.yml
├── .gitlab-ci.yml
├── docker-compose.yml
├── Dockerfile
├── pytest.ini
└── requirements.txt
```

## Run Locally

1. Install dependencies:

```bash
pip install -r requirements.txt
playwright install --with-deps
```

2. Run all tests:

```bash
pytest
```

3. Run suite by suite (recommended for clarity):

```bash
pytest ui_tests_selenium
pytest ui_tests_playwright
pytest api_tests
pytest db_tests
```

## Run with Docker

```bash
docker compose up --build
```

This starts MySQL, then runs Selenium, Playwright, API, and DB suites sequentially in the `tests` container.

## Logs and Test Results

- Unified test run logs are written to `logs/` (mounted from container).
- Allure raw results are written to `allure-results/`.
- Logging format is centralized via `utils/logging_config.py`.
- Each test logs:
  - `PASSED <nodeid>`
  - `FAILED <nodeid>` with failure details

## Allure Reporting

Generate results during run:

```bash
pytest --alluredir=allure-results
```

Open report locally:

```bash
allure serve allure-results
```

Build static report:

```bash
allure generate allure-results -o allure-report --clean
```

## CI

- **GitHub Actions**: `.github/workflows/tests.yml`
  - runs `docker compose up --build`
  - uploads `allure-results` artifact
- **GitLab CI**: `.gitlab-ci.yml`
  - runs Docker-in-Docker job with the same compose flow
  - stores `logs/` and `allure-results/` artifacts

## Known Limitations

- A small number of tests are marked `xfail` for known external behavior issues.
- UI tests depend on external demo site stability and can be slower than API/DB tests.

## Author / Purpose

Created as a QA automation portfolio project to demonstrate practical test architecture, tooling familiarity, and CI-ready execution in a Dockerized environment.