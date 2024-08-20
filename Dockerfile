FROM python:3.11

#App directory
WORKDIR /app

#set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the project to app directory
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Run the Django 
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
