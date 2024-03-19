# ai-project-manager
Project Management made easy using AI

### System Requirements

- Docker and Docker-Compose
- Note: It is recommended to use [OrbStack](https://orbstack.dev/) for MacOS X.

### Run Locally via Docker

```bash
docker-compose up --build
```

### Tech Stack
- Python
- Flask
- OpenAI
- Docker and Docker-Compose
- Jinja2
- MongoDB
- Poetry


### Installing the dependencies locally

```bash
pip install poetry
poetry install --with development
```

### How to contribute

- Create a new branch off of `main`
- Push your code to that branch
- Format the code using [black](https://github.com/psf/black) (You can run the command `black .` at the root of the
  repository.)
- Raise a PR against `main`
- Complete the PR checklist.
- Get it reviewed by one of the engineers
- Upon approval of the PR, merge it.
- Follow the deployment steps below to deploy if required.

### Setup the pre-commit hooks

Note: This has to be done only once when you setup the repo and it requires you to install the dependencies locally.

```bash
pre-commit install
```

### Connect to OpenAI from your local

To connect to OpenAI from your local, you have two methods, either you connect to it using your OpenAI Api Key and you use something like [LM Studio](https://lmstudio.ai/) and run something locally to simulate the OpenAI API
