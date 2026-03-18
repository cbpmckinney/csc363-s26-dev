; Symbol table 
; Function: InnerType.INT main([])

; Symbol table main
; name x type InnerType.INT location -4
; name y type InnerType.FLOAT location -8

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
FSW f6, 0(sp)
ADDI sp, sp, -4
FSW f7, 0(sp)
ADDI sp, sp, -4
FSW f8, 0(sp)
ADDI sp, sp, -4
FSW f9, 0(sp)
ADDI sp, sp, -4
FIMM.S f0, 2.3
FSW f0, -8(fp)
LI t0, 2
FLW f1, -8(fp)
IMOVF.S f2, t0
FMUL.S f3, f2, f1
LI t1, 2
IMOVF.S f4, t1
FMUL.S f5, f3, f4
FMOVI.S t2, f5
SW t2, -4(fp)
LW t3, -4(fp)
PUTI t3
LI t4, 2
FLW f6, -8(fp)
IMOVF.S f7, t4
FMUL.S f8, f7, f6
FMOVI.S t5, f8
LI t6, 2
MUL t7, t5, t6
SW t7, -4(fp)
LW t8, -4(fp)
PUTI t8
;Current temp: t9
;IR Code: 
LI t9, 0
SW t9, 8(fp)
J func_ret_main
func_ret_main:
ADDI sp, sp, 4
FLW f9, 0(sp)
ADDI sp, sp, 4
FLW f8, 0(sp)
ADDI sp, sp, 4
FLW f7, 0(sp)
ADDI sp, sp, 4
FLW f6, 0(sp)
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
