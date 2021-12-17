FROM python:3.9.9
WORKDIR /blogpath
ENV PYTHONPATH "${PYTHONPATH}:/app/python/bin"
COPY requirements.txt requirements.txt
RUN pip install -r "requirements.txt"
COPY . .
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]