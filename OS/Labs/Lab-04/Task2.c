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
        for (int i = 0; i < 100; i++) {
            printf("I am a child process\n");
        }
    } else {
        for (int i = 0; i < 100; i++) {
            printf("I am a parent process\n");
        }
      }
    return 0;
}
