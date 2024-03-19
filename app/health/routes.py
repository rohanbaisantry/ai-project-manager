from fastapi import APIRouter, Response

router = APIRouter(prefix="/health", tags=["health"])


@router.get("")
def health() -> Response:
    return Response(status_code=200, content="Server is running!")
