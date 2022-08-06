from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index() -> None:
    return {'message': 'Finance API is running successfully'}
