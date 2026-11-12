from dishka import make_async_container, Provider, provide, Scope
from dishka.integrations.fastapi import FastapiProvider
from dishka_faststream import FastStreamProvider
from src.repositories import StatsRepository
from src.services import AnalyticsService


class AppProvider(Provider):
    @provide(scope=Scope.APP)
    def repo(self) -> StatsRepository:
        return StatsRepository()

    @provide(scope=Scope.APP)
    def service(self, repo: StatsRepository) -> AnalyticsService:
        return AnalyticsService(repo)


def make_container():
    return make_async_container(
        AppProvider(),
        FastStreamProvider(),
        FastapiProvider()
    )
container = make_container()