FROM python:3.12-slim

WORKDIR /app
# Copy the rest of the application
COPY . .

# Install the requirements file
RUN pip3 install --requirement=./requirements.txt