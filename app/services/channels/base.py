from abc import ABC, abstractmethod

class BaseChannel(ABC):
    @abstractmethod
    def send(self, dados: dict):
        pass