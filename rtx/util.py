from typing import Tuple


def to_rtx_spa_command(command: int, arinc_word: int) -> bytes:
    """Convert an Arinc 29 32-bit Word to an RTX-SPA ready 40-bit command.

    :param command:
    :param arinc_word: Arinc 29 word
    :return: RTX-SPA 40 bit command
    """
    # Bit 32 is always 1.
    byte_a = 0x01 | ((command & 7) << 1)
    # Bits 31-28 go to 39-36
    byte_a |= (arinc_word >> 24) & 0xF0
    # Bits 27-21 go to 31-25
    byte_b = (arinc_word >> 20) & 0xFE
    # Bits 20-14 go to 23-17
    byte_c = (arinc_word >> 13) & 0xFE
    # Bits 13-6 go to 15-9
    byte_d = (arinc_word >> 6) & 0xFE
    # Bits 6-0 go to 7-1
    byte_e = (arinc_word & 0x0000007F) << 1
    return bytes([byte_a, byte_b, byte_c, byte_d, byte_e])


def from_rtx_spa_command(rtx_spa_command: bytes) -> Tuple[int, int]:
    """Convert RTX spa 40 bit command into a command and Arinc29 32 bit word

    :param rtx_spa_command: The rtx spa command
    :return: A tuple of command and arinc word.
    """
    byte_a, byte_b, byte_c, byte_d, byte_e = rtx_spa_command
    command = (byte_a >> 1) & 0x7
    arinc_word = (byte_a & 0xF0) << 24
    arinc_word |= (byte_b & 0xFE) << 20
    arinc_word |= (byte_c & 0xFE) << 13
    arinc_word |= (byte_d & 0xFE) << 6
    arinc_word |= (byte_e & 0xFE) >> 1
    return command, arinc_word
