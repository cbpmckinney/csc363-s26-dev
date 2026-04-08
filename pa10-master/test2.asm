; Symbol table GLOBAL
; Function: Type.INT fact([<Type.INT: 2>])
; Function: Type.INT main([])

; Symbol table main
; name res type Type.INT location -4

; Symbol table fact
; name n type Type.INT location 12

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
; Saving: 5 Int regs
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
; Saving: 0 Float regs
; Processing Call Node
; Processing 1 args
LI t0, 5
SW t0, 0(sp)
ADDI sp, sp, -4
; arg processing complete
ADDI sp, sp, -4
SW ra, 0(sp)
ADDI sp, sp, -4
JR func_fact
ADDI sp, sp, 4
LW ra, 0(sp)
ADDI sp, sp, 4
LW t1, 0(sp)
ADDI sp, sp, 4
; Finished with Call Node
SW t1, -4(fp)
LW t3, -4(fp)
PUTI t3
;Current temp: t4
;IR Code: 
LI t4, 0
SW t4, 8(fp)
; Generating function out label
J func_ret_main
func_ret_main:
ADDI sp, sp, 4
LW t4, 0(sp)
ADDI sp, sp, 4
LW t3, 0(sp)
ADDI sp, sp, 4
LW t2, 0(sp)
ADDI sp, sp, 4
LW t1, 0(sp)
MV sp, fp
LW fp, 0(fp)
RET

func_fact:
SW fp, 0(sp)
MV fp, sp
ADDI sp, sp, -4
ADDI sp, sp, 0
; Saving: 12 Int regs
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
; Saving: 0 Float regs
LW t2, 12(fp)
LI t0, 1
BGT t2, t0, else_1
;Current temp: t3
;IR Code: 
LI t3, 1
SW t3, 8(fp)
; Generating function out label
J func_ret_fact
J out_1
else_1:
;Current temp: t11
;IR Code: 
LW t10, 12(fp)
; Processing Call Node
; Processing 1 args
LW t6, 12(fp)
LI t4, 1
SUB t7, t6, t4
SW t7, 0(sp)
ADDI sp, sp, -4
; arg processing complete
ADDI sp, sp, -4
SW ra, 0(sp)
ADDI sp, sp, -4
JR func_fact
ADDI sp, sp, 4
LW ra, 0(sp)
ADDI sp, sp, 4
LW t8, 0(sp)
ADDI sp, sp, 4
; Finished with Call Node
MUL t11, t10, t8
SW t11, 8(fp)
; Generating function out label
J func_ret_fact
out_1:
func_ret_fact:
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
MV sp, fp
LW fp, 0(fp)
RET


.section .strings
