FROM ubuntu:20.04
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY . /code/
RUN apt-get update -y
RUN  apt install pip -y
RUN pip freeze
RUN pip list
RUN pip install fastapi
RUN pip install uvicorn
RUN pip install requests
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
