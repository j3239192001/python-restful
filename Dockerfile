FROM python:3.7-alpine3.8
WORKDIR /home/app
COPY ./app /home/app
RUN pip install -r requirements.txt
EXPOSE 8080
CMD python ./main.py