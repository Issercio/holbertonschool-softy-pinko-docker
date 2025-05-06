FROM ubuntu:latest

# Update APT package lists
RUN apt-get update

# Upgrade installed packages
RUN apt-get upgrade -y

# Install Python3 and pip3
RUN apt-get install -y python3 python3-pip

# Fix for externally managed environment error
RUN rm /usr/lib/python*/EXTERNALLY-MANAGED

# Install Flask using pip3
RUN pip3 install flask

RUN pip3 install flask-cors

# Set working directory
WORKDIR /app

# Copy Flask application to container
COPY api.py /app/

# Command to run Flask server
CMD ["python3", "api.py"]