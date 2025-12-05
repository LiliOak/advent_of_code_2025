

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    FILE *fptr = fopen("input.txt", "r");
    char buff[120]; // 120 in file
    int toiletpaper[144]; // 144 in total with buffers added
    int minesweeps[144]; // 144 in total with buffers added
    int sweep_i = 12; //12 per line

    for (int i=0; i<12; i++) {toiletpaper[i]=0;} //start
    while (fgets(buff, 12, fptr)) {
        toiletpaper[sweep_i++] = 0;
        for (int i = 0; i < 10; i++) {
            if (buff[i] == '@') {
                toiletpaper[sweep_i++] = -5;
            } else {
                toiletpaper[sweep_i++] = 0;
            }
        }
        toiletpaper[sweep_i++] = 0;
    }
    for (int i=144-12; i<144; i++) {toiletpaper[i]=0;} //end 

    for (int i=0; i<144; i++) {minesweeps[i]=0;}
    for (int y=0; y<12; y++){
        for (int x=0; x<12; x++){
            if (toiletpaper[y*12+x]){
               minesweeps[y * 12 + x - 1] += 1;
                minesweeps[y * 12 + x + 1] += 1;
                minesweeps[(y - 1) * 12 + x] += 1;
                minesweeps[(y + 1) * 12 + x] += 1;
                minesweeps[(y - 1) * 12 + x - 1] += 1;
                minesweeps[(y - 1) * 12 + x + 1] += 1;
                minesweeps[(y + 1) * 12 + x - 1] += 1;
                minesweeps[(y + 1) * 12 + x + 1] += 1;      
            }
        }
    }

    int total = 0;
    for (int y=1; y<11; y++){
            for (int x=1; x<11; x++){
                if  (minesweeps[(y-1)*12+x]<4 && toiletpaper[(y-1)*12+x]==-5){
                    total++;
                    printf("X"); 
                } else {
                    printf("%d", minesweeps[(y-1)*12+x]);
                }
        }
        printf("\n");
    };

    for (int y=0; y<12; y++){
            for (int x=0; x<12; x++){
                    printf("%d", minesweeps[(y-1)*12+x]);
            }
        printf("\n");
       }

    printf("%d", total);

    fclose(fptr);

}