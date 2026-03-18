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
SW t4, 0(sp)
ADDI sp, sp, -4
SW t5, 0(sp)
ADDI sp, sp, -4
FSW f1, 0(sp)
ADDI sp, sp, -4
FSW f2, 0(sp)
ADDI sp, sp, -4
FSW f3, 0(sp)
ADDI sp, sp, -4
FSW f4, 0(sp)
ADDI sp, sp, -4
FIMM.S f0, 3.5
FSW f0, -8(fp)
FIMM.S f1, 2.6
FSW f1, -12(fp)
; Casting code starts here
FLW f2, -8(fp)
FMOVI.S t0, f2
; Casting code ends here
; Casting code starts here
FLW f3, -12(fp)
FMOVI.S t1, f3
; Casting code ends here
ADD t2, t0, t1
SW t2, -4(fp)
LW t3, -4(fp)
PUTI t3
;Current temp: t4
;IR Code: 
LI t4, 0
SW t4, 8(fp)
J func_ret_main
func_ret_main:
ADDI sp, sp, 4
FLW f4, 0(sp)
ADDI sp, sp, 4
FLW f3, 0(sp)
ADDI sp, sp, 4
FLW f2, 0(sp)
ADDI sp, sp, 4
FLW f1, 0(sp)
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
