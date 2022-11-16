; Problem 2: sum over list
; Simon D. Levy
;
; Register key:  R0: sum
;                R1: current location in list (address)
;                R2: current value from list
;                R3: loop countdown
;
; ---------------------------------------------------------

          .ORIG x3000

          ; sum = 0
          AND R0, R0, #0

          ; start at head of list
          LEA R1, LIST

          ; start countdown
          LD R3, LEN
          
LOOP      LDR R2, R1, #0  ;load current value from list

          ADD R0, R0, R2  ; add current value to sum

          ADD R1, R1, #1  ; index += 1

          ; decrement the countdown and loop until it's zero
          ADD R3, R3, #-1
          BRp LOOP

          ; store the sum
          ST R0, SUM

          HALT

LIST      .FILL #1
          .FILL #3
          .FILL #5
          .FILL #7
          .FILL #9

LEN       .FILL #5 ; NB: must agree with LIST length

SUM       .BLKW #1

          .END
