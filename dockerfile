FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    ca-certificates \
    fonts-liberation \
    libasound2 \
    libx11-xcb1 \
    libxss1 \
    libappindicator3-1 \
    libfontconfig1 \
    libfreetype6 \
    libx11-6 \
    libxext6 \
    libxcb1 \
    libgcc1 \
    libgconf-2-4 \
    libnspr4 \
    libnss3 \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y \
    chromium \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

ENV CHROME_BIN=/usr/bin/chromium

ENV CHROMEDRIVER_VERSION=114.0.5735.90

RUN wget -q https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip -O /tmp/chromedriver.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver && \
    rm /tmp/chromedriver.zip

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install pytest

COPY . .

CMD ["pytest"]