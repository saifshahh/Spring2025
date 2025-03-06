```
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
```
We will have to multiply 2 with normal indexing to access word array value and 4 to access dword array value, if the arrays were changed to WORD and DWORD respectively.
## Output:
![image](https://github.com/user-attachments/assets/3a2cc8cc-9034-4c37-b478-c20668b6c0ec)
