import pytest

from rtx.command.rx_control import RtxRxControlCommand
from rtx.types import ChannelType, RtxArincSpeed


@pytest.fixture
def subject() -> RtxRxControlCommand:
    return RtxRxControlCommand()


@pytest.mark.parametrize(
    argnames=["channel", "expected"],
    argvalues=[[0, bytes([0x0D, 0x0D])], [1, bytes([0x1D, 0x1D])]],
)
def test_channel(
    subject: RtxRxControlCommand, channel: ChannelType, expected: bytes
) -> None:
    """It should set the channel correctly."""
    assert subject.channel(channel).get_bytes() == expected


@pytest.mark.parametrize(
    argnames=["parity_stuffing", "expected"],
    argvalues=[[True, bytes([0x0D, 0x0D])], [False, bytes([0x4D, 0x4D])]],
)
def test_parity(
    subject: RtxRxControlCommand, parity_stuffing: bool, expected: bytes
) -> None:
    """It should set the parity stuffing correctly."""
    assert subject.parity_stuffing(parity_stuffing).get_bytes() == expected


@pytest.mark.parametrize(
    argnames=["speed", "expected"],
    argvalues=[
        [RtxArincSpeed.low, bytes([0x8D, 0x8D])],
        [RtxArincSpeed.high, bytes([0x0D, 0x0D])],
    ],
)
def test_speed(
    subject: RtxRxControlCommand, speed: RtxArincSpeed, expected: bytes
) -> None:
    """It should set the speed correctly."""
    assert subject.speed(speed).get_bytes() == expected
