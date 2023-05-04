# base image
FROM python:3.10
# setup environment variable
ENV DockerHOME=/home/app
# set work directory
RUN mkdir -p $DockerHOME
# where your code lives 
WORKDIR $DockerHOME
# install dependencies
RUN pip install --upgrade pip
# copy whole project to your docker home directory
COPY . $DockerHOME
# run this command to install all dependencies
RUN pip install -r requirements.txt
# port where the django app runs
EXPOSE 443
# start server
CMD python manage.py runserver
