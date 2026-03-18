; Symbol table 
; Function: InnerType.INT main([])

; Symbol table main
; name x type InnerType.INT location -4
; name y type InnerType.FLOAT location -8
; name z type InnerType.FLOAT location -12

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
FIMM.S f0, 3.5
FSW f0, -8(fp)
FIMM.S f1, 2.6
FSW f1, -12(fp)
FLW f2, -8(fp)
FLW f3, -12(fp)
FADD.S f4, f2, f3
FMOVI.S t0, f4
SW t0, -4(fp)
LW t1, -4(fp)
PUTI t1
;Current temp: t2
;IR Code: 
LI t2, 0
SW t2, 8(fp)
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
LW t3, 0(sp)
ADDI sp, sp, 4
LW t2, 0(sp)
ADDI sp, sp, 4
LW t1, 0(sp)
MV sp, fp
LW fp, 0(fp)
RET


.section .strings
