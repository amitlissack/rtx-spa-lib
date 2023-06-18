from abc import ABC, abstractmethod

from rtx.types import RtxCommandIdentifier
from rtx.util import to_rtx_spa_command


class RtxCommandBase(ABC):
    __identifier: RtxCommandIdentifier

    def __init__(self, identifier: RtxCommandIdentifier) -> None:
        self.__identifier = identifier
        self.__word = 0

    @abstractmethod
    def get_word(self) -> int:
        ...

    def command(self) -> int:
        """Build the RTX command for transmission

        :return: The command
        """
        return to_rtx_spa_command(command=self.__identifier, arinc_word=self.get_word())
