from fastapi import APIRouter, HTTPException
from dishka.integrations.fastapi import inject, FromDishka
from src.repositories import StatsRepository



router = APIRouter()


@router.get("/stores")
@inject
async def get_stores(repository: FromDishka[StatsRepository]):
    return repository.get_all()


@router.get("/stores/{store_id}")
@inject
async def get_store(store_id: str, repository: FromDishka[StatsRepository]):
    stats = repository.get(store_id)

    if stats is None:
        raise HTTPException(status_code=404, detail="Store not found")

    return stats


@router.get("/stats")
@inject
async def get_stats(repository: FromDishka[StatsRepository]):
    return {"events_count": repository.get_events_count()}