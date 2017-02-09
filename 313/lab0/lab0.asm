;Class: CSE 313 Machine Orginization Lab
;Instructor: Taline Georgiou
;Term: Spring 2013
;NAme(s): Raul Diaz
;lab#0: Intro to the LC-3 stimulator
;Description: LC-3 Program that displays
;"Hello World!" to the console

	.ORIG		X3000
	LEA		R0, HW		; load address of string
	PUTS				; output string to console
	HALT				; end program
HW	.STRINGZ	"Hello World!"
	.END