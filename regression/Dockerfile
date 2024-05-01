# Use an official Python runtime as a parent image
FROM python:3.12

# Create a directory in the container and cd there
WORKDIR /app

# Copy the entire local folder into the container
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "-m", "streamlit", "run", "streamlitExampleRegression.py", "--server.port=5000"]
