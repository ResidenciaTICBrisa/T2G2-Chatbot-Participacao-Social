FROM python:3.10.13-bullseye
COPY . .
LABEL authors="isaque"
RUN pip install rasa python-dotenv telebot
EXPOSE 5005
CMD ["python", "TelegramIntegration.py", "&"]
ENTRYPOINT ["top", "-b"]