from fastapi import APIRouter

demo = APIRouter()
tag = "demo"


@demo.get(
    path="/demo1",
    tags=[tag],
    summary="demo1",
    description="demo1描述",
    deprecated=False
)
async def root():
    return {"message": "Hello World"}


@demo.get(
    path="/demo2/{name}",
    tags=[tag],
    summary="demo2",
    description="demo2描述",
    deprecated=False
)
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
