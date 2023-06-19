import pytest

from rtx.command import RtxBaudRateCommand
from rtx.types import BaudRateCommand, RtxConfiguration


@pytest.fixture
def subject() -> RtxBaudRateCommand:
    return RtxBaudRateCommand()


@pytest.mark.parametrize(
    argnames=["baud_rate", "expected"],
    argvalues=[
        [RtxConfiguration.baud_rate_9600, bytes([0x05, 0x05])],
        [RtxConfiguration.baud_rate_19200, bytes([0x25, 0x25])],
        [RtxConfiguration.baud_rate_38400, bytes([0x45, 0x45])],
        [RtxConfiguration.baud_rate_57600, bytes([0x65, 0x65])],
        [RtxConfiguration.baud_rate_115200, bytes([0x85, 0x85])],
        [RtxConfiguration.baud_rate_230400, bytes([0xA5, 0xA5])],
        [RtxConfiguration.baud_rate_460800, bytes([0xC5, 0xC5])],
    ],
)
def test_baud_rate(
    subject: RtxBaudRateCommand, baud_rate: BaudRateCommand, expected: bytes
) -> None:
    """It should create the command correctly."""
    assert subject.baud_rate(baud_rate=baud_rate).get_bytes() == expected
