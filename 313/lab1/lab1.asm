;Class: CSE 313 Machine Orginization Lab
;Instructor: Taline Georgiou
;Term: Spring 2013
;NAme(s): Raul Diaz
;lab#1: ALU Operations
;Description: We computed the sum X+Y, XANDY,
;XORY, NOTX, NOTY, X+3, Y-3, and also displayed
;a 0 if X is even and a 1 if X is odd. We also
;stored our results in location x3102 and up 
;because the values of x and y are located
;at x3100 & x3101 where we used load functions
;to get those values

	.ORIG	X3000
	LEA R2, xFF

;X + Y
	LDR R1, R2, #0		;LOADS X
	LDR R3, R2, #1		;LOADS Y
	ADD R4, R1, R3		;R4<=R1+R3
	STR R4, R2, #2		;STORES

;X AND Y
	AND R4, R1, R3		;R4<=R1 AND R3
	STR R4, R2, #3		;STORES

;X OR Y
	NOT R5, R1		;R5<= NOT X
	NOT R6, R3		;R6<= NOT Y
	AND R4, R5, R6		;R4<= NOT(X) AND NOT(Y)
	NOT R4, R4		;R4<= X OR Y
	STR R4, R2, #4		;STORES

;NOT X
	NOT R4, R1		;R4<=NOT X
	STR R4, R2, #5		;STORES
;NOT Y
	NOT R4, R3		;R4<=NOT Y
	STR R4, R2, #6		;STORES
;X + 3
	ADD R4, R1, #3		;R4<= X + 3
	STR R4, R2, #7		;STORES
;Y - 3
	ADD R4, R3, #-3		;R4<= Y - 3
	STR R4, R2, #8		;STORES
;X EVEN OR ODD
	AND R4, R1, X0001	;IF EVEN ITS 0, IF ODD ITS 1 
	STR R4, R2, #9		;STORES
	HALT
	.END