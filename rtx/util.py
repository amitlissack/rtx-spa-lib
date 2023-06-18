def to_rtx_spa_command(command: int, arinc_word: int) -> int:
    """Convert an Arinc 29 32-bit Word to an RTX-SPA ready 40-bit command.

    :param command:
    :param arinc_word: Arinc 29 word
    :return: RTX-SPA 40 bit command
    """
    # Bit 32 is always 1.
    result = 0x0100000000 | ((command & 7) << 33)
    # Bits 31-28
    result |= (arinc_word & 0xF0000000) << 8
    # Bits 27-21
    result |= (arinc_word & 0x0FE00000) << 4
    # Bits 20-14
    result |= (arinc_word & 0x001F6000) << 3
    # Bits 13-6
    result |= (arinc_word & 0x00003F80) << 2
    # Bits 6-0
    result |= (arinc_word & 0x0000007F) << 1
    return result


def from_rtx_spa_command(rtx_spa_command: int) -> tuple[int, int]:
    """Convert RTX spa 40 bit command into a command and Arinc29 32 bit word

    :param rtx_spa_command: The rtx spa command
    :return: A tuple of command and arinc word.
    """
    command = (rtx_spa_command >> 33) & 0x7
    arinc_word = (rtx_spa_command & 0xF000000000) >> 8
    arinc_word |= (rtx_spa_command & 0xFE000000) >> 4
    arinc_word |= (rtx_spa_command & 0xFE0000) >> 3
    arinc_word |= (rtx_spa_command & 0xFE00) >> 2
    arinc_word |= (rtx_spa_command & 0xFE) >> 1
    return command, arinc_word
