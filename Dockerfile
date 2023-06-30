FROM python:3.11-slim-buster

LABEL maintainer="Mykola Filippenko mykolafilippenko@gmail.com"

ARG UID=1000
ARG GID=1000
ENV UID=${UID}
ENV GID=${GID}

RUN useradd -m -u $UID docker_user
USER docker_user

WORKDIR /home/docker_user/app

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "-m", "bot.main.py"]