; Symbol table 
; Function: InnerType.INT main([])

; Symbol table main
; name a type InnerType.INT location -4
; name b type InnerType.INT location -8
; name c type InnerType.INT location -12

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
ADDI sp, sp, -12
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
LI t0, 2
SW t0, -4(fp)
LW t1, -4(fp)
SRLI t2, t1, 1
SW t2, -8(fp)
LW t3, -4(fp)
SLLI t4, t3, 1
SW t4, -12(fp)
LW t5, -4(fp)
PUTI t5
LW t6, -8(fp)
PUTI t6
LW t7, -12(fp)
PUTI t7
;Current temp: t8
;IR Code: 
LI t8, 0
SW t8, 8(fp)
J func_ret_main
func_ret_main:
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
