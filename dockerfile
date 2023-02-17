FROM python:3.9-slim

WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the code into the container
COPY bot.py .

# Start the bot
CMD ["python", "bot.py"]
