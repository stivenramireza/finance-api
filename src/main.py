from fastapi import FastAPI

from src.controllers import user_controller


app = FastAPI(title='Finance API')


@app.get(path='/', tags=['Home'])
def root() -> dict[str, any]:
    return {'message': 'Finance API is running successfully'}


app.include_router(user_controller.router)
