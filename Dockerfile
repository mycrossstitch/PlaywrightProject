# Используем официальный Python образ
FROM python:3.11-slim

# Устанавливаем системные зависимости для Playwright
RUN apt-get update && apt-get install -y --no-install-recommends \
    # Минимальные зависимости для Chromium
    libnss3 \
    libnspr4 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libdbus-1-3 \
    libxkbcommon0 \
    libatspi2.0-0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    # Шрифты
    fonts-liberation \
    # Для работы с сетью
    wget \
    curl \
    ca-certificates \
    # Для распаковки
    unzip \
    # Для Java (Allure) - минимальная JRE
    default-jre \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы зависимостей
COPY requirements.txt .

# Устанавливаем Python зависимости
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Устанавливаем Playwright браузеры
RUN playwright install --with-deps chromium
RUN playwright install-deps chromium

# Устанавливаем Allure командную строку
ENV ALLURE_VERSION=2.29.0
RUN curl -sL https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/${ALLURE_VERSION}/allure-commandline-${ALLURE_VERSION}.tgz \
    | tar -xz -C /opt/ && \
    ln -s /opt/allure-${ALLURE_VERSION}/bin/allure /usr/local/bin/allure


# Создаем директорию для отчетов
RUN mkdir -p /app/allure-results /app/allure-report

# Чистка кэша
RUN apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /tmp/* /var/tmp/*

# Устанавливаем переменные окружения
ENV PYTHONPATH=/app
ENV ALLURE_RESULTS_PATH=/app/allure-results
ENV ALLURE_REPORT_PATH=/app/allure-report

# Указываем команду по умолчанию
CMD ["bash"]
