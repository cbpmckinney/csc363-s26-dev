; Symbol table GLOBAL
; Function: Type.INT foo([<Type.INT: 2>, <Type.INT: 2>])
; Function: Type.FLOAT bar([<Type.FLOAT: 3>, <Type.FLOAT: 3>])
; Function: Type.INT main([])

; Symbol table main
; name a type Type.INT location -4
; name b type Type.INT location -8
; name c type Type.INT location -12
; name d type Type.FLOAT location -16

; Symbol table foo
; name y type Type.INT location 12
; name x type Type.INT location 16

; Symbol table bar
; name y type Type.FLOAT location 12
; name x type Type.FLOAT location 16

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
ADDI sp, sp, -16
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
FSW f1, 0(sp)
ADDI sp, sp, -4
FSW f2, 0(sp)
ADDI sp, sp, -4
GETI t1
SW t1, -4(fp)
GETI t2
SW t2, -8(fp)
LW t4, -4(fp)
SW t4, 0(sp)
ADDI sp, sp, -4
LW t6, -8(fp)
SW t6, 0(sp)
ADDI sp, sp, -4
ADDI sp, sp, -4
SW ra, 0(sp)
ADDI sp, sp, -4
JR func_foo
ADDI sp, sp, 4
LW ra, 0(sp)
ADDI sp, sp, 4
LW t7, 0(sp)
ADDI sp, sp, 8
SW t7, -12(fp)
LW t9, -4(fp)
SW t9, 0(sp)
ADDI sp, sp, -4
LW t11, -8(fp)
SW t11, 0(sp)
ADDI sp, sp, -4
ADDI sp, sp, -4
SW ra, 0(sp)
ADDI sp, sp, -4
JR func_bar
ADDI sp, sp, 4
LW ra, 0(sp)
ADDI sp, sp, 4
LW t12, 0(sp)
ADDI sp, sp, 8
FSW t12, -16(fp)
LW t14, -12(fp)
PUTI t14
FLW f1, -16(fp)
PUTF f1
;Current temp: t16
;IR Code: 
LI t16, 0
SW t16, 8(fp)
J func_ret_main
func_ret_main:
ADDI sp, sp, 4
FLW f2, 0(sp)
ADDI sp, sp, 4
FLW f1, 0(sp)
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
MV sp, fp
LW fp, 0(fp)
RET

func_foo:
SW fp, 0(sp)
MV fp, sp
ADDI sp, sp, -4
ADDI sp, sp, 0
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
FSW f1, 0(sp)
ADDI sp, sp, -4
;Current temp: t5
;IR Code: 
LW t2, 16(fp)
LW t4, 12(fp)
ADD t5, t2, t4
SW t5, 8(fp)
J func_ret_foo
func_ret_foo:
ADDI sp, sp, 4
FLW f1, 0(sp)
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

func_bar:
SW fp, 0(sp)
MV fp, sp
ADDI sp, sp, -4
ADDI sp, sp, 0
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
;Current temp: f3
;IR Code: 
FLW f1, 16(fp)
FLW f2, 12(fp)
FSUB.S f3, f1, f2
FSW f3, 8(fp)
J func_ret_bar
func_ret_bar:
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
