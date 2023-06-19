from rtx.command.base import RtxCommandBase
from rtx.types import RtxParity, RtxArincSpeed, RtxCommandIdentifier, ChannelType


class RtxTxControlCommand(RtxCommandBase):
    __channel: ChannelType
    __parity_enable: bool
    __parity_value: RtxParity
    __arinc_speed: RtxArincSpeed

    def __init__(self):
        self.__channel = 0
        self.__parity_enable = True
        self.__parity_value = RtxParity.odd
        self.__arinc_speed = RtxArincSpeed.high

    def channel(self, channel: ChannelType) -> "RtxTxControlCommand":
        """Set the channel."""
        self.__channel = channel
        return self

    def parity(self, enabled: bool) -> "RtxTxControlCommand":
        """Enable parity."""
        self.__parity_enable = enabled
        return self

    def parity_bit(self, bit: RtxParity) -> "RtxTxControlCommand":
        """Set the parity method."""
        self.__parity_value = bit
        return self

    def speed(self, speed: RtxArincSpeed) -> "RtxTxControlCommand":
        """Set the arinc speed."""
        self.__arinc_speed = speed
        return self

    def get_bytes(self) -> bytes:
        """Create the arinc word.

        :return: 32 bit word.
        """
        # bit 7 is 0 if high speed
        speed = (self.__arinc_speed == RtxArincSpeed.low) << 7
        # bit 6 is 0 if odd parity
        parity_bit = (self.__parity_value == RtxParity.even) << 6
        # bit 5 is 0 if parity enabled
        parity_enable = (not self.__parity_enable) << 5
        # bits 3-4 is channel
        channel = self.__channel << 3
        # bits 0-2 are b001 for first byte and b000 for second
        command = (RtxCommandIdentifier.tx_control & 0x7) << 1
        cmd_byte = speed | parity_bit | parity_enable | channel | command

        return bytes([cmd_byte | 1, cmd_byte])
