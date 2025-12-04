#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    FILE *fptr = fopen("input.txt", "r");
    
    char buff[102];
    int largest;
    int i_largest;
    int second_largest;
    int i_second_largest;
    int total = 0;


    

    while (fgets(buff, 102, fptr)) {
        largest = 0;
        i_largest = 0;
        second_largest = 0;
        i_second_largest = 0;

        for (int i = 0; i < 100; i++) {
          int d = buff[i]-'0';
          if (d>largest) {
            largest = d;
            i_largest = i;
          }
        }

        for (int i = i_largest+1; i < 99; i++) {
          int d = buff[i]-'0';
          if (d>second_largest) {
            second_largest = d;
            i_second_largest = i;
          }
        }

        char buffer[2];  
        sprintf(buffer, "%d%d", largest, second_largest);
        total += atoi(buffer);

    }
    
    printf("%d", total);
    fclose(fptr);
    return 0;
}