; Symbol table GLOBAL
; name curVal type Type.FLOAT location 0x20000000
; name x type Type.FLOAT location 0x20000004
; name degree type Type.INT location 0x20000008
; Function: Type.FLOAT addX([<Type.FLOAT: 3>, <Type.FLOAT: 3>])
; name val type Type.STRING location 0x10000000 value "Enter x value to evaluate: "
; name degreePrompt type Type.STRING location 0x10000004 value "Enter a degree: "
; name prompt type Type.STRING location 0x10000008 value "Enter coefficient: "
; Function: Type.INT main([])

; Symbol table main
; name cur type Type.INT location -4

; Symbol table addX
; name x type Type.FLOAT location 12
; name curVal type Type.FLOAT location 16
; name coeff type Type.FLOAT location -4

; generating code to print ; name val type Type.STRING location 0x10000000 value "Enter x value to evaluate: "
; generating code to print ; name degreePrompt type Type.STRING location 0x10000004 value "Enter a degree: "
; generating code to print ; name prompt type Type.STRING location 0x10000008 value "Enter coefficient: "
.section .text
;Current temp: 
;IR Code: 
MV fp, sp
JR func_main
HALT

func_main:
SW fp, 0(sp)
MV fp, sp
ADDI sp, sp, -4
ADDI sp, sp, -4
SW t0, 0(sp)
ADDI sp, sp, -4
SW t1, 0(sp)
ADDI sp, sp, -4
SW t2, 0(sp)
ADDI sp, sp, -4
SW t3, 0(sp)
ADDI sp, sp, -4
SW t4, 0(sp)
ADDI sp, sp, -4
SW t5, 0(sp)
ADDI sp, sp, -4
SW t6, 0(sp)
ADDI sp, sp, -4
SW t7, 0(sp)
ADDI sp, sp, -4
SW t8, 0(sp)
ADDI sp, sp, -4
SW t9, 0(sp)
ADDI sp, sp, -4
SW t10, 0(sp)
ADDI sp, sp, -4
SW t11, 0(sp)
ADDI sp, sp, -4
SW t12, 0(sp)
ADDI sp, sp, -4
SW t13, 0(sp)
ADDI sp, sp, -4
SW t14, 0(sp)
ADDI sp, sp, -4
SW t15, 0(sp)
ADDI sp, sp, -4
SW t16, 0(sp)
ADDI sp, sp, -4
SW t17, 0(sp)
ADDI sp, sp, -4
SW t18, 0(sp)
ADDI sp, sp, -4
SW t19, 0(sp)
ADDI sp, sp, -4
SW t20, 0(sp)
ADDI sp, sp, -4
SW t21, 0(sp)
ADDI sp, sp, -4
SW t22, 0(sp)
ADDI sp, sp, -4
SW t23, 0(sp)
ADDI sp, sp, -4
SW t24, 0(sp)
ADDI sp, sp, -4
FSW f0, 0(sp)
ADDI sp, sp, -4
FSW f1, 0(sp)
ADDI sp, sp, -4
FSW f2, 0(sp)
ADDI sp, sp, -4
FSW f3, 0(sp)
ADDI sp, sp, -4
FSW f4, 0(sp)
ADDI sp, sp, -4
FSW f5, 0(sp)
ADDI sp, sp, -4
LA t0, 0x20000000
FIMM.S f0, 0.0
FSW f0, 0(t0)
LI t1, 0
SW t1, -4(fp)
LA t2, 0x10000000
PUTS t2
GETF f1
LA t3, 0x20000004
FSW f1, 0(t3)
LA t4, 0x10000004
PUTS t4
GETI t5
LA t6, 0x20000008
SW t5, 0(t6)
LA t11, 0x20000008
LA t8, 0x20000008
LW t9, 0(t8)
LI t7, 1
ADD t10, t9, t7
SW t10, 0(t11)
loop_1:
LW t13, -4(fp)
LA t14, 0x20000008
LW t15, 0(t14)
BGE t13, t15, out_1
;Current temp: 
;IR Code: 
LW t18, -4(fp)
LI t16, 1
ADD t19, t18, t16
SW t19, -4(fp)
LA t22, 0x20000000
LA t20, 0x20000000
FLW f2, 0(t20)
FSW f2, 0(sp)
ADDI sp, sp, -4
LA t21, 0x20000004
FLW f3, 0(t21)
FSW f3, 0(sp)
ADDI sp, sp, -4
ADDI sp, sp, -4
SW ra, 0(sp)
ADDI sp, sp, -4
JR func_addX
ADDI sp, sp, 4
LW ra, 0(sp)
ADDI sp, sp, 4
FLW f4, 0(sp)
ADDI sp, sp, 4
FSW f4, 0(t22)
J loop_1
out_1:
LA t23, 0x20000000
FLW f5, 0(t23)
PUTF f5
;Current temp: t24
;IR Code: 
LI t24, 0
SW t24, 8(fp)
J func_ret_main
func_ret_main:
ADDI sp, sp, 4
FLW f5, 0(sp)
ADDI sp, sp, 4
FLW f4, 0(sp)
ADDI sp, sp, 4
FLW f3, 0(sp)
ADDI sp, sp, 4
FLW f2, 0(sp)
ADDI sp, sp, 4
FLW f1, 0(sp)
ADDI sp, sp, 4
FLW f0, 0(sp)
ADDI sp, sp, 4
LW t24, 0(sp)
ADDI sp, sp, 4
LW t23, 0(sp)
ADDI sp, sp, 4
LW t22, 0(sp)
ADDI sp, sp, 4
LW t21, 0(sp)
ADDI sp, sp, 4
LW t20, 0(sp)
ADDI sp, sp, 4
LW t19, 0(sp)
ADDI sp, sp, 4
LW t18, 0(sp)
ADDI sp, sp, 4
LW t17, 0(sp)
ADDI sp, sp, 4
LW t16, 0(sp)
ADDI sp, sp, 4
LW t15, 0(sp)
ADDI sp, sp, 4
LW t14, 0(sp)
ADDI sp, sp, 4
LW t13, 0(sp)
ADDI sp, sp, 4
LW t12, 0(sp)
ADDI sp, sp, 4
LW t11, 0(sp)
ADDI sp, sp, 4
LW t10, 0(sp)
ADDI sp, sp, 4
LW t9, 0(sp)
ADDI sp, sp, 4
LW t8, 0(sp)
ADDI sp, sp, 4
LW t7, 0(sp)
ADDI sp, sp, 4
LW t6, 0(sp)
ADDI sp, sp, 4
LW t5, 0(sp)
ADDI sp, sp, 4
LW t4, 0(sp)
ADDI sp, sp, 4
LW t3, 0(sp)
ADDI sp, sp, 4
LW t2, 0(sp)
ADDI sp, sp, 4
LW t1, 0(sp)
ADDI sp, sp, 4
LW t0, 0(sp)
MV sp, fp
LW fp, 0(fp)
RET

func_addX:
SW fp, 0(sp)
MV fp, sp
ADDI sp, sp, -4
ADDI sp, sp, -4
SW t0, 0(sp)
ADDI sp, sp, -4
SW t1, 0(sp)
ADDI sp, sp, -4
SW t2, 0(sp)
ADDI sp, sp, -4
SW t3, 0(sp)
ADDI sp, sp, -4
FSW f0, 0(sp)
ADDI sp, sp, -4
FSW f1, 0(sp)
ADDI sp, sp, -4
FSW f2, 0(sp)
ADDI sp, sp, -4
FSW f3, 0(sp)
ADDI sp, sp, -4
FSW f4, 0(sp)
ADDI sp, sp, -4
FSW f5, 0(sp)
ADDI sp, sp, -4
LA t0, 0x10000008
PUTS t0
GETF f0
FSW f0, -4(fp)
;Current temp: f5
;IR Code: 
FLW f1, 12(fp)
FLW f2, 16(fp)
FMUL.S f3, f1, f2
FLW f4, -4(fp)
FADD.S f5, f3, f4
FSW f5, 8(fp)
J func_ret_addX
func_ret_addX:
ADDI sp, sp, 4
FLW f5, 0(sp)
ADDI sp, sp, 4
FLW f4, 0(sp)
ADDI sp, sp, 4
FLW f3, 0(sp)
ADDI sp, sp, 4
FLW f2, 0(sp)
ADDI sp, sp, 4
FLW f1, 0(sp)
ADDI sp, sp, 4
FLW f0, 0(sp)
ADDI sp, sp, 4
LW t3, 0(sp)
ADDI sp, sp, 4
LW t2, 0(sp)
ADDI sp, sp, 4
LW t1, 0(sp)
ADDI sp, sp, 4
LW t0, 0(sp)
MV sp, fp
LW fp, 0(fp)
RET


.section .strings
0x10000000 "Enter x value to evaluate: "
0x10000004 "Enter a degree: "
0x10000008 "Enter coefficient: "
