FROM python:3.11.5-bullseye

# Retrieve latest list of available packages
RUN apt update && apt upgrade -y

# Upgrade pip to its latest version
RUN pip install --upgrade pip

# Install poetry to manage dependencies within Python.
RUN pip install poetry

# Set the working directory
WORKDIR /opt/app

# Copy poetry's files for dependency management
COPY backend/poetry.lock .
COPY backend/pyproject.toml .

# Install the packages declared in poetry.lock or pyproject.toml
RUN poetry config virtualenvs.create false
RUN poetry config installer.max-workers 15
RUN poetry install --no-dev

# Copy project files
COPY backend/ /opt/app

# Expose the appropriate port
EXPOSE 8000
