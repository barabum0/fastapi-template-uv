from fastapi import APIRouter

from app.types.requests.api.hi import HelloWorldRequest, HelloWorldResponse

router = APIRouter()


@router.post("/hi", description=":)")
async def hello_world(body: HelloWorldRequest) -> HelloWorldResponse:
    return HelloWorldResponse(greeting=f"Hello, {body.name}!")
