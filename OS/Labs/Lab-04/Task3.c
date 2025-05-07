#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/wait.h>
#include<sys/types.h>

void printID(){
  uid_t uid = getuid();
  printf("User ID: %d\n", uid);
}

int main(){
    pid_t pid = getpid();
    pid_t ppid = getppid();

    printf("Current Process ID: %d\n", pid);
    printf("Parent Process ID: %d\n", ppid);
    
    printID();
    
    return 0;
}
