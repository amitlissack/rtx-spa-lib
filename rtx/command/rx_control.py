from typing import Literal

from rtx.command.base import RtxCommandBase
from rtx.types import RtxParity, RtxArincSpeed, RtxCommandIdentifier, ChannelType


class RtxRxControlCommand(RtxCommandBase):
    __channel: ChannelType
    __parity_stuffing: bool
    __arinc_speed: RtxArincSpeed

    def __init__(self):
        self.__channel = 0
        self.__parity_stuffing = False
        self.__arinc_speed = RtxArincSpeed.high
        super().__init__(identifier=RtxCommandIdentifier.rx_control)

    def channel(self, channel: ChannelType) -> "RtxRxControlCommand":
        """Set the channel."""
        self.__channel = channel
        return self

    def parity_stuffing(self, enable: bool) -> "RtxRxControlCommand":
        """Disable parity."""
        self.__parity_stuffing = enable
        return self

    def speed(self, speed: RtxArincSpeed) -> "RtxRxControlCommand":
        """Set the arinc speed."""
        self.__arinc_speed = speed
        return self

    def get_word(self) -> int:
        """Create the arinc word.

        :return: 32 bit word.
        """
        # bit 7 is 0 if high speed
        # bit 6 is 0 if parity stuffing enabled
        # bits 4-5 is channel
        # bits 0-3 are b1101
        cmd_byte = (
            (self.__arinc_speed == RtxArincSpeed.low << 7)
            | (not self.__parity_stuffing << 6)
            | (self.__channel << 4)
            | 0xD
        )

        return (cmd_byte << 24) | (cmd_byte << 16)
