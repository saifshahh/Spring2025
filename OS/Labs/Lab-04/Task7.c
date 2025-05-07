#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/wait.h>
#include<sys/types.h>

int main(){
    pid_t a = fork();
    
    if (a < 0) {
        perror("Fork failed");
        exit(1);
    } else if (a == 0) {
        execlp("ls","ls",NULL);
        perror("execlp failed");
        exit(1);
    } else {
        wait(NULL);
        printf("Parent Process: Child has finished execution.\n");
    }
    
    return 0;
}
