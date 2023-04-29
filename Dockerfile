FROM python:3.7-slim
# Set the working directory
WORKDIR /app

COPY . .

#COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set the FLASK_APP environment variable
ENV FLASK_APP=server.py

# Expose the port that the Flask app will listen on
EXPOSE 5000

# Start the Flask server
CMD python list_instances.py && flask run --host 0.0.0.0
