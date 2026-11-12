from shared.exceptions import ObjectNotFound
from fastapi import FastAPI, HTTPException, Request


def setup_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(ObjectNotFound)
    async def object_not_found_handler(
        request: Request,
        exc: ObjectNotFound,
    ):
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )