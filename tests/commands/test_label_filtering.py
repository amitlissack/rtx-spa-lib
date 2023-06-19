import pytest

from rtx.command import RtxLabelFilteringCommand


@pytest.fixture
def subject() -> RtxLabelFilteringCommand:
    return RtxLabelFilteringCommand()


@pytest.mark.parametrize(
    argnames=["channel", "enable", "all_labels", "one_label", "label", "expected"],
    argvalues=[
        [0, False, False, False, 100, bytes([0xF5, 0xF5, 0x00, 0x64])],
        [1, True, False, True, 22, bytes([0xF5, 0xF5, 0x68, 0x16])],
        [0, True, True, False, 200, bytes([0xF5, 0xF5, 0x30, 0x00])],
        [3, True, False, True, 0x1234, bytes([0xF5, 0xF5, 0x68, 0x34])],
    ],
)
def test_label_filtering(
    subject: RtxLabelFilteringCommand,
    channel: int,
    enable: bool,
    all_labels: bool,
    one_label: bool,
    label: int,
    expected: bytes,
) -> None:
    """It should create the command correctly."""
    assert (
        subject.channel(channel=channel)
        .enable(enable=enable)
        .all_labels(enabled=all_labels)
        .one_label(enabled=one_label)
        .label(label=label)
        .get_bytes()
        == expected
    )
