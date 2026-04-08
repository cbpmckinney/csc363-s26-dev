; Symbol table GLOBAL
; name a type Type.INT location 0x20000000
; name b type Type.FLOAT location 0x20000004
; Function: Type.INT main([])

; Symbol table main
; name c type Type.INT location -4
; name d type Type.FLOAT location -8

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
ADDI sp, sp, -8
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
FSW f0, 0(sp)
ADDI sp, sp, -4
FSW f1, 0(sp)
ADDI sp, sp, -4
FSW f2, 0(sp)
ADDI sp, sp, -4
FSW f3, 0(sp)
ADDI sp, sp, -4
LA t1, 0x20000000
LI t0, 2
SW t0, 0(t1)
LA t2, 0x20000004
FIMM.S f0, 3.0
FSW f0, 0(t2)
LA t3, 0x20000000
LW t4, 0(t3)
PUTI t4
LA t5, 0x20000004
FLW f1, 0(t5)
PUTF f1
LI t6, 4
SW t6, -4(fp)
FIMM.S f2, 5.0
FSW f2, -8(fp)
LW t8, -4(fp)
PUTI t8
FLW f3, -8(fp)
PUTF f3
;Current temp: t10
;IR Code: 
LI t10, 0
SW t10, 8(fp)
func_ret_main:
ADDI sp, sp, 4
FLW f0, 0(sp)
ADDI sp, sp, 4
FLW f1, 0(sp)
ADDI sp, sp, 4
FLW f2, 0(sp)
ADDI sp, sp, 4
FLW f3, 0(sp)
ADDI sp, sp, 4
LW t0, 0(sp)
ADDI sp, sp, 4
LW t1, 0(sp)
ADDI sp, sp, 4
LW t2, 0(sp)
ADDI sp, sp, 4
LW t3, 0(sp)
ADDI sp, sp, 4
LW t4, 0(sp)
ADDI sp, sp, 4
LW t5, 0(sp)
ADDI sp, sp, 4
LW t6, 0(sp)
ADDI sp, sp, 4
LW t7, 0(sp)
ADDI sp, sp, 4
LW t8, 0(sp)
ADDI sp, sp, 4
LW t9, 0(sp)
ADDI sp, sp, 4
LW t10, 0(sp)
MV sp, fp
LW fp, 0(fp)
RET


.section .strings
