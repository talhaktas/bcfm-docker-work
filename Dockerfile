FROM python:3

WORKDIR /academy-demo

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "demo.py"]
