def convert(command: int, arinc_word: int) -> int:
    """Convert an Arinc 29 32-bit Word to an RTX-SPA ready 40-bit integer.

    :param command:
    :param arinc_word: Arinc 29 word
    :return: RTX-SPA 40 bit integer
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
