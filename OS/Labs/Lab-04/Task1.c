#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t child1, child2;

    child1 = fork();

    if (child1 < 0) {
        perror("Fork failed");
        exit(1);
    } else if (child1 == 0) {

        printf("Child 1: %d\n", getpid());
        exit(0);
    }

    child2 = fork();

    if (child2 < 0) {
        perror("Fork failed");
        exit(1);
    } else if (child2 == 0) {
        printf("Child 2: %d\n", getppid());
        exit(0);
    }

    wait(NULL);
    wait(NULL);
    
    printf("Both child processes has been finished.");

    return 0;
}
