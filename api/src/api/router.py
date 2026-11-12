from fastapi import APIRouter
from src.api.operation import router as operation_router
from src.api.account import router as account_router

router = APIRouter(prefix="/api/v1")

router.include_router(operation_router)
router.include_router(account_router)
