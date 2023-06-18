from rtx import util


def test_to_rtx_spa_command() -> None:
    """It should convert an arinc word and command into an spa command."""
    assert util.to_rtx_spa_command(1, 0x12345678) == 0x1322A258F0


def test_from_rtx_spa_command() -> None:
    """It should convert an rtx spa command into a command and 32 bit arinc word."""
    assert util.from_rtx_spa_command(0x1322A258F0) == (1, 0x12345678)
