from abc import ABC, abstractmethod


DATETIME_FORMAT_STRING = "%Y-%m-%d %H:%M:%S %z %Z"


class ClassAdapter(ABC):
    @abstractmethod
    def serialize(self, value):
        pass
    @abstractmethod
    def deserialize(self, value):
        pass


class Engine(ABC):
    def __init__(self, entrypoint: str, images: ClassAdapter, containers: ClassAdapter):
        self.entrypoint = entrypoint
        self.images = images
        self.containers = containers