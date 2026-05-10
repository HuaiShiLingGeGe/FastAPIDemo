from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from app.request.router import demo

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router=demo,
                   prefix="/demo",
                   tags=["demo"]
                   )
