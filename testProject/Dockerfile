FROM python:3.9
RUN pip install django
WORKDIR /app
RUN yes | apt update -y
RUN yes | apt install binutils libproj-dev gdal-bin
RUN yes | apt clean
RUN pip install psycopg2-binary
COPY ./ /app
# RUN python manage.py makemigrations
RUN python manage.py migrate
CMD [ "python3" ,"manage.py" ,"runserver" ,"0.0.0.0:8000", "--reload"]