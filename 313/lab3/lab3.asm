 ;Class:CSE 313 Machine Organization Lab
;Instructor: Taline Georgiou
;Term: Spring 2013
;Name(s): Raul Diaz 
;Lab#3: "Days of the Week"
;Description: Well this program was a bit more basic.
;what it does is displays a certain day when you enter
;a certain number from 0 to 6 which each one has a certain
;day assigned to it, and when the number entered is not 
;from 0 to 6 it displays "invalid Number". The program also
;runs in a loop that keeps asking you to input a number and
;it terminates until an invalid number is entered.



	.ORIG X3000
RESTART	LEA R0, PROMPT
	PUTS
	GETC
	ADD R3 , R0 , x0    ; Copy R0 into R3
	ADD R3 , R3 , #-16  ; Subtract 48 , the ASCII value of 0
	ADD R3 , R3 , #-16
 	ADD R3 , R3 , #-16  ; R3 now contains the actual value
	ADD R4, R3, #-6
	BRp INVALID
	LEA R0, DAYS
	ADD R3, R3, x0      ;CONDITIONAL CHECK
LOOP	BRz DISPLAY
	ADD R0, R0, #10
	ADD R3, R3, #-1
	BR LOOP		    ;loops until # inputed is not in range

DISPLAY	PUTS

	LEA R0, LF	;new line
	PUTS

	BR RESTART

INVALID	HALT

PROMPT	.STRINGZ "PLEASE ENTER NUMBER: "   ;input number

DAYS	.STRINGZ "Sunday   "		    ;outputs certain day
	.STRINGZ "Monday   "
	.STRINGZ "Tuesday  "
	.STRINGZ "Wednesday"
	.STRINGZ "Thursday "
	.STRINGZ "Friday   "
	.STRINGZ "Saturday "
	.STRINGZ "INVALID INPUT"
LF	.FILL x000A
	.END