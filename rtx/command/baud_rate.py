from rtx.command.base import RtxCommandBase
from rtx.types import BaudRateCommand, RtxConfiguration, RtxCommandIdentifier


class RtxBaudRateCommand(RtxCommandBase):
    __baud_rate: BaudRateCommand

    def __init__(self):
        self.__baud_rate = RtxConfiguration.baud_rate_9600

    def baud_rate(self, baud_rate: BaudRateCommand) -> "RtxBaudRateCommand":
        self.__baud_rate = baud_rate
        return self

    def get_bytes(self) -> bytes:
        # bits 1-3 or b010
        cmd_byte = RtxCommandIdentifier.configure << 1
        # bits 4-7 are baud rate
        cmd_byte |= self.__baud_rate << 4
        # lsb is 1
        cmd_byte |= 1
        return bytes([cmd_byte, cmd_byte])
