# Task 3
INCLUDE irvine32.inc

.data
    arr BYTE 61h, 43h, 11h, 52h, 25h  
    sorted BYTE 5 DUP(?)      

.code
main PROC
    mov al, [arr+2]
    mov [sorted], al
    call writehex
    call crlf

    mov al, [arr+4]
    mov [sorted+1], al
    call writehex
    call crlf

    mov al, [arr+1]
    mov [sorted+2], al
    call writehex
    call crlf

    mov al, [arr+3]
    mov [sorted+3], al
    call writehex
    call crlf

    mov al, [arr]
    mov [sorted+4], al
    call writehex
    call crlf

    exit
main ENDP
END main
