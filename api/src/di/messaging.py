from dishka import Provider, Scope, provide
from src.messaging.publisher import Publisher
from src.messaging.broker import broker


class MessagingProvider(Provider):

    @provide(scope=Scope.APP)
    def publisher(self) -> Publisher:
        return Publisher(broker=broker)
    