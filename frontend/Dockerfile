FROM node:18.15.0

# Set the working directory
WORKDIR /opt/app

# Copy package files for dependency management
COPY frontend/package*.json .

# Install the packages declared in package.json or package-lock.json
RUN npm ci

# Copy project files
COPY frontend/ /opt/app

# Expose the appropriate port
EXPOSE 3000
