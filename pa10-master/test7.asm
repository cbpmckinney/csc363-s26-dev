; Symbol table 
; name a type Type.INT location 0x20000000
; Function: Type.INT main([])

; Symbol table main
; name b type Type.INT location -4

LENGTH OF CODE: 0
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

; Done with code from func_main!



.section .strings
