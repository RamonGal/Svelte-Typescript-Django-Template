# pull official base image
FROM python:3.10

# set work directory

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update
RUN apt-get install -y libpq-dev python3-pip python-dev postgresql postgresql-contrib netcat locales
# RUN sed -i -e 's/# fr_FR.UTF-8 UTF-8/fr_FR.UTF-8 UTF-8/' /etc/locale.gen && \
#     dpkg-reconfigure --frontend=noninteractive locales

# ENV LANG fr_FR.UTF-8
# ENV LC_ALL fr_FR.UTF-8
# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .

RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh


# create the appropriate directories for staticfiles

# copy project
COPY . .

# staticfiles
RUN python manage.py collectstatic --no-input --clear -i node_modules


# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
