from uuid import UUID
from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter
from src.commands import CreateAccountCommand
from src.services import AccountService
from shared.schemas.accounts import AccountRead, AccountDetail, AccountCreate

router = APIRouter(prefix="/accounts")

@router.get(
    "/{id}",
    response_model=AccountDetail
)
@inject
async def get_account(
    id: UUID,
    service: FromDishka[AccountService]
):
    return await service.get_by_id(id)


@router.post(
    "",
    response_model=AccountRead
)
@inject
async def create_account(
    data: AccountCreate,
    command: FromDishka[CreateAccountCommand]
):
    return await command.execute(data)
