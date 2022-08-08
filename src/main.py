from fastapi import FastAPI

from src.controllers import auth_controller, user_controller


app = FastAPI(title='Finance API')


app.include_router(auth_controller.router)
app.include_router(user_controller.router)
