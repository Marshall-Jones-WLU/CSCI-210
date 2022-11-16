;;
;; Author: Simon D. Levy
;; File: subtract.asm

;; This program subtracts the number in the variable SECOND from the number in the variable FIRST 
;; and stores the result in the variable DIFF

	.ORIG x3000

;; Pseudocode design:

; diff = first - second

;; Main program register usage:
;  R1 = first
;  R2 = second
;  R1 = diff

;; Main program code
	LD	R1, FIRST	
	LD  R2, SECOND
	NOT	R2, R2       ; These two lines compute R2= -R2	
	ADD	R2, R2, #1   ;
    ADD     R1, R1, R2
	ST	R1, DIFF	
    HALT

; Data for main program
FIRST	.FILL 5
SECOND	.FILL 3
DIFF	.BLKW 1

	.END
