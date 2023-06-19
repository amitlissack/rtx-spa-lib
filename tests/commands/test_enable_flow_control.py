import pytest

from rtx.command import RtxEnableFlowControlCommand


@pytest.fixture
def subject() -> RtxEnableFlowControlCommand:
    return RtxEnableFlowControlCommand()


def test_enable_flow_control(subject: RtxEnableFlowControlCommand) -> None:
    """It should create the command correctly."""
    assert subject.get_bytes() == bytes([0x15, 0x15])
