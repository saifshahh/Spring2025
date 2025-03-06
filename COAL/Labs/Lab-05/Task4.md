```
INCLUDE irvine32.inc

.data
    arrayB Byte 10, 20, 30
    arrayW WORD 150, 250 ,350
    arrayD DWORD 600, 1200, 1800
    sum1 DWORD 0
    sum2 DWORD 0
    sum3 DWORD 0

.code
main PROC

    movzx eax, arrayB[0]
    movzx ebx, arrayW[0]
    add eax, ebx
    add eax, arrayD[0]
    mov sum1, eax
    call writeint
    call crlf

    movzx eax, arrayB[1]
    movzx ebx, arrayW[2]
    add eax, ebx
    add eax, arrayD[4]
    mov sum2, eax
    call writeint
    call crlf

    movzx eax, arrayB[2]
    movzx ebx, arrayW[4]
    add eax, ebx
    add eax, arrayD[8]
    mov sum3, eax
    call writeint
    call crlf

    exit
main ENDP
END main
```

## Output:
![image](https://github.com/user-attachments/assets/498b7c0c-a5c4-4e39-987a-54f36a82fbe2)
