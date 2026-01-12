# 🚀 Playwright UI Test Automation Framework

[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)](https://playwright.dev/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Allure Report](https://img.shields.io/badge/Allure_Report-FF6A38?style=for-the-badge&logo=allure&logoColor=white)](https://docs.qameta.io/allure/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)

**Фреймворк для автоматизации UI-тестирования** веб-приложений с полным циклом CI/CD, интерактивными отчетами и поддержкой Docker.

📌 **Цель проекта**: Автоматизация тестирования элементов интерфейса на сайте [https://www.qa-practice.com](https://www.qa-practice.com) с генерацией детальных отчетов.

## ✨ Основные возможности

| Компонент | Поддержка | Описание |
|-----------|-----------|----------|
| ✅ **Браузерная автоматизация** | Playwright | Кросс-браузерное тестирование (Chromium, Firefox, WebKit) |
| ✅ **Интерактивные отчеты** | Allure Report | Детальные отчеты с историей выполнения, скриншотами и шагами |
| ✅ **CI/CD Pipeline** | GitHub Actions | Автоматический запуск тестов на каждый push |
| ✅ **Контейнеризация** | Docker | Изолированная среда выполнения тестов |
| ✅ **Архитектура** | Page Object Model | Чистая, поддерживаемая структура проекта |
| ✅ **Параллельный запуск** | Pytest-xdist | Ускорение выполнения тестов в 4 раза |
| ✅ **Автоматические скриншоты** | Custom Fixtures | Скриншоты при падении тестов |

## 🏗️ Покрытие функциональности

### 📋 Проверяемые элементы интерфейса

| Элемент | Статус | Примеры тестов |
|---------|--------|---------------|
| **📝 Input Fields** | ✅ Полное | Текстовые поля, email, password, валидация |
| **🖱️ Buttons** | ✅ Полное | Клики, состояния, доступность |
| **☑️ Checkboxes** | ✅ Полное | Одиночные, множественные, состояния |
| **📦 Dropdowns** | ✅ Полное | Select, мульти-селекты |
| **🖼️ iFrames** | ✅ Полное | Вложенные фреймы, взаимодействие |
| **🌀 Drag & Drop** | ✅ Полное | Перетаскивание элементов, изображений |
| **⚠️ Alerts/Dialogs** | ✅ Полное | Alert, Confirm, Prompt |

## 🏗️ Архитектура проекта

```
PlaywrightProject/
├── 📁 base/                    # Базовые классы Page Object  
├── 📁 pages/                  # Page Object Model
├── 📁 tests/                  # Тестовые сценарии
├── 📁 utils/                  # Вспомогательные утилиты
├── 📁 config/                 # Конфигурации
├── 📁 .github/workflows/      # GitHub Actions workflows
│   └── config.yml            # CI/CD пайплайн
├── 📁 allure-results/         # Результаты тестов для Allure
├── 📁 allure-report/          # Сгенерированные отчеты Allure
├── 📄 conftest.py            # Pytest фикстуры
├── 📄 pytest.ini             # Конфигурация Pytest + Allure
├── 📄 Dockerfile             # Docker контейнеризация
├── 📄 docker-compose.yml     # Docker Compose конфигурация
├── 📄 requirements.txt       # Python зависимости
└── 📄 README.md              # Документация проекта
```

## 🚀 Быстрый старт

### Вариант 1: Локальный запуск (рекомендуется для разработки)

```bash
# 1. Клонировать репозиторий
git clone https://github.com/your-username/PlaywrightProject.git
cd PlaywrightProject

# 2. Установить зависимости
pip install -r requirements.txt

# 3. Установить браузеры Playwright
playwright install chromium

# 4. Запустить тесты
pytest tests/ -v --alluredir=allure-results

# 5. Сгенерировать и открыть отчет
allure generate allure-results --clean -o allure-report
allure open allure-report
```

### Вариант 2: Запуск через Docker (для CI/CD)

```bash
# 1. Собрать Docker образ
docker-compose build

# 2. Запустить тесты
docker-compose up


```


**Преимущества Allure в проекте:**
- 📈 **История выполнения** - тренды и статистика
- 🖼️ **Авто-скриншоты** - при падениях тестов
- 🏷️ **Категоризация** - по фичам, стори, severity


## 🤖 CI/CD Pipeline (GitHub Actions)


**Результат CI/CD:** [https://https://mycrossstitch.github.io/PlaywrightProject/](https://mycrossstitch.github.io/PlaywrightProject/)


## 🏆 Ключевые преимущества

| Преимущество | Описание |
|-------------|----------|
| **🎯 Production-ready** | Готов к использованию в продакшн среде |
| **📊 Профессиональные отчеты** | Allure Report с историей и аналитикой |
| **🤖 Полная автоматизация** | CI/CD от commit до деплоя отчета |
| **🐳 Изоляция среды** | Docker для воспроизводимости |
| **⚡ Быстрое выполнение** | Параллельный запуск тестов |
| **🧩 Расширяемость** | Чистая архитектура POM |
| **🖼️ Визуальная отладка** | Скриншоты при падениях |
| **🌐 Кросс-браузерность** | Поддержка Chromium, Firefox, WebKit |


**⭐ Если этот проект был полезен, поставьте звезду на GitHub!**

[![GitHub Stars](https://img.shields.io/github/stars/your-username/PlaywrightProject?style=social)](https://github.com/your-username/PlaywrightProject/stargazers)


