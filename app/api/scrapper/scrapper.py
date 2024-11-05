from fastapi import APIRouter

router = APIRouter(prefix="/scrapper", tags=["scrapper"])


@router.get("/")
async def root():
    return {"message": "Hello World from scrapper"}
