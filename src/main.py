from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from src.controllers import (
    auth_controller,
    user_controller,
    restaurant_controller,
    transaction_controller,
)


app = FastAPI(
    title='Finance API', description='Finance API specs', version='1.0.0'
)


@app.get(path='/', tags=['home'])
def root() -> RedirectResponse:
    return RedirectResponse(url='/docs')


app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'OPTIONS'],
    allow_headers=['*'],
)

app.include_router(auth_controller.router)
app.include_router(user_controller.router)
app.include_router(restaurant_controller.router)
app.include_router(transaction_controller.router)
