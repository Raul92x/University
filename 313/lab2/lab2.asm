;Class:CSE 313 Machine Organization Lab
;Instructor: Taline Georgiou
;Term: Spring 2013
;Name(s): Raul Diaz
;Lab#2: Arithmetic Functions
;Description: in this lab we give x and y values
;and then we compute the difference of them.
;then we get the absolute value of both of them
;and store them in a register. finally you compare
;x and y and which ever one is bigger u put a value
;in a register. if its x you put a 1 and if its you u put a 2.

	
	.ORIG X3000
	LDI R1, X
	LDI R2, Y

;X-Y
	NOT R3 , R2		;1's compliment of y
	ADD R3 , R3 , #1	;2's complient of y
	ADD R3 , R1 , R3	;x-y
	STI R3, X_Y		;store result x-y


;ABS X
	ADD R4, R1, #0
	BRzp ABSX
	NOT R4, R4		;did the 
	ADD R4, R4, #1		;2's compliment
ABSX	STI R4, ABS_X		;store result abs x
	

;ABS Y
	ADD R5, R2, #0
	BRzp ABSY
	NOT R5, R5		;did the 
	ADD R5, R5, #1		;2's compliment
ABSY	STI R5, ABS_Y		;store result abs y


;IXI or IYI
	NOT R6, R5		;did the 
	ADD R6, R6, #1		;2's complient
	ADD R6, R4, R6		;R6 = IxI or IyI

	BRz STORE
	BRn NEG

	AND R6, R6, #0		;positive part
	ADD R6, R6, #1
	BR STORE

NEG	AND R6, R6 #0		;negative part
	ADD R6, R6 #2
STORE	STI R6, Z		;Zero part



	HALT
X	.FILL X3120
Y 	.FILL X3121
X_Y	.FILL X3122
ABS_X	.FILL X3123
ABS_Y	.FILL X3124
Z	.FILL X3125
	.END