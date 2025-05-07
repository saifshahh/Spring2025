## TASK 15

```c
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <string.h>

#define BUFFER_SIZE 1024
#define NEW_CONTENT "Processed by child process\n"

int main() {
    int fd;
    char buffer[BUFFER_SIZE];
    ssize_t bytesRead;

    // Open input.txt for reading and writing
    fd = open("input.txt", O_RDWR);
    if (fd == -1) {
        perror("open");
        exit(EXIT_FAILURE);
    }

    // Read contents of the file into the buffer
    bytesRead = read(fd, buffer, BUFFER_SIZE - 1);
    if (bytesRead == -1) {
        perror("read");
        close(fd);
        exit(EXIT_FAILURE);
    }
    buffer[bytesRead] = '\0'; // Null-terminate the buffer
    printf("Original File Content:\n%s\n", buffer);

    // Create child process
    pid_t pid = fork();

    if (pid == -1) {
        perror("fork");
        close(fd);
        exit(EXIT_FAILURE);
    }

    if (pid == 0) { // Child Process
        // Modify file contents by writing new content using buffer
        strcpy(buffer, NEW_CONTENT); // Store new content in buffer
        lseek(fd, 0, SEEK_END); // Move file pointer to the end
        if (write(fd, buffer, strlen(buffer)) == -1) {
            perror("write");
            close(fd);
            exit(EXIT_FAILURE);
        }
        close(fd);

        // Replace child process with cat command to display modified content
        execlp("cat", "cat", "input.txt", NULL);
        perror("execlp");
        exit(EXIT_FAILURE);
    } else { // Parent Process
        // Wait for child process to complete
        wait(NULL);
        printf("Parent process completed.\n");
        close(fd);
    }

    return 0;
}
```

