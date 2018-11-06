FROM python:3.6.6

ENV PYTHONPATH /opt/boiler/
WORKDIR $PYTHONPATH

RUN pip install pipenv

COPY Pipfile* .
RUN pipenv install --dev

COPY . .

CMD ["pipenv", "run", "python", "ops/run.py"]
