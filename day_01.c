#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define abs(x) ((x)>=0?(x):-(x))
#define LEN 1024


enum direction { N, S, E, W };

int solve_part_1() {
    FILE *fp;

    char buffer[LEN];

    fp = fopen("../input_01.txt", "r");
    char *sp;
    char v[3] = ", ";
    int position[3] = {0, 0, 0}; // row, col, direction
    
    if (fp == NULL) {
        printf("Error while opening file.\n");
        exit(0);
    }

    while (fgets(buffer, LEN, fp) != NULL) {

        sp = strtok(buffer, v);
        int dir, step;
        
        while (sp) {
            dir = position[2];
            step = atoi(sp+1);
            
            if (dir == 0) {                 // heading north
                if (sp[0] == 'R') {                 // turn right -> eastward
                    position[1] += step;
                    position[2] = 2;
                } else {                            // turn left -> westward
                    position[1] -= step;
                    position[2] = 3;
                }
            }
            
            if (dir == 1) {                    // heading south
                if (sp[0] == 'L') {                    // turn left -> eastward
                    position[1] += step;
                    position[2] = 2;
                } else {                               // turn right -> westward
                    position[1] -= step;
                    position[2] = 3;
                }
            }

            if (dir == 2) {                    // heading east
                if (sp[0] == 'R') {                    // turn righ -> south
                    position[0] += step;
                    position[2] = 1;
                } else {                               // turn left -> north
                    position[0] -= step;
                    position[2] = 0;
                }
            }

            if (dir == 3) {                    // heading west
                if (sp[0] == 'L') {                    // turn left -> south
                    position[0] += step;
                    position[2] = 1;
                } else {                               // turn right -> north
                    position[0] -= step;
                    position[2] = 0;
                }
            }
            sp = strtok(NULL, v);
        }
    }

    fclose(fp);
    return abs(position[0]) + abs(position[1]);
}




int main() {

    printf("Solution part 1: %d", solve_part_1());
    return 0;

}