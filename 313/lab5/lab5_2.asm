;Class:CSE 313 Machine Organization Lab
;Instructor: Taline Georgiou
;Term: Spring 2013
;Name(s): Raul Diaz
;Lab#5: Subroutines: Multiplication, Division, Modules
;Description: in this program we input an x and y to get the
;product of them and storing it in location x3103. the input
;value of x and y are stored in locations x3101 and x3102
;i took the 2s compliment of y and made it a counter and so the
;program multiplied by x, itself, until the counter hit zero, 
;which y was the counter.the other part of this program was 
;division. we divided x and y and stored the quotient and remainder
;in the locations x3104 and x3105. for this there was a branch where
;if y was zero then jump to the end and quit.

	.ORIG X3000
	LDI R1, X		;X IS IN R1
	LDI R2, Y		;Y IS IN R2

	JSR MULT		;MULTIPLICATION SUBROUTINE
	STI R3, XY		;PRODUCT XY IS IN R3
	JSR DIV			;DIVISION SUBROUTINE
	STI R5, QUOT		;QUOTIENT NUMBER
	STI R3, R		;REMAINDER
	HALT

X	.FILL X3100
Y	.FILL X3101
XY	.FILL X3102
QUOT	.FILL X3103
R	.FILL X3104

MULT	
	ST R5, SaveReg5		;SAVE R5
	ST R6, SaveReg6		;SAVE R6

	ADD R4, R2, #0		;PUT THE VALUE OF Y INTO R4
	NOT R4, R4		;INVERTED IT
	ADD R4, R4, #1		;2S COMPLIMENT
	BRp POSLOOP		;FOR NEGATIVE VALUES THAT BECOME POS	
				;SO NEED A NEGATIVE COUNTER INSTEAD

LOOP	ADD R6, R5, R4		;CHECKS IF N>0 IF YES QUIT
	BRzp QUIT1		;ELSE KEEP GOING
	ADD R5, R5, #1		;COUNTER
	ADD R3, R3, R1		;IS MULTIPLIYING UNTIL COUNTER HITS 0
	BR  LOOP		;BACK TO LOOP
QUIT1	RET			;BACK TO CALLING PROGRAM


POSLOOP	ADD R4, R4, #0		;THIS LOOP DOES
LOOP2	ADD R6, R5, R4		;THE SAME AS THE TOP ONE
	BRz QUIT2		;BUT MAKES THE VALUE AT
	ADD R5, R5, #1		;THE END NEGATIVE BECAUSE
	ADD R3, R3, R1		;IT HAD A NEGATIVE VALUE IN
	BR  LOOP2		;Y, SO THE RESULT MUST END 
QUIT2	NOT R3, R3		;IN NEGATIVE AFTER THEY MULTIPLY
	ADD R3, R3, #1

	LD R5, SaveReg5		;RESTORE R5
	LD R6, SaveReg6		;RESTORE R6
	RET			;BACK TO CALLING PROGRAM
SaveReg5   .FILL X0
SaveReg6   .FILL X0


DIV
	ADD R2, R2, #0		;CHECKS IF Y IS 0
	BRz QUIT3
	ADD R6, R2, #0		;Y INTO R6
	AND R5, R5, #0		;CLEAR R5
	ADD R3, R1, #0		;X INTO R3
	ADD R4, R2, #0		;Y INTO R4
	NOT R4, R4		;INVERT
	ADD R4, R4, #1		;2S COMPLIMENT
	ADD R0, R3, R4		;SUBTRACT X BY Y
	BRn QUIT2		;CHECKS IF Y>X
LOOP3	ADD R5, R5, #1		;COUNTER
	ADD R3, R3, R4		;SUBTRACT X BY Y
	BRp LOOP3		;IF POS GO BACK TO LOOP3
	BRz QUIT3		;IF 0 GO TO QUIT3
	ADD R3, R3, R6		;IF NEG ADD THE RESULT + Y
	ADD R5, R5, #-1		;IF NEG ADD THE COUNTER + 1
	BR QUIT3
QUIT3	RET			;BACK TO CALLING PROGRAM
.END	