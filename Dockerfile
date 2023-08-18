FROM python:3.7

# Set the working directory
WORKDIR /app

# Copy the entrypoint.sh script and grant execute permission
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Copy the Python script and grant execute permission
COPY test.py .
RUN chmod +x test.py

# Define the entrypoint script
ENTRYPOINT ["/entrypoint.sh"]
