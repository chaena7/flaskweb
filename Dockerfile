From python:3.8-slim

RUN apt-get update
RUN apt-get install -y --no-install-recommends

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
