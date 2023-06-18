from typing import Literal

from rtx.command.base import RtxCommandBase
from rtx.types import RtxCommandIdentifier, ChannelCommand
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

    def get_word(self) -> bytes:
        return to_rtx_spa_command(command=self.__identifier, arinc_word=self.__word)

    def word(self, arinc29_word: int) -> "RtxTxRxCommand":
        self.__word = arinc29_word
        return self


def create_rxtx_command_channel_0() -> RtxTxRxCommand:
    """Create a command for channel 0.

    :return: RtxTxRxCommand
    """
    return RtxTxRxCommand(identifier=RtxCommandIdentifier.channel0_tx_rx)


def create_rxtx_command_channel_1() -> RtxTxRxCommand:
    """Create a command for channel 1.

    :return: RtxTxRxCommand
    """
    return RtxTxRxCommand(identifier=RtxCommandIdentifier.channel1_tx_rx)
