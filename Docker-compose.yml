# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Copy the Scores.txt file to the root of the container's filesystem
COPY Scores.txt /Scores.txt

# Set the command to run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
