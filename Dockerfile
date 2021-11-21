FROM python:3.7

RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt --proxy=xx.xx.xx.xx:xxxx

EXPOSE 5000
CMD ["python", "/app/app.py"]
