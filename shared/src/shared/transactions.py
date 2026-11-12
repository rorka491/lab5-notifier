from sqlalchemy.ext.asyncio import AsyncSession

class SQLAlchemyTransaction:

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def __aenter__(self):
        await self.session.begin()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if exc_type is not None:
            await self.session.rollback()
        else:
            await self.session.commit()
        