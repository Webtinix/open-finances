# Python 3.8 image
FROM python:3.8

# Env variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# Copy all files to /app
COPY . /app/

# Workspace directory
WORKDIR /app

# Update apt-get
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y netcat-openbsd gcc && \
    apt-get clean

# Copy requirements.txt to /app
COPY requirements.txt /app/

# Upgrade pip
RUN pip install --upgrade pip 

# Install all django project dependencies
RUN pip install -r requirements.txt  

# Run migrations
RUN python src/manage.py makemigrations
RUN python src/manage.py migrate

# Expose port 8080
EXPOSE 8000

CMD python src/manage.py runserver 0.0.0.0:8000