FROM python:3.11-slim

RUN apt update && apt upgrade -y && apt install -y libpq-dev gcc netcat-traditional

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY starter.sh .
COPY . .

#RUN chmod +x starter.sh
#ENTRYPOINT [ "/app/starter.sh" ]
