## MODIFIED

```c
#include <sys/types.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

#define BUFFER_SIZE 25
#define READ_END 0
#define WRITE_END 1

int main() {
    char write_msg[BUFFER_SIZE] = "Greetings!";
    char read_msg[BUFFER_SIZE];
    int fd[2];
    pid_t pid;

    if (pipe(fd) == -1) { 
        fprintf(stderr, "Pipe failed");
        return 1;
    }

    pid = fork();
    if (pid < 0) { 
        fprintf(stderr, "Fork failed");
        return 1;
    }

    pid = fork();

    if (pid > 0) {
        close(fd[READ_END]);
        write(fd[WRITE_END], write_msg, strlen(write_msg) + 1);
        close(fd[WRITE_END]);
    } 
    else { 
        close(fd[WRITE_END]); 
        read(fd[READ_END], read_msg, BUFFER_SIZE); 
        printf("read %s\n", read_msg);
        printf("ID: %d\n",getpid());
        close(fd[READ_END]); 
    }
    
    return 0;
}
```

## OUTPUT:
![Screenshot from 2025-03-05 12-57-04](https://github.com/user-attachments/assets/52e97523-9676-40e0-862e-aeb13888f974)
