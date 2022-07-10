FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./req.txt .
RUN pip install -r req.txt

COPY . .

ENTRYPOINT ["/app/entrypoint.sh"]

EXPOSE 8000




#FROM python:3.10
#
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
#
#WORKDIR /usr/src/wherefilmed
#
#COPY ./req.txt /usr/src/req.txt
#RUN pip install -r /usr/src/req.txt
#
#COPY . /usr/src/wherefilmed
#
#EXPOSE 8000


