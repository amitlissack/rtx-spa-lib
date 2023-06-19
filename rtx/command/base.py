from abc import ABC, abstractmethod


class RtxCommandBase(ABC):
    @abstractmethod
    def get_bytes(self) -> bytes:
        ...
