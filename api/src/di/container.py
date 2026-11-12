from dishka.integrations.fastapi import FastapiProvider
from dishka import make_async_container
from src.di.sqlalchemy import SQLAlchemyProvider
from src.di.repositories import RepositoryProvider
from src.di.services import ServiceProvider
from src.di.messaging import MessagingProvider
from src.di.commands import CommandProvider



container = make_async_container(
    FastapiProvider(),
    SQLAlchemyProvider(),
    RepositoryProvider(),
    ServiceProvider(),
    MessagingProvider(),
    CommandProvider(),
)