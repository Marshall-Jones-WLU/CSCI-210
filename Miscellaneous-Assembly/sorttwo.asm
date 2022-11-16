;;
;; Author: Simon D. Levy
;; File: multiply.asm

;; This program compares the numbers stored in variables SMALLER
;; and LARGER and swaps them if necessary.

	    .ORIG x3000

;; Pseudocode design:

; if smaller > larger:
;    tmp = smaller
;    smaller = larger
;    larger = tmp

;; Main program register usage:
; R0 = smaller
; R1 = larger
; R2 = -smaller
; R3 = larger - smaller

;; Main program code
	LD  R0, SMALLER	    ; R0 <-- SMALLER
	LD  R1, LARGER      ; R1 <-- LARGER
    NOT R2, R0          ; R2 <-- -SMALLER
    ADD R2, R2, #1      ; 
    ADD R3, R1, R2      ; R3 <-- LARGER - SMALLER
    BRzp DONE           ; If R3 >= 0, goto DONE
    ST  R1, SMALLER     ; swap
    ST  R0, LARGER      
DONE    HALT           

; Data for main program
SMALLER .FILL 7
LARGER  .FILL 4

        .END
