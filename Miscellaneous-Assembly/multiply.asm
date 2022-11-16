;;
;; Author: Simon D. Levy
;; File: multiply.asm

;; This program computes the product of numbers stored in variables FIRST
;; and SECOND and stores the result in the variable PRODUCT

	    .ORIG x3000

;; Pseudocode design:

; product = first * second

;; Main program register usage:
; R1 = first, then location of product
; R2 = second
; R0 = product

;; Main program code
	    LD	R1, FIRST   ; R1 <-- FIRST
	    LD  R2, SECOND  ; R2 <-- SECOND
        AND R0, R0, #0      ; R0 <-- 0
LOOP    ADD R0, R0, R2      ; R0 <-- R0 + R2
        ADD R1, R1, #-1     ; R1 <-- R1-1
        BRz DONE            ; If R1 is negative, we're done
        JSR LOOP            ; Continue looping
DONE    ST R0, PRODUCT      ; PRODUCT <- R0
        HALT                ; halt

; Output of main program
PRODUCT .BLKW 1

; Data for main program: sum should be 1+3+5+7+9 = 25
FIRST   .FILL 3
SECOND  .FILL 5

        .END
