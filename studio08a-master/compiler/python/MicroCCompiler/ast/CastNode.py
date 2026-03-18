from .ASTNode import ASTNode
from typing import TYPE_CHECKING, Any
import sys

from ..compiler.Scope import Scope

if TYPE_CHECKING:
  from .visitor import ASTVisitor


class CastNode(ASTNode):
  
  def __init__(self, my_type: Scope.Type, expr: ASTNode):
    self.setExpr(expr)
    self.setCastType(my_type)
    self.exprtype = expr.getType()
    self.type = self.casttype
    
    #print(self.exprtype, file=sys.stderr)
    #print(str(my_type), file=sys.stderr)
    ## THIS NEEDS TO CHANGE: TYPE SHOULD BE DETERMINED BY MYTYPE NOT EXPR

  def accept(self, visitor: 'ASTVisitor') -> Any:
    return visitor.visitCastNode(self)
  
  def setExpr(self, expr) -> ASTNode:
    self.expr = expr

  def getExpr(self) -> ASTNode:
    return self.expr
  
  def setCastType(self, my_type: Scope.Type):
    self.casttype = my_type

  def getCastType(self) -> Scope.Type:
    return self.casttype




