import pytest

from rtx.command.tx_control import RtxTxControlCommand
from rtx.types import ChannelType, RtxArincSpeed, RtxParity


@pytest.fixture
def subject() -> RtxTxControlCommand:
    return RtxTxControlCommand()


@pytest.mark.parametrize(
    argnames=["channel", "expected"],
    argvalues=[[0, bytes([0x01, 0x00])], [1, bytes([0x09, 0x08])]],
)
def test_channel(
    subject: RtxTxControlCommand, channel: ChannelType, expected: bytes
) -> None:
    """It should set the channel correctly."""
    assert subject.channel(channel).get_bytes() == expected


@pytest.mark.parametrize(
    argnames=["enabled", "expected"],
    argvalues=[[True, bytes([0x01, 0x00])], [False, bytes([0x21, 0x20])]],
)
def test_parity(subject: RtxTxControlCommand, enabled: bool, expected: bytes) -> None:
    """It should set the parity enabled bit correctly."""
    assert subject.parity(enabled=enabled).get_bytes() == expected


@pytest.mark.parametrize(
    argnames=["bit", "expected"],
    argvalues=[
        [RtxParity.odd, bytes([0x01, 0x00])],
        [RtxParity.even, bytes([0x41, 0x40])],
    ],
)
def test_parity_bit(
    subject: RtxTxControlCommand, bit: RtxParity, expected: bytes
) -> None:
    """It should set the parity bit correctly."""
    assert subject.parity_bit(bit=bit).get_bytes() == expected


@pytest.mark.parametrize(
    argnames=["speed", "expected"],
    argvalues=[
        [RtxArincSpeed.low, bytes([0x81, 0x80])],
        [RtxArincSpeed.high, bytes([0x01, 0x00])],
    ],
)
def test_speed(
    subject: RtxTxControlCommand, speed: RtxArincSpeed, expected: bytes
) -> None:
    """It should set the speed correctly."""
    assert subject.speed(speed).get_bytes() == expected
