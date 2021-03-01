FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

EXPOSE 80
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]