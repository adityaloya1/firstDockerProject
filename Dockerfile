# Dockerfile, Image, Container
FROM alpine:latest

RUN apk update
RUN apk --update add python3

WORKDIR /home/data

COPY app.py ./
COPY IF.txt ./
COPY Limerick-1.txt ./

RUN cd ..
RUN mkdir output
RUN touch result.txt

RUN cd /home/data
CMD ["python3", "app.py"]
RUN cd ..
RUN cd output

CMD ["cat" , "result.txt"]