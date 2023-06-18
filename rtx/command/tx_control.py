from rtx.command.base import RtxCommandBase
from rtx.types import RtxParity, RtxArincSpeed, RtxCommandIdentifier, ChannelType


class RtxTxControlCommand(RtxCommandBase):
    __channel: ChannelType
    __parity_enable: bool
    __parity_value: RtxParity
    __arinc_speed: RtxArincSpeed

    def __init__(self):
        self.__channel = 0
        self.__parity_enable = False
        self.__parity_value = RtxParity.odd
        self.__arinc_speed = RtxArincSpeed.high

    def channel(self, channel: ChannelType) -> "RtxTxControlCommand":
        """Set the channel."""
        self.__channel = channel
        return self

    def enable_parity(self) -> "RtxTxControlCommand":
        """Enable parity."""
        self.__parity_enable = True
        return self

    def disable_parity(self) -> "RtxTxControlCommand":
        """Disable parity."""
        self.__parity_enable = False
        return self

    def parity(self, method: RtxParity) -> "RtxTxControlCommand":
        """Set the parity method."""
        self.__parity_value = method
        return self

    def speed(self, speed: RtxArincSpeed) -> "RtxTxControlCommand":
        """Set the arinc speed."""
        self.__arinc_speed = speed
        return self

    def get_word(self) -> bytes:
        """Create the arinc word.

        :return: 32 bit word.
        """
        # bit 7 is 0 if high speed
        # bit 6 is 0 if odd parity
        # bit 5 is 0 if parity enabled
        # bits 3-4 is channel
        # bits 0-2 are b001
        cmd_byte = (self.__arinc_speed == RtxArincSpeed.low << 7) | (
            self.__parity_value == RtxParity.even << 6
        ) | (not self.__parity_enable << 5) | (self.__channel << 3) | (
            RtxCommandIdentifier.tx_control & 0x7
        ) < 1 | 0x1

        return bytes([cmd_byte, cmd_byte & 0xFE])
