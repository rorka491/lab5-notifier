from fastapi import FastAPI 
from dishka.integrations.fastapi import setup_dishka
from src.api.router import router
from src.exception_handlers import setup_exception_handlers
from src.di.container import container 
from src.lifespan import lifespan

app = FastAPI(lifespan=lifespan)
app.include_router(router)
setup_dishka(container, app)
setup_exception_handlers(app)