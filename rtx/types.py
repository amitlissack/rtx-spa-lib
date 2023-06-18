from enum import Enum
from typing import Literal


class RtxCommandIdentifier(int, Enum):
    channel0_tx_rx = 1  # 001
    channel1_tx_rx = 3  # 011
    configure = 4  # 010
    tx_control = 0  # 000
    rx_control = 6  # 110


class RtxConfiguration(int, Enum):
    baud_rate_9600 = 0x0  # 0000
    baud_rate_19200 = 0x2  # 0010
    baud_rate_38400 = 0x4  # 0100
    baud_rate_57600 = 0x6  # 0110
    baud_rate_115200 = 0x8  # 1000
    baud_rate_230400 = 0xA  # 1010
    baud_rate_460800 = 0xC  # 1100
    enable_flow_control = 0x1  # 0001
    label_filtering = 0xF  # 1111


class RtxParity(int, Enum):
    odd = 0
    even = 1


class RtxArincSpeed(int, Enum):
    high = 0
    low = 1


ChannelType = Literal[0, 1]