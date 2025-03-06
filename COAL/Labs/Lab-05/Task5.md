```
INCLUDE irvine32.inc

.data
    array1 BYTE 10h, 20h, 30h, 40h   
    array2 BYTE 4 DUP(?)

.code
main PROC
  
    mov esi, OFFSET array1      
    add esi, 3                   
    mov edi, OFFSET array2       

   
    mov al, [esi]               
    mov [edi], al               
    call writehex
    call crlf
    dec esi                      
    inc edi                      

  
    mov al, [esi]              
    mov [edi], al               
    call writehex
    call crlf
    dec esi
    inc edi

    mov al, [esi]                
    mov [edi], al              
    call writehex
    call crlf
    dec esi
    inc edi

   
    mov al, [esi]              
    mov [edi], al               
    call writehex
    call crlf

    exit
main ENDP
END main
```
