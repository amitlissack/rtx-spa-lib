from rtx.command.base import RtxCommandBase
from rtx.types import RtxCommandIdentifier, RtxConfiguration


class RtxEnableFlowControlCommand(RtxCommandBase):
    def get_bytes(self) -> bytes:
        # bits 1-3 or b010
        cmd_byte = RtxCommandIdentifier.configure << 1
        # bits 4-7 are baud rate
        cmd_byte |= RtxConfiguration.enable_flow_control << 4
        # lsb is 1
        cmd_byte |= 1
        return bytes([cmd_byte, cmd_byte])
