FROM python:3.8

COPY ./app /app
WORKDIR /app

# EXPOSE 4000

RUN pip install -r requirements.txt
# CMD [ "python app.py" ]
