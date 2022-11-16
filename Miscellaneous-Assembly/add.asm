        .ORIG x3000
        
        ; Load values into registers
        LD R1, NUM1
        LD R2, NUM2
        
        ; Add the values into R7
        ADD R7, R1, R2
        
        ; Store the new value in R7 as SUM
        ST R7, SUM
        
        ; reset registers
        AND R1, R1, #0
        AND R2, R2, #0
        AND R7, R7, #0
        
        HALT
    
NUM1    .FILL #2
NUM2    .FILL #3
SUM     .BLKW #1

        .END
