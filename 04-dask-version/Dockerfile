FROM python:3.11-slim

# Install system dependencies and build tools
RUN apt-get update && apt-get install -y \
    build-essential \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Create necessary directories
RUN mkdir /data /scripts /utils /scarf /results

# Copy the required directories and files
COPY ./scripts /scripts
COPY ./utils /utils
COPY ./scarf /scarf
COPY ./requirements.txt /requirements.txt

# Install dependencies and scarf
RUN pip install --no-cache-dir -r /requirements.txt && \
    cd /scarf && \
    pip install -e .

RUN  pip install --upgrade pip

# Create an entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# # Set PYTHONPATH properly
# ENV PYTHONPATH=/:/utils:/scarf

ENTRYPOINT ["/entrypoint.sh"]