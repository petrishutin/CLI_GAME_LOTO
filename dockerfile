FROM python:3.7.7-slim

WORKDIR ./app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["sh", "script.sh"]