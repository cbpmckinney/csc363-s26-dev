import sys
import os

from .CodeObject import CodeObject
from .InstructionList import InstructionList
from .instructions import *
from ..compiler import *
from ..ast import *
from ..ast.visitor.AbstractASTVisitor import AbstractASTVisitor

class CodeGenerator(AbstractASTVisitor):

  def __init__(self):
    self.intRegCount = 0
    self.floatRegCount = 0
    self.intTempPrefix = 't'
    self.floatTempPrefix = 'f'

  def getIntRegCount(self):
    return self.intRegCount

  def getFloatRegCount(self):
    return self.floatRegCount

  # Generate code for Variables
  #
  # Create a code object that just holds a variable
  # Important: add a pointer from the code object to the symbol table entry so
  # we know how to generate code for it later (we'll need it to find the
  # address)
  #
  # Mark the code object as holding a variable, and also as an lval

  def postprocessVarNode(self, node: VarNode) -> CodeObject:
    sym = node.getSymbol()

    co = CodeObject(sym)
    co.lval = True
    co.type = node.getType()

    return co

  # Generate code for IntLiterals
  #
  # Use load immediate instruction to do this
  
  def postprocessIntLitNode(self, node: IntLitNode) -> CodeObject:
    co = CodeObject()
    i = Li(self.generateTemp(Scope.Type.INT), node.getVal())
		
    #Load an immediate into a register
		#The li and la instructions are the same, but it's helpful to distinguish
		#for readability purposes.
		#li tmp' value

    co.code.append(i) #add this instruction to the code object
    co.lval = False #co holds an rval -- data
    co.temp = i.getDest()
    co.type = node.getType() # temp is in destination of li
    return co

  # Generate code for FloatLiterals
  #
  # Use load immediate instruction to do this

  def postprocessFloatLitNode(self, node: FloatLitNode) -> CodeObject:
    co = CodeObject()

    #Load an immediate into a register
		#The li and la instructions are the same, but it's helpful to distinguish
		#for readability purposes.
		#li tmp' value
    i = FImm(self.generateTemp(Scope.Type.FLOAT), node.getVal())
    
    co.code.append(i) # add this instruction to the code object
    co.lval = False # co holds an rval -- data
    co.temp = i.getDest() # temp is in destination of li
    co.type = node.getType()
    return co

	 # Generate code for binary operations.
	 # 
	 # Step 0: create new code object
	 # Step 1: add code from left child
	 # Step 1a: if left child is an lval, add a load to get the data
	 # Step 2: add code from right child
	 # Step 2a: if right child is an lval, add a load to get the data
	 # Step 3: generate binary operation using temps from left and right
	 # 
	 # Don't forget to update the temp and lval fields of the code object!
	 # 	   Hint: where is the result stored? Is this data or an address?

  def postprocessBinaryOpNode(self, node: BinaryOpNode, left: CodeObject, right: CodeObject) -> CodeObject:
    #Step 0: create new code object
    co = CodeObject()
    newcode = CodeObject()

    print("Left: ", left, "Left Type: ", left.type)
    print("Right: ", right)
    print("Optype: ", str(node.op))

    optype = str(node.op) # Get string corresponding to the operation (+, -, *, /)
    #Step 1: add code from left child
    
    #Step 1a: check if left child is an lval or rval; if lval, rvalify
    if left.lval == True:
      left = self.rvalify(left) # create new code object, fix this, this is bad?
      print("Left type after rvalify:", left.type)
    co.code.extend(left.code)

    #Step 2: add code from right child

    if right.lval == True:
      right = self.rvalify(right)
    
    co.code.extend(right.code)
  
    #Step 2a: check if left child is an lval or rval; if lval, rvalify

    #Step 3: generate correct binop.  8 cases for 4 ops, float vs. int. for 4 arithmetic ops.

    if left.type != right.type:
      print("Incompatible types in binary operation!\n")
    
    # Get appropriate new temporary for result of operation
    if left.type == Scope.Type.INT:
      print("Processing binop with INTs")
      newtemp = self.generateTemp(Scope.Type.INT)
      if optype == "OpType.ADD":
        newcode = Add(left.temp, right.temp, newtemp)
      elif optype == "OpType.SUB":
        newcode = Sub(left.temp, right.temp, newtemp)
      elif optype == "OpType.MUL":
        newcode = Mul(left.temp, right.temp, newtemp)
      elif optype == "OpType.DIV":
        newcode = Div(left.temp, right.temp, newtemp)
      else:
        print("Bad operation in binop!\n")


    elif left.type == Scope.Type.FLOAT:
      newtemp = self.generateTemp(Scope.Type.FLOAT)
      if optype == "OpType.ADD":
        newcode = FAdd(left.temp, right.temp, newtemp)
      elif optype == "OpType.SUB":
        newcode = FSub(left.temp, right.temp, newtemp)
      elif optype == "OpType.MUL":
        newcode = FMul(left.temp, right.temp, newtemp)
      elif optype == "OpType.DIV":
        newcode = FDiv(left.temp, right.temp, newtemp)
      else:
        print("Bad operation in binop!\n")

    else:
      print("Bad type in binary op!\n")


    #Step 4: update temp, lval etc., return code object


    co.code.append(newcode)
    co.lval = False
    co.temp = newtemp
    co.type = left.type
    print(newcode)
    return co
	 
   #  Generate code for unary operations.
	 #  
	 #  Step 0: create new code object
	 #  Step 1: add code from child expression
	 #  Step 1a: if child is an lval, add a load to get the data
	 #  Step 2: generate instruction to perform unary operation (don't forget to generate right type of op)
	 #  
	 #  Don't forget to update the temp and lval fields of the code object!
	 #  	   Hint: where is the result stored? Is this data or an address?


  # Note that this handles negative literals, e.g. -2 is unary op(2, -)
  def postprocessUnaryOpNode(self, node: UnaryOpNode, expr: CodeObject) -> CodeObject:
    #print("Processing Unary Operation!\n")
    #print("Node is: ", node, "\n")
    #print("expr is: ", expr, "\n")
    co = CodeObject()  # Step 0
    #FILL IN CODE FOR STEP 2
    instrlist = InstructionList()
    #print("expr code: ", expr.code, "\n")
    #print("expr lval: ", expr.lval, "\n")
    #print("expr type is ", expr.type, "\n")
    instrlist.extend(expr.code)
    if expr.lval == True:
      newcode = self.rvalify(expr)
      instrlist.append(newcode)  # Need to fix something here-ish, not correctly handling lvalues and this means expr.temp is broken later
      oldtemp = newcode.temp
    else:
      oldtemp = expr.temp

    # Step 2: generate negation operation code
    if expr.type == Scope.Type.INT:
      #print("Processing INT\n")
      newtemp = self.generateTemp(Scope.Type.INT)
      #print("New temp for int: ", newtemp, "\n")
      #print("Original temp: ", oldtemp, "\n")
      negcode = Neg(oldtemp, newtemp)  # Need source and destination
      #print("Neg code: ", negcode, "\n")
    elif expr.type == Scope.Type.FLOAT:
      #print("Processing Float\n")
      newtemp = self.generateTemp(Scope.Type.FLOAT)
      #print("New temp for float: ", newtemp, "\n")
      negcode = FNeg(oldtemp, newtemp)
    else:
      print("Non float/int in unary op!\n")
    instrlist.append(negcode)
    co.code.extend(instrlist)
    co.temp = newtemp
    co.lval = False
    co.type = expr.type
    # Does something need to be stored somewhere?  Or is that going to be done by the assignment node that's a parent of the unary node?
    #print("Code at end: ", co, "\n")
    return co
  





	 # Generate code for assignment statements
	 # 
	 # Step 0: create new code object
	 # Step 1a: if LHS is a variable, generate a load instruction to get the address into a register
	 #          (see generateAddrFromVariable)
	 # Step 1b: add code from LHS of assignment (make sure it results in an lval!)
	 # Step 2: add code from RHS of assignment
	 # Step 2a: if right child is an lval, add a load to get the data
	 # Step 3: generate store (don't forget to generate the right type of store)
	 # 
	 # Hint: it is going to be easiest to just generate a store with a 0 immediate
	 # offset, and the complete store address in a register:
	 # 
	 # sw rhs 0(lhs)

  def postprocessAssignNode(self, node: AssignNode, left: CodeObject, right: CodeObject) -> CodeObject:
    #Step 0: create new code object
    co = CodeObject()
    instrlist = InstructionList()
    assert(left.lval is True)

    if right.lval == True:
      right = self.rvalify(right)

    #Step 1a
    if left.isVar():
      left = self.generateAddrFromVariable(left)
      instrlist.extend(left.code)
      instrlist.extend(right.code)

      if left.type == Scope.Type.INT:
        newcode = Sw(right.temp, left.temp, "0")
      elif left.type == Scope.Type.FLOAT:
        newcode = Fsw(right.temp, left.temp, "0")
      else:
        print("Assignment with non-var Left Hand Side!\n")
    
    instrlist.append(newcode)
    #Step 2
    
    co.code.extend(instrlist)

    #co.lval = False #doesn't matter
    #co.temp = None #set to None to trigger errors
    #co.type = None #set to None to trigger errors

    return co

  # Add together all the lists of instructions generated by the children

  def postprocessStatementListNode(self, node: StatementListNode, statements: list) -> CodeObject:
    co = CodeObject()

    for subcode in statements:
      co.code.extend(subcode.code)

    co.type = None
    return co

	 # Generate code for read
	 # 
	 # Step 0: create new code object
	 # Step 1: add code from VarNode (make sure it's an lval)
	 # Step 2: generate GetI instruction, storing into temp
	 # Step 3: generate store, to store temp in variable
	
  def postprocessReadNode(self, node: ReadNode, var: CodeObject) -> CodeObject:
    co = CodeObject()
    assert(var.getSTE() is not None)
    tmp = self.generateAddrFromVariable(var)

    co.code.extend(tmp.code)

    il = InstructionList()

    typ = node.getType()

    if typ == Scope.Type.INT:
 		  # Code to generate if INT:
			#	geti tmp
			#	sw tmp 0(var.tmp)
      geti = GetI(self.generateTemp(Scope.Type.INT))
      il.append(geti)
      sw = Sw(geti.getDest(), tmp.temp, "0")
      il.append(sw)
    elif typ == Scope.Type.FLOAT:
      # Code to generate if FLOAT:
			#	getf tmp
			#	fsw tmp 0(var.tmp)
      getf = GetF(self.generateTemp(Scope.Type.FLOAT))
      il.append(getf)
      fsw = Fsw(getf.getDest(), tmp.temp, "0")
      il.append(fsw)
    else:
      raise Exception("Shouldn't read into other variable")

    co.code.extend(il)

    co.lval = False #doesn't matter
    co.temp = None #set to None to trigger errors
    co.type = None #set to None to trigger errors

    return co
	 
   # Generate code for print
	 # 
	 # Step 0: create new code object
	 # 
	 # If printing a string:
	 # Step 1: add code from expression to be printed (make sure it's an lval)
	 # Step 2: generate a PutS instruction printing the result of the expression
	 # 
	 # If printing an integer:
	 # Step 1: add code from the expression to be printed
	 # Step 1a: if it's an lval, generate a load to get the data
	 # Step 2: Generate PutI that prints the temporary holding the expression

  def postprocessWriteNode(self, node: WriteNode, expr: CodeObject) -> CodeObject:
    co = CodeObject()
    #generating code for write(expr)

    #for strings, we expect a variable
    if node.getWriteExpr().getType() == Scope.Type.STRING:
      #Step 1:
      assert(expr.getSTE() is not None)

      #Get the address of the variable
      addrCo = self.generateAddrFromVariable(expr)
      co.code.extend(addrCo.code)

      #Step 2:
      write = PutS(addrCo.temp)
      co.code.append(write)
    else:
      #Step 1a:
      #if expr is an lval, load from it
      if expr.lval is True:
        expr = self.rvalify(expr)
      #Step 1:
      co.code.extend(expr.code)

      #Step 2:
      #if type of writenode is int, use puti, if float, use putf
      write = None
      typ = node.getWriteExpr().getType()
      if typ == Scope.Type.STRING:
        raise Exception("Shouldn't have a STRING here")
      elif typ == Scope.Type.INT:
        write = PutI(expr.temp)
      elif typ == Scope.Type.FLOAT:
        write = PutF(expr.temp)
      else:
        raise Exception("WriteNode has a weird type")
      co.code.append(write)

    co.lval = False #doesn't matter
    co.temp = None #set to None to trigger errors
    co.type = None #set to None to trigger errors
    return co

  # Generating code for returns
	# 
	# For now, we don't do anything with return values, so just generate HALT
  
  def postprocessReturnNode(self, node: ReturnNode, retExpr: CodeObject) -> CodeObject:
    co = CodeObject()

    #if retexpr is an lval, load from it
    if retExpr.lval is True:
      retExpr = self.rvalify(retExpr)

    co.code.extend(retExpr.code)

    #We don't support functions yet, so a return is just a halt
    h = Halt()
    co.code.append(h)
    co.type = None #set to None to trigger errors

    return co

	# Generate a fresh temporary
	# 
	# @return new temporary register name
  
  def generateTemp(self, t: Scope.Type) -> str:
    if t == Scope.Type.INT:
      s = self.intTempPrefix + str(self.intRegCount)
      self.intRegCount += 1
      return s
    elif t == Scope.Type.FLOAT:
      s = self.floatTempPrefix + str(self.floatRegCount)
      self.floatRegCount += 1
      return s
    else:
      raise Exception("Generating temp for bad type")

	 # Take a code object that results in an lval, and create a new code
	 # object that adds a load to generate the rval.
	 # 
	 # Step 0: Create new code object
	 # 
	 # Step 1: Add all the lco code to the new code object
	 # 		   (If lco is just a variable, create a new code object that
	 #          stores the address of variable in a code object; see
	 #          generateAddrFromVariable)
	 # 
	 # Step 2: Generate a load to load from lco's temp into a new temporary
	 # 		   Hint: it'll be easiest to generate a load with no offset:
	 # 				lw newtemp 0(oldtemp)
	 #         Don't forget to generate the right kind of load based on the type
	 #         stored in the address
	 # 
	 # Don't forget to update the temp and lval fields of the code object!
	 # 		   Hint: where is the result stored? Is this data or an address?
	 # 
	 # @param lco The code object resulting in an address
	 # @return A code object with all the code of <code>lco</code> followed by a load
	 #         to generate an rval

  # Append goes at the back, extend goes at the front (like prepending)

  def rvalify(self, lco : CodeObject) -> CodeObject:
    # Step 0
    co = CodeObject()
    assert(lco.lval is True)
    # FILL IN CODE FOR STEP 2
    #Step 1:
    #print("Rvalify input type: ", lco.type)

    if lco.isVar():
      newco = self.generateAddrFromVariable(lco)
      # Add LW instruction, update temp field
      if lco.type == Scope.Type.INT:
        newtemp = self.generateTemp(Scope.Type.INT)
        loadcode = Lw(newtemp, newco.temp, "0")
      elif lco.type == Scope.Type.FLOAT:
        newtemp = self.generateTemp(Scope.Type.FLOAT)
        loadcode = Flw(newtemp, newco.temp, "0")
      else:
        print("Error!  Bad type of variable in rvalify!\n")
      
      co.code.append(newco.code)
      co.code.append(loadcode)
      co.temp = newtemp
      #print("New temp from rvalify: ", newtemp, "\n")
    else:
      co.code.extend(lco.code)


    #Step 2
    co.type = lco.type 
    co.lval = False
    #print("rvalify type of output: ", co.type)
    return co





	# Take a code object that holds just a variable and turn it into a code object
	# that places the address of that variable into a registers
	# 
	# @param lco The code object holding a variable
	# @return A code object with the variable's address in a register

  def generateAddrFromVariable(self, lco: CodeObject) -> CodeObject:
    co = CodeObject()

    #Step 1:
    symbol = lco.getSTE()
    address = str(symbol.getAddress())

    #Step 2:
    #la tmp' addr // Register type needs to be an int
    loadAddr = La(self.generateTemp(Scope.Type.INT), address)
    
    co.code.append(loadAddr) #add instruction to code object
    co.lval = True #co holds an lval, because it's an address
    co.temp = loadAddr.getDest() #temp is in destination of la
    co.ste = None #not a variable
    co.type = symbol.getType() #even though register type is an int, address points to Type

    return co
  
