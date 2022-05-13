FROM python:3.8
ADD ./actividad /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python app.py