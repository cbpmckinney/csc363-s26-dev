import sys
import os
from typing import List

from python.MicroCCompiler.ast import ShiftNode

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
    self.loopLabel = 0
    self.elseLabel = 0
    self.outLabel = 0
    self.currFunc = None

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
    newtemp = self.generateTemp(Scope.InnerType.INT)
    i = Li(newtemp, node.getVal())
		
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
    i = FImm(self.generateTemp(Scope.InnerType.FLOAT), node.getVal())
    
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
    
    co = CodeObject()
    newcode = CodeObject()

    #print("Processing binary op node!", file=sys.stderr)
    #print("Left Type: ", str(left.type), file=sys.stderr)
    #print("Left temp: ", str(left.temp), file=sys.stderr)
    #print("Left is var? ", str(left.isVar()), file=sys.stderr)
    #print("Right Type: ", str(right.type), file=sys.stderr)
    #print("Right temp: ", str(right.temp), file=sys.stderr)
    #print("Right is var? ", str(right.isVar()), file=sys.stderr)
    #print("Optype: ", str(node.op), file=sys.stderr)

    optype = str(node.op) # Get string corresponding to the operation (+, -, *, /, <<, >>)
    #Step 1: add code from left child
    
    #Step 1a: check if left child is an lval or rval; if lval, rvalify
    if left.lval == True:
      left = self.rvalify(left) # create new code object, fix this, this is bad?
      #print("Left type after rvalify:", left.type)
    co.code.extend(left.code)

    #Step 2: add code from right child

    if right.lval == True:
      right = self.rvalify(right)
    
    co.code.extend(right.code)
  
    #Step 2a: check if left child is an lval or rval; if lval, rvalify

    #Step 3: generate correct binop.  8 cases for 4 ops, float vs. int. for 4 arithmetic ops.

    if left.type == right.type:
      # Types match, do the usual thing
      if left.type == Scope.Type(Scope.InnerType.INT):
          #print("Processing binop with INTs")
          newtemp = self.generateTemp(Scope.InnerType.INT)
          if optype == "OpType.ADD":
            co.code.append(Add(left.temp, right.temp, newtemp))
          elif optype == "OpType.SUB":
            co.code.append(Sub(left.temp, right.temp, newtemp))
          elif optype == "OpType.MUL":
            co.code.append(Mul(left.temp, right.temp, newtemp))
          elif optype == "OpType.DIV":
            co.code.append(Div(left.temp, right.temp, newtemp))
          else:
            print("Bad operation in binop!\n")

      elif left.type == Scope.Type(Scope.InnerType.FLOAT):
        newtemp = self.generateTemp(Scope.InnerType.FLOAT)
        if optype == "OpType.ADD":
          co.code.append(FAdd(left.temp, right.temp, newtemp))
        elif optype == "OpType.SUB":
          co.code.append(FSub(left.temp, right.temp, newtemp))
        elif optype == "OpType.MUL":
          co.code.append(FMul(left.temp, right.temp, newtemp))
        elif optype == "OpType.DIV":
          co.code.append(FDiv(left.temp, right.temp, newtemp))
        else:
          print("Bad operation in binop!\n")

      co.type = left.type
      co.temp = newtemp


    else:
      # Types do not match.  Either pointer arithmetic or need to cast or type error

      if (left.type == Scope.Type(Scope.InnerType.INT) and right.type == Scope.Type(Scope.InnerType.FLOAT)):
        typeconvtemp = self.generateTemp(Scope.InnerType.FLOAT)
        co.code.append(IMOVF(left.temp, typeconvtemp))
        newtemp = self.generateTemp(Scope.InnerType.FLOAT)
        co.temp = newtemp
        co.type = right.type
        if optype == "OpType.ADD":
          co.code.append(FAdd(typeconvtemp, right.temp, newtemp))
        elif optype == "OpType.SUB":
          co.code.append(FSub(typeconvtemp, right.temp, newtemp))
        elif optype == "OpType.MUL":
          co.code.append(FMul(typeconvtemp, right.temp, newtemp))
        elif optype == "OpType.DIV":
          co.code.append(FDiv(typeconvtemp, right.temp, newtemp))
        else:
          print("Bad operation in binop!\n")

        
      elif (left.type == Scope.Type(Scope.InnerType.FLOAT) and right.type == Scope.Type(Scope.InnerType.INT)):
        typeconvtemp = self.generateTemp(Scope.InnerType.FLOAT)
        co.code.append(IMOVF(right.temp, typeconvtemp))
        newtemp = self.generateTemp(Scope.InnerType.FLOAT)
        co.temp = newtemp
        co.type = left.type
        if optype == "OpType.ADD":
          co.code.append(FAdd(left.temp, typeconvtemp, newtemp))
        elif optype == "OpType.SUB":
          co.code.append(FSub(left.temp, typeconvtemp, newtemp))
        elif optype == "OpType.MUL":
          co.code.append(FMul(left.temp, typeconvtemp, newtemp))
        elif optype == "OpType.DIV":
          co.code.append(FDiv(left.temp, typeconvtemp, newtemp))
        else:
          print("Bad operation in binop!\n")

      else:
        # This is the pointer arithmetic situation, or type error
        newtemp = self.generateTemp(Scope.InnerType.INT)
        match optype:
          case 'OpType.ADD':
            co.code.append(Add(left.temp, right.temp, newtemp))
          case 'OpType.SUB':
            co.code.append(Sub(left.temp, right.temp, newtemp))
          case 'OpType.MUL':
            co.code.append(Mul(left.temp, right.temp, newtemp))
          case 'OpType.DIV':  # This case probably shouldn't ever happen
            co.code.append(Div(left.temp, right.temp, newtemp))

        co.type = left.type
        co.temp = newtemp

    #Step 4: update temp, lval etc., return code object


    co.lval = False
    return co



  def postprocessShiftNode(self, node: ShiftNode, expr: CodeObject, shftamt: str) -> CodeObject:
    #print("Processing Shift Node!", file=sys.stderr)
    #print("Expr type is: " + str(expr.type), file=sys.stderr)
    #print("Shift amount is: " + str(shftamt), file=sys.stderr)
    #print("Shift operation is: " + str(node.op), file=sys.stderr)
    co = CodeObject()

    if expr.lval:
      expr = self.rvalify(expr)
    co.code.extend(expr.code)

    nodetype = str(node.op)
    

    newtemp = self.generateTemp(Scope.InnerType.INT)

    match nodetype:
      case 'OpType.SLLI':
        co.code.append(Slli(expr.temp, shftamt, newtemp))
      case 'OpType.SRLI':
        co.code.append(Srli(expr.temp, shftamt, newtemp))

    co.type = Scope.InnerType.INT
    co.temp = newtemp
    co.lval = False
    return co
    

  def postprocessCastNode(self, node: CastNode, my_type: Scope.Type, expr: ASTNode) -> CodeObject:
    co = CodeObject()

    if expr.lval:
      expr = self.rvalify(expr)
    
    #co.code.append("; Casting code starts here")
    co.code.extend(expr.code)
  
    #print("Processing cast node!", file=sys.stderr)
    #print("my_type: " + str(my_type), file=sys.stderr)
    #print("expr type: " + str(expr.type), file=sys.stderr)
    #print("expr temp: " + str(expr.temp), file=sys.stderr)
    #print("expr lval? " + str(expr.lval), file=sys.stderr)

    if my_type == Scope.Type(Scope.InnerType.INT):
      #print("Casting to int", file=sys.stderr)
      newtemp = self.generateTemp(Scope.InnerType.INT)
      co.code.append(FMOVI(expr.temp, newtemp))
      co.temp = newtemp
      co.type = Scope.Type(Scope.InnerType.INT)

    elif Scope.Type(Scope.InnerType.FLOAT):
      #print("Casting to float", file=sys.stderr)
      newtemp = self.generateTemp(Scope.InnerType.FLOAT)
      co.code.append(IMOVF(expr.temp, newtemp))
      co.temp = newtemp
      co.type = Scope.Type(Scope.InnerType.FLOAT)

    elif Scope.Type.pointerToType(Scope.Type(Scope.InnerType.INT)):
      #print("Casting to int pointer", file=sys.stderr)
      pass
      
    elif Scope.Type.pointerToType(Scope.Type(Scope.InnerType.FLOAT)):
      #print("Casting to float pointer", file=sys.stderr)
      pass

  

    #co.code.append("; Casting code ends here")
    return co


  def postprocessUnaryOpNode(self, node: UnaryOpNode, expr: CodeObject) -> CodeObject:

    co = CodeObject()

    co.code.extend(expr.code)
    if expr.lval == True:
      newcode = self.rvalify(expr)
      co.code.append(newcode)
      oldtemp = newcode.temp
    else:
      oldtemp = expr.temp
    
    if expr.type == Scope.Type(Scope.InnerType.INT):
      newtemp = self.generateAddrFromVariable(Scope.InnerType.INT)
      co.code.append(Neg(oldtemp, newtemp))
    elif expr.type == Scope.Type(Scope.InnerType.FLOAT):
      co.code.append(FNeg(oldtemp, newtemp))

    co.temp = newtemp
    co.lval = False
    co.type = expr.type

    return co

  def postprocessAssignNode(self, node: AssignNode, left: CodeObject, right: CodeObject) -> CodeObject:
    
    #print("Processing assign node!", file=sys.stderr)
    #print("Inside function: " + str(self.currFunc), file=sys.stderr)
    #print("Left type: " + str(left.type), file=sys.stderr)
    #print("Left lval? " + str(left.lval), file=sys.stderr)
    #print("Left temp: " + str(left.temp), file=sys.stderr)
    #print("Left var? " + str(left.isVar()), file=sys.stderr)
    #print("Right type: " + str(right.type), file=sys.stderr)
    #print("Right lval? " + str(right.lval), file=sys.stderr)
    #print("Right temp: " + str(right.temp), file=sys.stderr)
    #print("Right var? " + str(right.isVar()), file=sys.stderr)

    co = CodeObject()
    
    typeconv = False
    if left.type != right.type:
      # Types differ: need to worry.
      #print("Assign types mismatch!", file=sys.stderr)
      if left.type == Scope.Type(Scope.InnerType.INT) and right.type == Scope.Type(Scope.InnerType.FLOAT):
        #print("LHS is int, RHS is float, casting float to int", file=sys.stderr)
        typeconvtemp = self.generateTemp(Scope.InnerType.INT)
        convertcode = FMOVI(right.temp, typeconvtemp)
        typeconv = True

      elif left.type == Scope.Type(Scope.InnerType.FLOAT) and right.type == Scope.Type(Scope.InnerType.INT):
        #print("LHS is float, RHS is int, casting int to float", file=sys.stderr)
        typeconvtemp = self.generateTemp(Scope.Type.FLOAT)
        convertcode = (IMOVF(right.temp, typeconvtemp))
        typeconv = True



    if left.lval:
      #print("Left is lval", file=sys.stderr)
      # Left is an lval
      #assert (left.isVar() is True)
      if left.isVar():
        symbol = left.getSTE()
        if right.lval == True:
          right = self.rvalify(right)

        if symbol.isLocal():
          # Left is a local var
          address = symbol.addressToString()
          co.code.extend(right.code)

          if typeconv:
            co.code.append(convertcode)
            right.temp = typeconvtemp

          if left.type == Scope.Type(Scope.InnerType.INT):
            co.code.append(Sw(right.temp, 'fp', address))

          elif left.type == Scope.Type(Scope.InnerType.FLOAT):
            co.code.append(Fsw(right.temp, 'fp', address))

          elif left.type == Scope.Type.pointerToType(Scope.Type(Scope.InnerType.INT)):
            # This is the case for pointer to an int
            co.code.append(Sw(right.temp, 'fp', address))

          elif left.type == Scope.Type.pointerToType(Scope.Type(Scope.InnerType.FLOAT)):
            # This is the case for pointer to a float...pointers are ints, remember!
            co.code.append(Sw(right.temp, 'fp', address))

          #elif left.type == Scope.Type.pointerToType(Scope.Type(Scope.InnerType.PTR)):
          elif left.type == Scope.Type.pointerToType(Scope.Type.pointerToType(Scope.Type(Scope.InnerType.INT))):
            
            co.code.append(Sw(right.temp, 'fp', address))

        else: 
          # Left is a global var
          newaddrtemp = self.intTempPrefix + str(self.intRegCount)
          newleft = self.generateAddrFromVariable(left)
          co.code.extend(newleft)
          co.code.extend(right.code)
          if typeconv:
            co.code.append(convertcode)
            right.temp = typeconvtemp
          if left.type == Scope.Type(Scope.InnerType.INT):
            co.code.append(Sw(right.temp, newaddrtemp, '0'))
          elif left.type == Scope.Type(Scope.InnerType.FLOAT):
            co.code.append(Fsw(right.temp, newaddrtemp, '0'))
      
      else:
        # Left is an lval but not a var
        #print("Left is an lval but not a var", file=sys.stderr)
        #print("Left temp: " + str(left.temp), file=sys.stderr)
        #print("Left type: " + str(left.type), file=sys.stderr)
        #print("Right lval? " + str(right.lval), file=sys.stderr)
        if right.lval:
          #print("Rvalifying right", file=sys.stderr)
          right = self.rvalify(right)

        if left.type == Scope.Type(Scope.InnerType.INT):
          #pointer to int case
          #co.code.append("; left code here")
          co.code.extend(left.code)
          #co.code.append("; end left code")
          #co.code.append("; right code here")
          co.code.extend(right.code)
          #co.code.append("; end right code")
          co.code.append(Sw(right.temp, left.temp, '0'))
          
        elif left.type == Scope.Type(Scope.InnerType.FLOAT):
          #pointer to float case
          co.code.extend(left.code)
          co.code.extend(right.code)
          co.code.append(Fsw(right.temp, left.temp, '0'))

        else:
          # pointer to a pointer case
          #print("Pointer to pointer case", file=sys.stderr)
          co.code.extend(left.code)
          co.code.extend(right.code)
          co.code.append(Sw(right.temp, left.temp, '0'))



    #co.code.append("; end assign node")
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

    il = InstructionList()

    typ = node.getType()

    if typ.type == Scope.InnerType.INT:
 		  # Code to generate if INT:
			#	geti tmp
      # if var is global: la tmp', <var>; sw tmp 0(tmp')
      # if var is local: sw tmp offset(fp)
      geti = GetI(self.generateTemp(Scope.InnerType.INT))
      il.append(geti)
      store = InstructionList()
      if var.getSTE().isLocal():
        store.append(Sw(geti.getDest(), "fp", var.getSTE().addressToString()))
      else:
        store.extend(self.generateAddrFromVariable(var));
        store.append(Sw(geti.getDest(), store.getLast().getDest(), "0"))
      il.extend(store)
    elif typ.type == Scope.InnerType.FLOAT:
      # Code to generate if FLOAT:
			#	getf tmp
      # if var is global: la tmp', <var>; fsw tmp 0(tmp')
      # if var is local: fsw tmp offset(fp)
      getf = GetF(self.generateTemp(Scope.InnerType.FLOAT))
      il.append(getf)
      fstore = InstructionList()
      if var.getSTE().isLocal():
        fstore.append(Fsw(getf.getDest(), "fp", var.getSTE().addressToString()))
      else:
        fstore.extend(self.generateAddrFromVariable(var));
        fstore.append(Fsw(getf.getDest(), fstore.getLast().getDest(), "0"))
      il.extend(fstore)
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
    if node.getWriteExpr().getType().type == Scope.InnerType.STRING:
      #Step 1:
      assert(expr.getSTE() is not None)

      #print(f"; generating code to print {expr.getSTE()}")

      #Get the address of the variable
      
      addrCo = self.generateAddrFromVariable(expr)
      co.code.extend(addrCo)
      #Step 2:
      write = PutS(addrCo.getLast().getDest())
      co.code.append(write)

    else:
      #Step 1a:
      #if expr is an lval, load from it
      if expr.lval is True:
        expr = self.rvalify(expr)

      #Step 1:
      #co.code.append("; rvalify in write node starts here")
      co.code.extend(expr.code)
      #co.code.append("; rvalify in write node ends here")

      #Step 2:
      #if type of writenode is int, use puti, if float, use putf
      write = None
      typ = node.getWriteExpr().getType()

      if typ.type == Scope.InnerType.STRING:
        raise Exception("Shouldn't have a STRING here")
      elif typ.type == Scope.InnerType.INT or typ.type == Scope.InnerType.PTR:
        write = PutI(expr.temp)
      elif typ.type == Scope.InnerType.FLOAT:
        write = PutF(expr.temp)
      else:
        raise Exception("WriteNode has a weird type")
      #co.code.append("; Appending write code")
      co.code.append(write)
      #co.code.append("; FInished write code")

    co.lval = False #doesn't matter
    co.temp = None #set to None to trigger errors
    co.type = None #set to None to trigger errors
    return co

	#  Generating an instruction sequence for a conditional expression
	#  
	#  Implement this however you like. One suggestion:
	# 
	#  Create the code for the left and right side of the conditional, but defer
	#  generating the branch until you process IfStatementNode or WhileNode (since you
	#  do not know the labels yet). Modify CodeObject so you can save the necessary
	#  information to generate the branch instruction in IfStatementNode or WhileNode
	#  
	#  Alternate idea 1:
	#  
	#  Don't do anything as part of CodeGenerator. Create a new visitor class
	#  that you invoke *within* your processing of IfStatementNode or WhileNode
	#  
	#  Alternate idea 2:
	#  
	#  Create the branch instruction in this function, then tweak it as necessary in
	#  IfStatementNode or WhileNode
	#  
	#  Hint: you may need to preserve extra information in the returned CodeObject to
	#  make sure you know the type of branch code to generate (int vs float)

  def postprocessCondNode(self, node: CondNode, left: CodeObject, right: CodeObject) -> CodeObject:
    co = CodeObject()
    
    if(left.lval == True):
      left = self.rvalify(left)
    if(right.lval == True):
      right = self.rvalify(right)

    if left.type != right.type:
      print("TYPE ERROR", file=sys.stderr)
      sys.exit(7)


    if left.type == Scope.Type(Scope.InnerType.INT):
      # Both left and right are integer types
      # add left/right code
      co.code.extend(left.code)
      co.code.extend(right.code)
      co.temp = left.temp
      co.temp2 = right.temp
      co.type = left.type

    if left.type == Scope.Type(Scope.InnerType.FLOAT):
      co.code.extend(left.code)
      co.code.extend(right.code)
      #co.temp = self.generateTemp(Scope.Type.FLOAT) # generate new temporary for comparison
      co.type = left.type
      co.temp = left.temp
      co.temp2 = right.temp
      # Add stuff here for the comparison?

    co.lval = False # I think?
    # node.oc records op type:
    # EQ = 1
    # NE = 2
    # LT = 3
    # LE = 4
    # GT = 5
    # GE = 6
    co.cmptype = node.oc # records comparison type to pass up chain
    return co


   # Code generation for IfStatement
	 # Step 0: Create code object
	 # 
	 # Step 1: generate labels
	 # 
	 # Step 2: add code from conditional expression
	 # 
	 # Step 3: create branch statement (if not created as part of step 2)
	 # 			don't forget to generate correct branch based on type
	 # 
	 # Step 4: generate code
	 # 		<cond code>
	 #		<flipped branch> elseLabel
	 #		<then code>
	 #		j outLabel
	 #		elseLabel:
	 #		<else code>
	 #		outLabel:
	 #
	 # Step 5 insert code into code object in appropriate order.

  def postprocessIfStatementNode(self, node: IfStatementNode, cond: CodeObject, tlist: CodeObject, elist: CodeObject) -> CodeObject:
    
    co = CodeObject()
    # Recall condnodes have the function for reversing the op type
    #print(";Processing If Statement Node!\n")
    #startlabel = self.generateLoopLabel() # Place before the comparison
    endlabel = self.generateOutLabel()
    
    if elist != None:
      elselabel = self.generateElseLabel()

    comparisoncode = InstructionList()
    comparisoncode.extend(cond.code)
    revcmptype = self.reverseCompType(cond.cmptype)

    if elist != None:
      comparisonJumpTarget = elselabel
    else:
      comparisonJumpTarget = endlabel

    if cond.type == Scope.Type(Scope.InnerType.INT):
      # Integer comparison
      if revcmptype == 'OpType.EQ':
        comparisoncode.append(Beq(cond.temp, cond.temp2, comparisonJumpTarget))
      elif revcmptype == 'OpType.NE':
        comparisoncode.append(Bne(cond.temp, cond.temp2, comparisonJumpTarget))
      elif revcmptype == 'OpType.LT':
        comparisoncode.append(Blt(cond.temp, cond.temp2, comparisonJumpTarget))
      elif revcmptype == 'OpType.LE':
        comparisoncode.append(Ble(cond.temp, cond.temp2, comparisonJumpTarget))
      elif revcmptype == 'OpType.GT':
        comparisoncode.append(Bgt(cond.temp, cond.temp2, comparisonJumpTarget))
      elif revcmptype == 'OpType.GE':
        comparisoncode.append(Bge(cond.temp, cond.temp2, comparisonJumpTarget))
      else:
        print("Bad comparison type in if/then!\n")
    
    if cond.type == Scope.Type(Scope.InnerType.FLOAT): # condition is float-based!
      # Need two comparison operations for floats
      # First is one of the three float comparisons, which output to an integer register
      # Then need to compare that integer register, either is zero or nonzero
      # Also need to write some new test cases, since all of the given tests don't use float
      # need new integer temporary for the comparison
      tempintreg = self.generateTemp(Scope.InnerType.INT) # Need integer temporary
      #tempintreg2 = self.generateTemp(Scope.Type.INT) # Need a place to put 1 or 0 for the comparison
      # Optimization idea: could use r0 for this since r0 is always 0.  Not sure if the simulator respects this.
      # It does: use x0 for the always 0 int register
      #comparisoncode.append(Li(tempintreg2, "0")) # Load 0 for use with integer comparisons
      # Later on we can remove the Li instruction and use register 0 (which always is zero)
      if revcmptype == 'OpType.EQ': # == 
        comparisoncode.append(Feq(cond.temp, cond.temp2, tempintreg))
        comparisoncode.append(Bne(tempintreg, "x0", comparisonJumpTarget))
      elif revcmptype == 'OpType.NE': # != 
        comparisoncode.append(Feq(cond.temp, cond.temp2, tempintreg))
        comparisoncode.append(Beq(tempintreg, "x0", comparisonJumpTarget))
      elif revcmptype == 'OpType.LT': # <
        comparisoncode.append(Flt(cond.temp, cond.temp2, tempintreg))
        comparisoncode.append(Bne(tempintreg, "x0", comparisonJumpTarget))
      elif revcmptype == 'OpType.LE': # <=
        comparisoncode.append(Fle(cond.temp, cond.temp2, tempintreg))
        comparisoncode.append(Bne(tempintreg, "x0", comparisonJumpTarget))
      elif revcmptype == 'OpType.GT': # >
        comparisoncode.append(Flt(cond.temp2, cond.temp, tempintreg))
        comparisoncode.append(Bne(tempintreg, "x0", comparisonJumpTarget))
      elif revcmptype == 'OpType.GE': # >=
        comparisoncode.append(Fle(cond.temp2, cond.temp, tempintreg))
        comparisoncode.append(Bne(tempintreg, "x0", comparisonJumpTarget))
      else:
        print("Bad cmp type!\n")

    # Star building up the code
    # Start label goes first
    #co.code.append(Label(startlabel))
    # Now the comparison code
    co.code.extend(comparisoncode)
    # Now the "then" statement
    co.code.extend(tlist.code)
    # Now an unconditional jump to the end label
    co.code.append(J(endlabel))
    # Now the "else" label and code if any
    if elist != None:
      co.code.append(Label(elselabel))
      co.code.extend(elist.code)
    # Now the end label
    co.code.append(Label(endlabel))
    co.lval = False
    return co


   # Code generation for While statement
	 # Step 0: Create code object
	 # 
	 # Step 1: generate labels
	 # 
	 # Step 2: add code from conditional expression
	 # 
	 # Step 3: create branch statement (if not created as part of step 2)
	 # 			don't forget to generate correct branch based on type
	 # 
	 # Step 4: generate code
	 # 		loopLabel:
	 #		<cond code>
	 #		<flipped branch> outLabel
	 #		<body code>
	 #		j loopLabel
	 #		outLabel:
	 #
	 # Step 5 insert code into code object in appropriate order.

  def postprocessWhileNode(self, node: WhileNode, cond: CodeObject, wlist:
  CodeObject) -> CodeObject:
    co = CodeObject()
    looplabel = self.generateLoopLabel()
    endlabel = self.generateOutLabel()
    #print(";Loop label: ", looplabel)
    #print(";End label: ", endlabel)
    #print(";Cond temps 1/2: ", cond.temp, cond.temp2)
    
    comparisoncode = InstructionList()
    comparisoncode.extend(cond.code) # Add comparison code to code list (this doesn't DO the comparison, just prepares all the data)
    revcmptype = self.reverseCompType(cond.cmptype)

    if cond.type == Scope.Type(Scope.InnerType.INT): # condition is integer-based!  
    # The condition can be one of six types (==, !=, <, <=, >, >=) codes (1, 2, 3, 4, 5, 6)
      if revcmptype == 'OpType.EQ':
        comparisoncode.append(Beq(cond.temp, cond.temp2, endlabel))
      elif revcmptype == 'OpType.NE':
        comparisoncode.append(Bne(cond.temp, cond.temp2, endlabel))
      elif revcmptype == 'OpType.LT':
        comparisoncode.append(Blt(cond.temp, cond.temp2, endlabel))
      elif revcmptype == 'OpType.LE':
        comparisoncode.append(Ble(cond.temp, cond.temp2, endlabel))
      elif revcmptype == 'OpType.GT':
        comparisoncode.append(Bgt(cond.temp, cond.temp2, endlabel))
      elif revcmptype == 'OpType.GE':
        comparisoncode.append(Bge(cond.temp, cond.temp2, endlabel))
      else:
        print("Bad cmp type!\n")

    if cond.type == Scope.Type(Scope.InnerType.FLOAT): # condition is float-based!
      # Need two comparison operations for floats
      # First is one of the three float comparisons, which output to an integer register
      # Then need to compare that integer register, either is zero or nonzero
      # Also need to write some new test cases, since all of the given tests don't use float
      # need new integer temporary for the comparison
      tempintreg = self.generateTemp(Scope.InnerType.INT) # Need integer temporary
      #tempintreg2 = self.generateTemp(Scope.Type.INT) # Need a place to put 1 or 0 for the comparison
      # Optimization idea: could use r0 for this since r0 is always 0.  Not sure if the simulator respects this.
      #comparisoncode.append(Li(tempintreg2, "0")) # Load 0 for use with integer comparisons
      # Later on we can remove the Li instruction and use register 0 (which always is zero)
      if revcmptype == 'OpType.EQ': # == 
        comparisoncode.append(Feq(cond.temp, cond.temp2, tempintreg))
        comparisoncode.append(Bne(tempintreg, "x0", endlabel))
      elif revcmptype == 'OpType.NE': # != 
        comparisoncode.append(Feq(cond.temp, cond.temp2, tempintreg))
        comparisoncode.append(Beq(tempintreg, "x0", endlabel))
      elif revcmptype == 'OpType.LT': # <
        comparisoncode.append(Flt(cond.temp, cond.temp2, tempintreg))
        comparisoncode.append(Bne(tempintreg, "x0", endlabel))
      elif revcmptype == 'OpType.LE': # <=
        comparisoncode.append(Fle(cond.temp, cond.temp2, tempintreg))
        comparisoncode.append(Bne(tempintreg, "x0", endlabel))
      elif revcmptype == 'OpType.GT': # >
        comparisoncode.append(Flt(cond.temp2, cond.temp, tempintreg))
        comparisoncode.append(Bne(tempintreg, "x0", endlabel))
      elif revcmptype == 'OpType.GE': # >=
        comparisoncode.append(Fle(cond.temp2, cond.temp, tempintreg))
        comparisoncode.append(Bne(tempintreg, "x0", endlabel))
      else:
        print("Bad cmp type!\n")
    

    # Now to build up the code.
    # First we need the loop label.
    co.code.append(Label(looplabel))
    # Next we need the conditional checking.
    co.code.extend(comparisoncode)
    # Now the loop body
    co.code.append(wlist) 
    # Now the unconditional jumb back up to the loop label
    co.code.append(J(looplabel))
    # Now the end label
    co.code.append(Label(endlabel))
    # Code object constructed!
    # Now set type/values as needed before returning.
    co.lval = False
    # co.temp = ?
    # co.type = ?
    return co


	# FILL IN FOR STEP 4
	# 
	# Generating code for returns
	# 
	# Step 0: Generate new code object
	# 
	# Step 1: Add retExpr code to code object (rvalify if necessary)
	# 
	# Step 2: Store result of retExpr in appropriate place on stack (fp + 8)
	# 
	# Step 3: Jump to out label (use @link{generateFunctionOutLabel()})
  
  def postprocessReturnNode(self, node: ReturnNode, retExpr: CodeObject) -> CodeObject:
    
    co = CodeObject()


    # TO DO : Deal with case when we have void return

    #print("; Processing return node!", file=sys.stderr)
    #print("; Return expression is: " + str(retExpr.type), file=sys.stderr)
    #if retExpr is None:
    #  print("Return expression is null", file=sys.stderr)
    #print(str(node.getFuncSymbol().getReturnType()), file=sys.stderr) # <-- use this
      # This can check if we have a null return.  Could also use the node.funcSymbol.getReturnType()
    
    #Where am I?
    #tempname = self.currFunc
    #co.code.append("; Being called by " + tempname)
    #tempsymb = node.funcSymbol
    #co.code.append("; Func symbol is " + str(tempsymb))
    #rettype = node.funcSymbol.getReturnType()
    #co.code.append("; Return type is " + str(rettype))

    #temptype = self.currFunc
    #if retExpr.type != node.funcSymbol.getReturnType():
    #  pass
      #print("TYPE ERROR", file=sys.stderr)
      #sys.exit(7)

    if node.getFuncSymbol().getReturnType() == Scope.Type(Scope.InnerType.VOID):
      # Void return type
      # This means retExpr is empty
      # So, uh, do nothing...
      pass

    else:

      if retExpr.lval:
        retExpr = self.rvalify(retExpr)

      co.code.append(retExpr)

      if retExpr.type == Scope.Type(Scope.InnerType.INT):
        co.code.append(Sw(retExpr.temp, "fp", "8"))
        co.type = Scope.Type(Scope.InnerType.INT)

      elif retExpr.type == Scope.Type(Scope.InnerType.FLOAT):
        co.code.append(Fsw(retExpr.temp, "fp", "8"))
        co.type = Scope.Type(Scope.InnerType.FLOAT)

      elif retExpr.type == Scope.Type.pointerToType(Scope.Type(Scope.InnerType.FLOAT)):
        co.code.append(Sw(retExpr.temp, 'fp', '8'))
        co.type = retExpr.type

      elif retExpr.type == Scope.Type.pointerToType(Scope.Type(Scope.InnerType.INT)):
        co.code.append(Sw(retExpr.temp, 'fp', '8'))
        co.type = retExpr.type


      # TO DO: Add something to handle return of pointer types
      # This is necessary for test 6 to not fail

       


    co.code.append(J(self.generateFunctionOutLabel()))
    return co
  
  def preprocessFunctionNode(self, node: FunctionNode):
		#Generate function label information, used for other labels inside function

    self.currFunc = node.getFuncName()

		# reset register counts; each function uses new registers!
    self.intRegCount = 0
    self.floatRegCount = 0

	# FILL IN FOR STEP 4
	# 
	# Generate code for functions
	# 
	# Step 1: add the label for the beginning of the function
	# 
	# Step 2: manage frame  pointer
	# 			a. Save old frame pointer
	# 			b. Move frame pointer to point to base of activation record (current sp)
	# 			c. Update stack pointer
	# 
	# Step 3: allocate new stack frame (use scope infromation from FunctionNode)
	# 
	# Step 4: save registers on stack (Can inspect intRegCount and floatRegCount to know what to save)
	# 
	# Step 5: add the code from the function body
	# 
	# Step 6: add post-processing code:
	# 			a. Label for `return` statements inside function body to jump to
	# 			b. Restore registers
	# 			c. Deallocate stack frame (set stack pointer to frame pointer)
	# 			d. Reset fp to old location
	# 			e. Return from function

  def postprocessFunctionNode(self, node: FunctionNode, body: CodeObject) -> CodeObject:
    
    co = CodeObject()

    numIntRegsToSave = self.intRegCount
    numFloatRegsToSave = self.floatRegCount
    #print("; Need to save " + str(numIntRegsToSave) + " int regs")
    #print("; Need to save " + str(numFloatRegsToSave) + " float regs")

    co.code.append("func_" + self.currFunc + ":")
    # FILL IN

    #Step 2: Manage frame pointer
    #Step 2a: save old frame pointer
    co.code.append(Sw("fp", "sp", "0"))
    #Step 2b: move frame pointer to current sp
    co.code.append(Mv("sp", "fp"))
    #Step 2c: update stack pointer

    #Step 3: Allocate new stack frame
    #This code is probably wrong
    co.code.append(Addi("sp", "-4", "sp")) 
    #Allocate space for local variables
    #Need to figure out how to count the number of local variables
    
    #co.code.append(";Processing local variables")
    #co.code.append(";Working in function: " + node.funcName)
    #co.code.append(";Number of locals: " + str(node.scope.getNumLocals()))
    numlocals = node.scope.getNumLocals();
    co.code.append(Addi("sp", str(-4*numlocals), "sp"))


    #Step 4: save registers on stack
    #Step 4a: save int temporaries
    #co.code.append("; Saving: " + str(numIntRegsToSave) + " Int regs")
    for i in range(1, numIntRegsToSave + 1, 1):
      co.code.append(Sw("t"+str(i), "sp", "0"))
      co.code.append(Addi("sp", "-4", "sp"))

      #print("; Saving register t" + str(i))

    #Step 4b: save float temporaries
    #co.code.append("; Saving: " + str(numFloatRegsToSave) + " Float regs")
    for i in range(1, numFloatRegsToSave + 1, 1):
      co.code.append(Fsw("f"+str(i), "sp", "0"))
      co.code.append(Addi("sp", "-4", "sp"))


    #Step 5: Add code from function body
    #co.code.append("; Putting code from func_" + self.currFunc + " here!")
    co.code.extend(body.code)
    #co.code.append("; Done with code from func_" + self.currFunc + "!")

    #Step 6: post-processing code
    #Step 6a: label
    co.code.append("func_ret_" + self.currFunc + ":")
    #Step 6b: restore registers
    for i in range(numFloatRegsToSave, 0, -1):
      co.code.append(Addi("sp", "4", "sp"))
      co.code.append(Flw("f"+str(i), "sp", "0"))
    for i in range(numIntRegsToSave, 0, -1):
      co.code.append(Addi("sp", "4", "sp"))
      co.code.append(Lw("t"+str(i), "sp", "0"))
   

    #co.code.append(Addi("sp", str(-4*numlocals), "sp"))
    #co.code.append(Addi("sp", "4", "sp"))
    #Step 6c: deallocate stack frame
    co.code.append(Mv("fp", "sp"))
    #Step 6d: reset FP to old location
    co.code.append(Lw("fp", "fp", "0"))

    #Step 6e: RET
    co.code.append(Ret()) # Generate RET instruction
    #Step 7: what is the type of this object?
    #co.type = Scope.Type.INT # temporary fix

    # Code object complete, return!
    return co

	# Generate code for the list of functions. This is the "top level" code generation function
	# 
	# Step 1: Set fp to point to sp
	# 
	# Step 2: Insert a JR to main
	# 
	# Step 3: Insert a HALT
	# 
	# Step 4: Include all the code of the functions

  def postprocessFunctionListNode(self, node: FunctionListNode, functions: List[CodeObject]) -> CodeObject:
    co = CodeObject()

    co.code.append(Mv("sp", "fp"))
    co.code.append(Jr(self.generateFunctionLabel("main")))
    co.code.append(Halt())
    co.code.append(Blank())

    # Add code for each of the functions
    for c in functions:
      co.code.extend(c.code)
      co.code.append(Blank())
    
    return co

	# FILL IN FOR STEP 4
	# 
	# Generate code for a call expression
	# 
	# Step 1: For each argument:
	# 
	# 	Step 1a: insert code of argument (don't forget to rvalify!)
	# 
	# 	Step 1b: push result of argument onto stack 
	# 
	# Step 2: alloate space for return value
	# 
	# Step 3: push current return address onto stack
	# 
	# Step 4: jump to function
	# 
	# Step 5: pop return address back from stack
	# 
	# Step 6: pop return value into fresh temporary (destination of call expression)
	# 
	# Step 7: remove arguments from stack (move sp)
  #
  # FOR STEP 6: Add special handling for malloc and free
  #
  # FOR STEP 6: Make sure to handle VOID functions properly
  def postprocessCallNode(self, node: CallNode, args: List[CodeObject]) -> CodeObject:
    co = CodeObject()

    #print("Processing Call Node to function" + str(node.getFuncName()), file=sys.stderr)

    #print("Call node has type: " + str(node.type), file=sys.stderr)
    #co.code.append("; Call node has args: " + args)
    #co.code.append("; Processing Call Node")
    #print(node.funcName)
    # Step 1: for each argument
    # Step 1a: insert code of argument (rvalify!)
    # Step 1b: push result of arg onto stack
    #co.code.append("; Processing " + str(len(args)) + " args")
    for arg in args:
      if arg.lval:
        #co.code.append("; arg is lval, rvalifying")
        #co.code.append("; code before rvalifying")
        #co.code.append(arg)
        #co.code.append("; done before rvalifying")
        arg = self.rvalify(arg)
      #co.code.append("; arg code here")
      co.code.append(arg.code) # Step 1a
      #co.code.append("; end arg code")

      if arg.type == Scope.Type(Scope.InnerType.INT):
        co.code.append(Sw(arg.temp, "sp", "0"))

      elif arg.type == Scope.Type(Scope.InnerType.FLOAT):
        co.code.append(Fsw(arg.temp, "sp", "0"))

      else:
        # If arg is not an int or float, it must be a pointer
        co.code.append(Sw(arg.temp, 'sp', '0'))



      # This should be dependent on number of args
      #co.code.append("; Fucked up number here!")  
      co.code.append(Addi("sp", "-4", "sp"))
    #co.code.append("; arg processing complete")
    #Step 2: Allocate space for return value (and ra)

    # Need to only do this if the type is not void, because voids have no return value
    co.code.append(Addi("sp", "-4", "sp"))

    #Step 3: Push current return address onto stack
    co.code.append(Sw("ra", "sp", "0")) # Return address at sp+0, return value at sp+4

    #Step 4: JR to function
    co.code.append(Addi("sp", "-4", "sp"))
    co.code.append(Jr("func_" + node.funcName))
    co.code.append(Addi("sp", "4", "sp"))
    #Step 5: Pop return address back
    co.code.append(Lw("ra", "sp", "0"))
    co.code.append(Addi("sp", "4", "sp")) # Same thing on this end, need to only do this if function is non-void

    #Step 6: Pop return value into new temporary
    
    if node.type == Scope.Type(Scope.InnerType.INT):
      newtemp = self.generateTemp(Scope.InnerType.INT)
      co.code.append(Lw(newtemp, "sp", "0"))
      co.temp = newtemp
    elif node.type == Scope.Type(Scope.InnerType.FLOAT):
      newtemp = self.generateTemp(Scope.InnerType.FLOAT)
      co.code.append(Flw(newtemp, "sp", "0"))
      co.temp = newtemp
    elif node.type == Scope.Type(Scope.InnerType.VOID):
      pass
    elif node.type == Scope.Type.pointerToType(Scope.Type(Scope.InnerType.FLOAT)):
      newtemp = self.generateTemp(Scope.InnerType.INT)
      co.code.append(Lw(newtemp, "sp", "0"))
      co.temp = newtemp
      # What should the temp of this node be if it's a void function?
    # Need more cases here: functions can return void, pointers, etc.  For pointer, look at test6.uC where it returns a float pointer
    # None of the tests have int * returns but this should be handled just in case


    #Step 7: Remove arguments from stack (move SP back up)
    co.code.append(Addi("sp", str(4*len(args)), "sp"))
    

    #Step 8: Code object complete; now return
    co.type = node.type #Node has the return type

    #co.code.append("; Finished with Call Node")
    #co.code.append(J("func_ret_" + node.funcName)) this belongs in ret node not here
    return co
	 






   # Generate code for * (expr)
	 # 
	 # Goal: convert the r-val coming from expr (a computed address) into an l-val (an address that can be loaded/stored)
	 # 
	 # Step 0: Create new code object
	 # 
	 # Step 1: Rvalify expr if needed
	 # 
	 # Step 2: Copy code from expr (including any rvalification) into new code object
	 # 
	 # Step 3: New code object has same temporary as old code, but now is marked as an l-val
	 # 
	 # Step 4: New code object has an "unwrapped" type: if type of expr is * T, type of temporary is T. Can get this from node
  
  
  def postprocessPtrDerefNode(self, node: PtrDerefNode, expr: CodeObject) -> CodeObject:
    co = CodeObject()
    #print("Processing pointer dereference node!", file=sys.stderr)
    #print("Node type is: " + str(node.type), file=sys.stderr)
    #print("Expr lval? " + str(expr.lval), file=sys.stderr)
    #print("Expr temp: " + str(expr.temp), file=sys.stderr)
    #print("Expr type: " + str(expr.type), file=sys.stderr)
    #print("Expr code is:" , file=sys.stderr)
    #print("Expr is var? " + str(expr.isVar()), file=sys.stderr)

    #print(expr.code, file=sys.stderr)
    #FILL IN FOR STEP 6

    if expr.lval:
      expr = self.rvalify(expr)

    co.code.extend(expr.code)
    co.temp = expr.temp
    #co.code.append("; end of deref")
    #co.code.append("; temp:" + str(expr.temp))
    #if expr.type == Scope.Type.pointerToType(Scope.Type(Scope.InnerType.INT)):
      #print("You're here", file=sys.stderr)
    #  newtemp = self.generateTemp(Scope.InnerType.INT)
    #  co.code.append(Lw(newtemp, expr.temp, '0'))
    #  co.temp = newtemp
    #elif expr.type == Scope.Type.pointerToType(Scope.Type(Scope.InnerType.FLOAT)):
    #  newtemp = self.generateTemp(Scope.InnerType.FLOAT)
    #  co.code.append(Flw(newtemp, expr.temp, '0'))
    #  co.temp = newtemp

    
    co.lval = True
    
    co.type = node.type

    return co

 # Generate code for a & (expr)
 # 
 # Goal: convert the lval coming from expr (an address) to an r-val (a piece of data that can be used)
 # 
 # Step 0: Create new code object
 # 
 # Step 1: If lval is a variable, generate code to put address into a register (e.g., generateAddressFromVar)
 #			Otherwise just copy code from other code object
 # 
 # Step 2: New code object has same temporary as existing code, but is an r-val
 # 
 # Step 3: New code object has a "wrapped" type. If type of expr is T, type of temporary is *T. Can get this from node
  def postprocessAddrOfNode(self, node: AddrOfNode, expr: CodeObject) -> CodeObject:
    co = CodeObject()
    #print("Processing address of node", file=sys.stderr)
    #print("Node type: ", node.type, file=sys.stderr)
    #print("Expr type: ", expr.type, file=sys.stderr)
    #print("Expr is var? ", expr.isVar(), file=sys.stderr)
    #print("Expr temp: " + str(expr.temp), file=sys.stderr)
    # FILL IN CODE FOR STEP 6

    co.type = node.type

    if expr.isVar():
      # If the expression we're &ing is a variable, we can just get its address and be done with it
      address = self.generateAddrFromVariable(expr)
      symbol = expr.getSTE()
      #co.code.append("STE:" + str(symbol))
      # What temp did we put stuff into?
      #print(self.getIntRegCount(), file=sys.stderr)
      newtemp = 't' + str(self.getIntRegCount()-1)
      co.temp = newtemp
      #co.code.append("; Start of & node")
      co.code.append(address)
      #co.code.append("; End of & node.  newtemp: " + str(newtemp))
    
    else:
      # If it's not a var...
      #co.code.append("; & Node with non var")
      co.code.extend(expr.code)
      co.temp = expr.temp

    co.type = node.type
    co.lval = False

    return co

	# Generate code for malloc
	# 
	# Step 0: Create new code object
	# 
	# Step 1: Add code from expression (rvalify if needed)
	# 
	# Step 2: Create new MALLOC instruction
	# 
	# Step 3: Set code object type to INFER
  def postprocessMallocNode(self, node: MallocNode, expr: CodeObject) -> CodeObject:
    co = CodeObject()
    # FILL IN CODE FOR STEP 6

    if expr.lval:
      expr = self.rvalify(expr)
    
    co.code.extend(expr.code)

    # Need new temp because malloc returns a pointer
    newtemp = self.generateTemp(Scope.InnerType.INT)
    co.code.append(Malloc(expr.temp, newtemp))

    co.temp = newtemp

    co.type = Scope.InnerType.INFER

    return co

	#  Generate code for free
	#  
	#  Step 0: Create new code object
	#  
	#  Step 1: Add code from expression (rvalify if needed)
	#  
	#  Step 2: Create new FREE instruction
  def postprocessFreeNode(self, node: FreeNode, expr: CodeObject) -> CodeObject:
    co = CodeObject()
    #FILL IN CODE FOR STEP 6
    if expr.lval:
      expr = self.rvalify(expr)
    
    co.code.extend(expr.code)
    co.code.append(Free(expr.temp))

    return co

	# Generate a fresh temporary
	# 
	# @return new temporary register name
  
  def generateTemp(self, t: Scope.InnerType) -> str:
    if t == Scope.InnerType.INT or t == Scope.InnerType.PTR:
      s = self.intTempPrefix + str(self.intRegCount)
      self.intRegCount += 1
      return s
    elif t == Scope.InnerType.FLOAT:
      s = self.floatTempPrefix + str(self.floatRegCount)
      self.floatRegCount += 1
      return s
    else:
      raise Exception("Generating temp for bad type")

  def generateLoopLabel(self) -> str:
    self.loopLabel += 1
    return "loop_" + str(self.loopLabel)

  def generateElseLabel(self) -> str:
    self.elseLabel += 1
    return "else_" + str(self.elseLabel)

  def generateOutLabel(self) -> str:
    self.outLabel += 1
    return "out_" + str(self.outLabel)
  
  def generateFunctionLabel(self, func = None) -> str:
    if func is None:
      return "func_" + self.currFunc
    else:
      return "func_" + func
    
  def generateFunctionOutLabel(self) -> str:
    return "func_ret_" + self.currFunc
  

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

  def rvalify(self, lco : CodeObject) -> CodeObject:
    # Step 0
    co = CodeObject()
    #co.code.append("; start rvalify")
    
    assert(lco.lval is True)

    #print("lco type: " + str(lco.type), file=sys.stderr)
    #print("lco is var? " + str(lco.isVar()), file=sys.stderr)

    if lco.isVar():
      symbol = lco.getSTE()
      symboladdress = symbol.addressToString()
      if (not symbol.isLocal()): # Global case
        newaddrtemp = self.intTempPrefix + str(self.intRegCount)
        newaddr = self.generateAddrFromVariable(lco)
        co.code.append(newaddr)
        if lco.type == Scope.Type(Scope.InnerType.INT):
          newtemp = self.generateTemp(Scope.InnerType.INT)
          co.code.append(Lw(newtemp, newaddrtemp, "0"))
        elif lco.type == Scope.Type(Scope.InnerType.FLOAT):
          newtemp = self.generateTemp(Scope.InnerType.FLOAT)
          co.code.append(Flw(newtemp, newaddrtemp, "0"))
        else:
          #print("Rvalify pointer case global", file=sys.stderr)
          newtemp = self.generateTemp(Scope.InnerType.INT)
          co.code.append(La(newtemp, newaddr))
          #pass
          #print("TYPE ERROR", file=sys.stderr)
          #sys.exit(7)
        co.temp = newtemp
      else: 
        #co.code.append("; rvalifying local var")
        #newaddr = self.generateAddrFromVariable(lco)
        #co.code.append("; local newaddr:" + symboladdress)
        if lco.type == Scope.Type(Scope.InnerType.INT):
          newtemp = self.generateTemp(Scope.InnerType.INT)
          co.code.append(Lw(newtemp, "fp", symboladdress))
        elif lco.type == Scope.Type(Scope.InnerType.FLOAT):
          newtemp = self.generateTemp(Scope.InnerType.FLOAT)
          co.code.append(Flw(newtemp, "fp", symboladdress))
        else:
          #print("Rvalify pointer case local", file=sys.stderr)
          newtemp = self.generateTemp(Scope.InnerType.INT)
          #print("New temp: " + str(newtemp), file=sys.stderr)
          co.code.append(Lw(newtemp, 'fp', symboladdress))
          #newtemp = self.generateTemp(Scope.InnerType.INT)
          #co.code.append(Lw(newtemp, oldtemp, '0'))

          #co.code.append(Addi('fp', newaddr, newtemp))
          
          #co.code.append(La(newtemp, newaddr))
          #print("Type Error", file=sys.stderr)
          #sys.exit(7)

      co.temp = newtemp
      
    else:
      #print("Lco is not var", file=sys.stderr)
      #co.code.append("; lco is not var")
      co.code.extend(lco.code)
      #co.code.append("; - issue here - ")
      #co.code.append("; lco is type: " + str(lco.type))
      if lco.type == Scope.Type(Scope.InnerType.FLOAT):
        newtemp = self.generateTemp(Scope.InnerType.FLOAT)
        co.code.append(Flw(newtemp, lco.temp, '0'))
      else:
        newtemp = self.generateTemp(Scope.InnerType.INT)
        co.code.append(Lw(newtemp, lco.temp, '0'))
      co.temp = newtemp
    #Step 2

    #co.code.append("; end rvalify")
    co.type = lco.type 
    co.lval = False
    return co

	# Generate an instruction sequence that holds the address of the variable in a code object
	# 
	# If it's a global variable, just get the address from the symbol table
	# 
	# If it's a local variable, compute the address relative to the frame pointer (fp)
	# 
	# @param lco The code object holding a variable
	# @return a list of instructions that puts the address of the variable in a register

  def generateAddrFromVariable(self, lco: CodeObject) -> InstructionList:
    il = InstructionList()

    #Step 1:
    symbol = lco.getSTE()
    address = symbol.addressToString()

    #Step 2:
    if symbol.isLocal():
      # If local, address is offset
			# need to load fp + offset
			# addi tmp' fp offset
      compAddr = Addi("fp", address, self.generateTemp(Scope.InnerType.INT))
    else:
			#If global, address in symbol table is the right location
      #la tmp' addr // Register type needs to be an int
      compAddr = La(self.generateTemp(Scope.InnerType.INT), address)
    il.append(compAddr) # add instruction

    return il

  def reverseCompType(self, cmptype) -> int:
    # Generates the reverse comparison type based on input comparison type and data type
    #intdictionary = {1:2, 2:1, 3:6, 4:5, 5:4, 6:3}
    #intdictionary = {'==':2, '!=':1, '<':6, '<=':5, '>':4, '>=':3}
    
    dictionary = {'OpType.EQ':'OpType.NE', 'OpType.NE':'OpType.EQ', 'OpType.LT':'OpType.GE', 'OpType.LE':'OpType.GT', 'OpType.GT':'OpType.LE', 'OpType.GE':'OpType.LT'}
    #print("Reversing: ", cmptype, file=sys.stderr)
    #print("Reversed type: ", dictionary[str(cmptype)], file=sys.stderr)
    
    return dictionary[str(cmptype)]
