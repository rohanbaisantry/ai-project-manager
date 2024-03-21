FROM node:18.15.0

# Set the working directory
WORKDIR /opt/app

# Copy package files for dependency management
COPY frontend/package.json .
COPY frontend/package-lock.json .

# Install the packages declared in package.json or package-lock.json
RUN npm ci

RUN cat package.json

# Copy project files
COPY frontend/ .

# Expose the appropriate port
EXPOSE 5173
