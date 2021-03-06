;Class:CSE 313 Machine Organization Lab
;Instructor: Taline Georgiou
;Term: Spring 2013
;Name(s): Raul Diaz
;Lab#7: COMPUTE DAY OF THE WEEK
;Description: in this lab we wrote an LC-3 program that
;given the day, month, and year will return the day of 
;the week. i did this by doing many JMP routines and by
;following the concept of zellers formula, which is
;f= k + (13m-1)/5 + D + D/4 + C/4 - 2C
;at the end the result has to end in a number between
;0 and 6, 0 being sunday and 6 being saturday. 


	.ORIG X3000

	JSR MONTH		;SUBROUTINE TO GET m
	STI R4, M		;STORES VALUE IN R4 TO M

	JSR MULT		;MULTIPLICATION SUBROUTINE
	STI R3, NEWM		;STORES VALUE IN R3 TO NEWM

	JSR DIV1		;DIVISION SUBROUTINE
	STI R5, QUOTOFM		;QUOTIENT OF NEWM
	STI R3, R		;REMAINDER

	JSR DIV2		;DIVISION SUBROUTINE
	STI R5, QUOTOFD		;QUOTIENT OF D, FIRST 2 #S OF YEAR
	STI R3, R		;REMAINDER

	JSR DIV3		;DIVISION SUBROUTINE
	STI R5, QUOTOFC		;QUOTIENT OF C, CENTURY, LAST 2 #S OF YR
	STI R3, R		;REMAINDER

	JSR ZELLERS		;SUBROUTINE TO GET f
	STI R6, F		;STORES VALUE IN R6 TO F

	JSR MODULEF		;SUBROUTINE TO GET THE MODULE F%7
	STI R5, MODF		;STORES VALUE IN R5 TO MODF
	STI R3, R		;STORES VALUE IN R3 TO R

	LDI R0, R		;LOADS VALUE OF R INTO R0

	AND R3, R3, #0		;CLEAR R3
	ADD R3, R0 , x0		;Copy R0 into R3
	AND R4, R4, #0		;CLEARS R4
	ADD R4, R3, #-6		;SUBTRACTS 6 TO GET NUMBER OF THE DAY OF THE WEEK
	BRp INVALID
	LEA R0, DAYS
	ADD R3, R3, x0		;CONDITIONAL CHECK
DLOOP	BRz DISPLAY
	ADD R0, R0, #10
	ADD R3, R3, #-1
	BR DLOOP		;loops until # inputed is not in range

DISPLAY	PUTS

	;LEA R0, LF	;new line


INVALID	HALT

DAYS	.STRINGZ "Sunday   "		    ;outputs certain day
	.STRINGZ "Monday   "
	.STRINGZ "Tuesday  "
	.STRINGZ "Wednesday"
	.STRINGZ "Thursday "
	.STRINGZ "Friday   "
	.STRINGZ "Saturday "
;LF	.FILL x000A





X	.FILL X31F0
K	.FILL X31F1
C	.FILL X31F2
D	.FILL X31F3

M	.FILL X31F5
NEWM	.FILL X31F6
QUOTOFM	.FILL X3103
QUOTOFD	.FILL X3104
QUOTOFC	.FILL X3105
F	.FILL X3106
MODF	.FILL X3107
R	.FILL X31F4





MONTH
	LDI R1, X		;PUT ORIGINAL MONTH,x, IN R1
	ADD R4, R1, #0		;PUT THE MONTH INTO R4
	ADD R4, R4 #-2		;GET NEW MONTH, M
	BRnz GETM		;IF X > 2 SUBTRACT 2
	RET			;BACK TO CALLING PROGRAM
GETM	ADD R4, R4, #12		;ELSE ADD 10 TO x
	RET			;BACK TO CALLING PROGRAM





MULT	
	ST R5, SaveReg5		;SAVE R5
	ST R6, SaveReg6		;SAVE R6

	LDI R4, M		;GET VALUE THATS IN M
	NOT R4, R4		;INVERTED IT
	ADD R4, R4, #1		;2S COMPLIMENT
	
LOOP	ADD R6, R5, R4		;CHECKS IF m>0 IF YES QUIT
	BRzp QUIT1		;ELSE KEEP GOING
	ADD R5, R5, #1		;COUNTER
	ADD R3, R3, #13		;IS MULTIPLIYING 13 UNTIL COUNTER MAKES R6 HIT 0
	BR  LOOP		;BACK TO LOOP
QUIT1	ADD R3, R3, #-1		;(13M-1) PART OF ZELLERS FORMULA
	RET			;BACK TO CALLING PROGRAM

	LD R5, SaveReg5		;RESTORE R5
	LD R6, SaveReg6		;RESTORE R6
	RET			;BACK TO CALLING PROGRAM
SaveReg5   .FILL X0
SaveReg6   .FILL X0





DIV1
	LDI R0, NEWM		;LOAD VALUE OF NEWM IN R0
	AND R1, R1, #0		;CLEARS R1
	ADD R1, R1, #5		;PUTS 5 IN R1

	ADD R0, R0, #0		;CHECKS IF NEWM IS 0
	BRz QUIT2		;IF YES QUIT ELSE CONTINUE
	ADD R3, R0, #0		;NEWM INTO R3
	ADD R4, R1, #0		;5 INTO R4
	NOT R4, R4		;INVERT
	ADD R4, R4, #1		;2S COMPLIMENT
	AND R5, R5, #0		;CLEAR R5

LOOP2	ADD R5, R5, #1		;COUNTER
	ADD R3, R3, R4		;SUBTRACT NEWM BY -5
	BRp LOOP2		;IF POS GO BACK TO LOOP3
	BRz QUIT2		;IF 0 GO TO QUIT3
	ADD R3, R3, R1		;IF NEG ADD THE RESULT + 5
	ADD R5, R5, #-1		;IF NEG ADD TO THE COUNTER - 1
QUIT2	RET			;BACK TO CALLING PROGRAM





DIV2
	LDI R0, D		;LOAD VALUE OF D, LAST 2 DIGITS OF YEAR, IN R0
	AND R1, R1, #0		;CLEARS R1
	ADD R1, R1, #4		;PUTS 4 IN R1

	
	ADD R0, R0, #0		;CHECKS IF D IS 0
	BRz QUIT3		;IF ZERO QUIT ELSE CONTINUE
	ADD R3, R0, #0		;D INTO R3
	ADD R4, R1, #0		;4 INTO R4
	NOT R4, R4		;INVERT
	ADD R4, R4, #1		;2S COMPLIMENT
	AND R5, R5, #0		;CLEAR R5

LOOP3	ADD R5, R5, #1		;COUNTER
	ADD R3, R3, R4		;SUBTRACT D BY -4
	BRp LOOP3		;IF POS GO BACK TO LOOP3
	BRz QUIT3		;IF 0 GO TO QUIT3
	ADD R3, R3, R1		;IF NEG ADD THE RESULT + 4
	ADD R5, R5, #-1		;IF NEG ADD TO THE COUNTER - 1
QUIT3	RET			;BACK TO CALLING PROGRAM





DIV3
	LDI R0, C		;LOAD C, CENTURY OF YEAR, IN R0
	AND R1, R1, #0		;CLEARS R1
	ADD R1, R1, #4		;PUTS 4 IN R1

	
	ADD R0, R0, #0		;CHECKS IF C IS 0
	BRz QUIT4		;IF ZERO QUIT ELSE CONTINUE
	ADD R3, R0, #0		;NEWM INTO R3
	ADD R4, R1, #0		;4 INTO R4
	NOT R4, R4		;INVERT
	ADD R4, R4, #1		;2S COMPLIMENT
	AND R5, R5, #0		;CLEAR R5

LOOP4	ADD R5, R5, #1		;COUNTER
	ADD R3, R3, R4		;SUBTRACT C BY -4
	BRp LOOP4		;IF POS GO BACK TO LOOP3
	BRz QUIT4		;IF 0 GO TO QUIT3
	ADD R3, R3, R1		;IF NEG ADD THE RESULT + 4
	ADD R5, R5, #-1		;IF NEG ADD THE COUNTER + 1
QUIT4	RET			;BACK TO CALLING PROGRAM


ZELLERS
	LDI R0, K		;LOAD VALUE OF K, THE DAY ,IN R0
	LDI R1, QUOTOFM		;LOAD VALUE OF (13M-1)/5, IN R1
	LDI R2, D		;LOAD VALUE OF D, LAST 2 #s OF YR, IN R2
	LDI R3, QUOTOFD		;LOAD VALUE OF D/4, IN R3
	LDI R4, QUOTOFC		;LOAD VALUE OF C/4, IN R4
	LDI R5, C		;LOAD VALUE OF C IN R5

	ADD R5, R5, R5		;THIS DOES THE 2(C) PART
	NOT R5, R5		;IN ZELLERS FORMULA
	ADD R5, R5, #1		

	ADD R6, R0, R1		;THIS PARTS ADD EVERYTHING
	ADD R6, R6, R2		;AFTER DOING THE MULTIPLICATION
	ADD R6, R6, R3		;AND DIVISION PARTS, SO THIS
	ADD R6, R6, R4		;GIVES YOU THE FINAL SUM
	ADD R6, R6, R5		;WHICH IS f
	RET

MODULEF

	LDI R0, F		;LOAD F IN R0
	AND R1, R1, #0		;CLEARS R1
	ADD R1, R1, #7		;PUTS 7 IN R1

	
	ADD R0, R0, #0		;CHECKS IF F IS 0
	BRz QUIT5		;IF ZERO QUIT
	
	BRn NEGF		;IF NEG GO TO NEGF, ELSE CONTINUE

	ADD R3, R0, #0		;F INTO R3
	ADD R4, R1, #0		;7 INTO R4
	NOT R4, R4		;INVERT
	ADD R4, R4, #1		;2S COMPLIMENT
	AND R5, R5, #0		;CLEAR R5

LOOP5	ADD R5, R5, #1		;COUNTER
	ADD R3, R3, R4		;SUBTRACT F BY -7
	BRp LOOP5		;IF POS GO BACK TO LOOP5
	BRz QUIT5		;IF 0 GO TO QUIT3
	ADD R3, R3, R1		;IF NEG ADD THE RESULT + 7
	ADD R5, R5, #-1		;IF NEG ADD THE COUNTER + 1
QUIT5	RET			;BACK TO CALLING PROGRAM



NEGF
	ADD R3, R0, #0		;F INTO R3
	NOT R3, R3		;INVERT
	ADD R3, R3, #1		;2S COMPLIMENT
	ADD R4, R1, #0		;7 INTO R4
	NOT R4, R4		;INVERT
	ADD R4, R4, #1		;2S COMPLIMENT
	AND R5, R5, #0		;CLEAR R5

LOOP6	ADD R5, R5, #1		;COUNTER
	ADD R3, R3, R4		;SUBTRACT F BY 7
	BRp LOOP6		;IF POS GO BACK TO LOOP6
	BRz QUIT6		;IF 0 GO TO QUIT6
	NOT R3, R3		;IF NEG MAKE F POS
	ADD R3, R3, #1		;BY 2S COMPLIMENT
	ADD R5, R5, #-1		;IF IT WAS NEG ADD THE COUNTER + 1
QUIT6	RET			;BACK TO CALLING PROGRAM


.END	