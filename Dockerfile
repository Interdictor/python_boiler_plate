FROM python:3.6.6

ENV PYTHONPATH /opt/boiler/
WORKDIR $PYTHONPATH

RUN pip install pipenv

COPY Pipfile* $PYTHONPATH
RUN pipenv install --dev

COPY . $PYTHONPATH

CMD ["pipenv", "run", "up"]
