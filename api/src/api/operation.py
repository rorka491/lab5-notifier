from uuid import UUID
from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter
from src.services import OperationService
from shared.schemas.operations import OperationCreate, OperationRead

router = APIRouter(prefix="/operations")



@router.get(
    "/{id}",
    response_model=OperationRead
)
@inject
async def get_operation(
    id: UUID,
    service: FromDishka[OperationService]
):
    return await service.get_by_id(id)

@router.post("")
@inject
async def create_operation(
    data: OperationCreate,
    service: FromDishka[OperationService]
):
    await service.create(data)
