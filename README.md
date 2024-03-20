# ai-project-manager
Project Management made easy using AI

### System Requirements

- Docker
- Docker-Compose

### Run Locally via Docker

```bash
docker-compose up --build
```

### How to contribute

- Create a new branch off of `main`
- commit normally and don't use the `--no-verify` flag so that the pre-commit hooks run properly and format your code.
- Push your code to that branch
- Raise a PR against `main`
- Complete the PR checklist.
- Get it reviewed
- Upon approval of the PR, merge it.

### Setup the pre-commit hooks

Note: This has to be done only once when you setup the repo and it requires you to install the dependencies locally.

```bash
pre-commit install
```

### Connect to OpenAI from your local

To connect to OpenAI from your local, you have two methods, either you connect to it using your OpenAI Api Key or you use something like [LM Studio](https://lmstudio.ai/) and run something locally to simulate the OpenAI API
