import pytest

from rtx.command.channel import RtxTxRxCommand
from rtx.types import ChannelCommand, RtxCommandIdentifier


@pytest.mark.parametrize(
    argnames=["channel", "word", "expected"],
    argvalues=[
        [
            RtxCommandIdentifier.channel0_tx_rx,
            0x87654321,
            bytes([0x83, 0x76, 0x2A, 0x0C, 0x42]),
        ],
        [
            RtxCommandIdentifier.channel1_tx_rx,
            0x87654321,
            bytes([0x87, 0x76, 0x2A, 0x0C, 0x42]),
        ],
    ],
)
def test_channel0(channel: ChannelCommand, word: int, expected: bytes) -> None:
    """It should build the command correctly."""
    assert (
        RtxTxRxCommand(identifier=channel).word(arinc29_word=word).get_bytes()
        == expected
    )
