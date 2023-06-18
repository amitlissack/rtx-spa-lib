from rtx import util


def test_to_rtx_spa_command() -> None:
    """It should convert an arinc word and command into an spa command."""
    assert util.to_rtx_spa_command(1, 0x12345678) == bytes(
        [0x13, 0x22, 0xA2, 0x58, 0xF0]
    )


def test_from_rtx_spa_command() -> None:
    """It should convert an rtx spa command into a command and 32 bit arinc word."""
    assert util.from_rtx_spa_command(bytes([0x13, 0x22, 0xA2, 0x58, 0xF0])) == (
        1,
        0x12345678,
    )
