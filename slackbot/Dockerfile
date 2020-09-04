FROM python:3.6.4-jessie
ADD source /source
WORKDIR /source
RUN pip install -r requirements.txt
CMD ["python", "run.py"]