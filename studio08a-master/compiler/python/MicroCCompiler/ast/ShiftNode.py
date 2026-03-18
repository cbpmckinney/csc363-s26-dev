from .ASTNode import ASTNode
from typing import TYPE_CHECKING, Any
from enum import Enum

if TYPE_CHECKING:
  from .visitor import ASTVisitor

class ShiftNode(ASTNode):
  class OpType(Enum):
    SLLI = 1
    SRLI = 2


  def getOpFromString(self, op: str):
    if op == '<<':
      return self.OpType.SLLI
    elif op == '>>':
      return self.OpType.SRLI
    else:
      raise Exception("Invalid opcode in Shift Op")

  def __init__(self, expr: ASTNode, shftamt: str, op: str):
    self.setExpr(expr)
    self.setShftAmt(shftamt)
    self.setOp(self.getOpFromString(op))
    self.setType(expr.getType())

  def accept(self, visitor: 'ASTVisitor') -> Any:
    return visitor.visitShiftNode(self)

  def getExpr(self) -> ASTNode:
    return self.expr

  def setExpr(self, expr: ASTNode):
    self.expr = expr

  def getShftAmt(self) -> str:
    return self.shftamt

  def setShftAmt(self, shftamt: str):
    self.shftamt = shftamt

  def setOp(self, op):
    self.op = op

  def getOp(self) -> OpType:
    return self.op
