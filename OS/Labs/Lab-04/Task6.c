#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/wait.h>
#include<sys/types.h>
#include<signal.h>

void handle_alarm(int signum) {
    printf("\nAlarm received!\n");
    exit(0);
}

int main(){
    int i = 1;
    signal(SIGALRM,handle_alarm);
    alarm(5);
    
    while (1){
        printf("%d second passed...\n",i);
        i += 1;
        sleep(1);
    }
    
    return 0;
}
