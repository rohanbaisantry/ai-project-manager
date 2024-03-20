# ai-project-manager-api
The backend for the ai-project-manager app.

### Tech Stack
- Python
- Flask
- OpenAI
- MongoDB
- Poetry

### Installing the dependencies locally and running the api

```bash
pip install poetry
poetry install --with development
uvicorn app.api:api --host 0.0.0.0 --port --reload
```
