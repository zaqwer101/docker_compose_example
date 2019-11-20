FROM python:3.8
RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
RUN pip install flask uwsgi
USER uwsgi
WORKDIR /app
EXPOSE 9090 9191
COPY app /app

# CMD ["python", "flaskapp.py"]
CMD ["uwsgi", "--http", "0.0.0.0:9090", "--wsgi-file", "/app/flaskapp.py", \
 "--callable", "app", "--stats", "0.0.0.0:9191"] 
