import pytest
from rtx.util import convert


def test_convert() -> None:
    assert convert(1, 0x12345678) == 0x1322A258F0
