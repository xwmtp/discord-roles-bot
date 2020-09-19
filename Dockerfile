FROM python:3.8-slim-buster

RUN pip install discord pyYAML

COPY ./ /etc/discord-roles-bot

VOLUME ["/etc/discord-roles-bot/configuration", "/etc/discord-roles-bot/log"]

WORKDIR /etc/discord-roles-bot/discord-roles-bot
CMD ["python", "Main.py"]
