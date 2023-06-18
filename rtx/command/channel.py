from typing import Literal

from rtx.command.base import RtxCommandBase
from rtx.types import RtxCommandIdentifier


class RtxTxRxCommand(RtxCommandBase):
    __word: int

    def __init__(
        self,
        identifier: Literal[
            RtxCommandIdentifier.channel0_tx_rx, RtxCommandIdentifier.channel1_tx_rx
        ],
    ) -> None:
        self.__word = 0
        super().__init__(identifier)

    def get_word(self) -> int:
        return self.__word

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
