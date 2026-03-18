from .Instruction3O import Instruction3O
from .Instruction import OpCode

class Srli(Instruction3O):
  def __init__(self, src1: str, imm: str, dest: str):
    super().__init__(src1, imm, dest)
    self.oc = OpCode.SRLI
