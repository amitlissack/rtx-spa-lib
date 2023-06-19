from rtx.command.base import RtxCommandBase
from rtx.types import ChannelCommand
from rtx.util import to_rtx_spa_command


class RtxTxRxCommand(RtxCommandBase):
    __word: int
    __identifier: ChannelCommand

    def __init__(
        self,
        identifier: ChannelCommand,
    ) -> None:
        self.__identifier = identifier
        self.__word = 0

    def get_bytes(self) -> bytes:
        return to_rtx_spa_command(command=self.__identifier, arinc_word=self.__word)

    def word(self, arinc29_word: int) -> "RtxTxRxCommand":
        self.__word = arinc29_word
        return self
