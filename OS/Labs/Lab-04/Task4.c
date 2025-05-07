#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>

int main() {
    int input, output;
    ssize_t bytes_read, bytes_written;
    char buffer[1024];

    input = open("input.txt", O_RDONLY);
    if (input == -1) {
        perror("Error opening input file");
        exit(1);
    }

    output = open("output.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (output == -1) {
        perror("Error opening output file");
        close(input);  // Close input file before exiting
        exit(1);
    }

    while ((bytes_read = read(input, buffer, 1024)) > 0) {
        bytes_written = write(output, buffer, bytes_read);
        if (bytes_written != bytes_read) {
            perror("Error writing to output file");
            close(input);
            close(output);
            exit(1);
        }
    }

    if (bytes_read == -1) {
        perror("Error reading from input file");
    }

    close(input);
    close(output);

    printf("File copied successful!\n");

    return 0;
}
