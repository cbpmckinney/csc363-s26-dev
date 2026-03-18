; Symbol table 
; Function: InnerType.INT main([])

; Symbol table main
; name x type InnerType.FLOAT location -4
; name i type InnerType.INT location -8

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
SW t1, 0(sp)
ADDI sp, sp, -4
SW t2, 0(sp)
ADDI sp, sp, -4
SW t3, 0(sp)
ADDI sp, sp, -4
SW t4, 0(sp)
ADDI sp, sp, -4
FSW f1, 0(sp)
ADDI sp, sp, -4
FIMM.S f0, 2.0
FSW f0, -4(fp)
; Casting code starts here
ADDI t0, fp, -4
; Casting code ends here
LW t1, 0(None)
SW t1, -8(fp)
LW t2, -8(fp)
PUTI t2
;Current temp: t3
;IR Code: 
LI t3, 0
SW t3, 8(fp)
J func_ret_main
func_ret_main:
ADDI sp, sp, 4
FLW f1, 0(sp)
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
