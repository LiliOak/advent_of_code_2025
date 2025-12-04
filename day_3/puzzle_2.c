#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>


int main() {
    FILE *fptr = fopen("input.txt", "r");
    
    char buff[102];
    int joltage[12];
    int last_joltage;
    long long int total = 0;
    long long int number;

    

    while (fgets(buff, 102, fptr)) {
        for (int i = 0; i < 12; i++) joltage[i] = 0;
        last_joltage = -1;

        for (int i = 0; i < 12; i++) {
            for (int b = last_joltage+1; b<100-(11-i); b++) {
                int d = buff[b]-'0';
                if (d>joltage[i]) {
                    joltage[i] = d;
                    last_joltage = b;
                }
            }

        }

        
        number = 0;

        for (int i = 0; i < 12; i++) {
            number *= 10;
            number += joltage[i];
        }


        total += number;

        
    
    }

    
    printf("%lld", total);
    fclose(fptr);
    return 0;
}