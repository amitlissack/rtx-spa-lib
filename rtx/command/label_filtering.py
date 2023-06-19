from rtx.command.base import RtxCommandBase
from rtx.types import RtxCommandIdentifier, RtxConfiguration


class RtxLabelFilteringCommand(RtxCommandBase):
    __channel: int
    __enable: bool
    __all_labels: bool
    __one_label: bool
    __label: int

    def channel(self, channel: int) -> "RtxLabelFilteringCommand":
        self.__channel = channel
        return self

    def enable(self, enable: bool) -> "RtxLabelFilteringCommand":
        self.__enable = enable
        return self

    def all_labels(self, enabled: bool) -> "RtxLabelFilteringCommand":
        self.__all_labels = enabled
        return self

    def one_label(self, enabled: bool) -> "RtxLabelFilteringCommand":
        self.__one_label = enabled
        return self

    def label(self, label: int) -> "RtxLabelFilteringCommand":
        self.__label = label
        return self

    def get_bytes(self) -> bytes:
        byte_a = (
            (RtxConfiguration.label_filtering << 4)
            | (RtxCommandIdentifier.configure << 1)
            | 1
        )
        byte_b = byte_a
        byte_c = (
            ((self.__channel & 0x1) << 6)
            | (self.__enable << 5)
            | (self.__all_labels << 4)
            | (self.__one_label << 3)
        )
        byte_d = (self.__label & 0xFF) if not self.__all_labels else 0
        return bytes([byte_a, byte_b, byte_c, byte_d])
