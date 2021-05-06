FROM python:3.7

RUN pip install Django==3.1
RUN mkdir /app

CMD ["/bin/bash"]