FROM python:3.9.9
WORKDIR /blog
ENV PYTHONPATH "${PYTHONPATH}:/app/python/bin"
ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip3 install -r "requirements.txt"
COPY . .
EXPOSE 5000
ENTRYPOINT ["flask", "run"]