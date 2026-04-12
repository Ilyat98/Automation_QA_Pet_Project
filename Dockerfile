FROM python:3.11

WORKDIR /app


RUN mkdir -p /etc/apt/keyrings \
    && curl -fsSL https://dl.google.com/linux/linux_signing_key.pub \
    | gpg --dearmor -o /etc/apt/keyrings/google-chrome.gpg \
    && echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main" \
    > /etc/apt/sources.list.d/google-chrome.list


RUN apt-get update && apt-get install -y google-chrome-stable

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN playwright install --with-deps

COPY . .

CMD ["pytest"]