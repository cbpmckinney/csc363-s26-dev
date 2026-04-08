; Symbol table GLOBAL
; Function: Type.INT foo([<Type.INT: 2>])
; Function: Type.INT main([])

; Symbol table main
; name a type Type.INT location -4
; name b type Type.INT location -8

; Symbol table foo
; name a type Type.INT location 12

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
LI t0, 3
SW t0, -4(fp)
; Processing Call Node
; Processing 1 args
LW t2, -4(fp)
SW t2, 0(sp)
ADDI sp, sp, -4
; arg processing complete
ADDI sp, sp, -4
SW ra, 0(sp)
ADDI sp, sp, -4
JR func_foo
ADDI sp, sp, 4
LW ra, 0(sp)
ADDI sp, sp, 4
LW t3, 0(sp)
ADDI sp, sp, 4
; Finished with Call Node
SW t3, -8(fp)
;Current temp: t4
;IR Code: 
LI t4, 0
SW t4, 8(fp)
func_ret_main:
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
MV sp, fp
LW fp, 0(fp)
RET

func_foo:
SW fp, 0(sp)
MV fp, sp
ADDI sp, sp, -4
ADDI sp, sp, 0
SW t0, 0(sp)
ADDI sp, sp, -4
SW t1, 0(sp)
ADDI sp, sp, -4
;Current temp: t1
;IR Code: 
LW t1, 12(fp)
SW t1, 8(fp)
func_ret_foo:
ADDI sp, sp, 4
LW t0, 0(sp)
ADDI sp, sp, 4
LW t1, 0(sp)
MV sp, fp
LW fp, 0(fp)
RET


.section .strings
