; Symbol table 
; name a type Type.INT location 0x20000000
; Function: Type.INT main([])

; Symbol table main

.section .text
;Current temp: 
;IR Code: 
MV fp, sp
JR func_main
HALT

func_main:
SW fp, 0(sp)
MV fp, sp
; Putting code from func_main here!
LA t1, 0x20000000
LI t0, 3
SW t0, 0(t1)
LA t6, 0x20000000
LA t3, 0x20000000
LW t4, 0(t3)
LI t2, 2
ADD t5, t4, t2
SW t5, 0(t6)
; Done with code from func_main!
func_ret_main:
RET


.section .strings
