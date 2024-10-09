#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

int plugboard_cable;
char arr_plugboard[27][3]; // 각 플러그보드 값이 문자열(2자리 + 널문자)

int sel_rotors[3]; // 순서대로 몇번째 rotor가 들어가는지 
int idx_rotors[3]; // rotor의 시작 index

// hard-coded rotors
int arr_rotors[5][53] = {
    {-1, 11, 9, 13, 22, 20, 24, 25, 3, 5, 4, 17, 7, 6, 18, 8, 26, 10, 23, 21, 14, 2, 12, 15, 1, 16, 19, 24, 21, 8, 10, 9, 13, 12, 15, 2, 17, 1, 22, 3, 20, 23, 25, 11, 14, 26, 5, 19, 4, 18, 6, 7, 16},
    {-1, 12, 6, 4, 14, 17, 11, 3, 16, 19, 21, 13, 26, 18, 9, 22, 8, 1, 25, 7, 24, 15, 5, 2, 23, 20, 10, 17, 23, 7, 3, 22, 2, 19, 16, 14, 26, 6, 1, 11, 4, 21, 8, 5, 13, 9, 25, 10, 15, 24, 20, 18, 12},
    {-1, 5, 11, 10, 12, 23, 25, 2, 22, 16, 7, 1, 4, 9, 19, 3, 8, 26, 17, 13, 15, 18, 24, 20, 6, 21, 14, 11, 7, 15, 12, 1, 24, 10, 16, 13, 3, 2, 4, 19, 26, 20, 9, 18, 21, 14, 23, 25, 8, 5, 22, 6, 17},
    {-1, 26, 23, 21, 7, 10, 12, 4, 15, 11, 3, 22, 19, 1, 8, 9, 20, 16, 6, 13, 14, 24, 18, 5, 2, 17, 25, 13, 24, 10, 7, 23, 18, 4, 14, 15, 5, 9, 6, 19, 20, 8, 17, 25, 22, 12, 16, 3, 11, 2, 21, 26, 1},
    {-1, 2, 14, 25, 16, 23, 1, 10, 7, 4, 11, 12, 22, 18, 20, 26, 17, 15, 3, 8, 19, 6, 13, 21, 5, 24, 9, 6, 1, 18, 9, 24, 21, 8, 19, 26, 7, 10, 11, 22, 2, 17, 4, 16, 13, 20, 14, 23, 12, 5, 25, 3, 15},
}; 

int arr_reflect[27] = {-1, 9, 15, 12, 8, 26, 25, 24, 4, 1, 17, 19, 3, 22, 23, 2, 20, 10, 21, 11, 16, 18, 13, 14, 7, 6, 5};

void setting_rotors(){
    int sel_idx;

    // select rotors
    sel_rotors[0] = rand() % 5; // select first rotor
    do {
        sel_idx = rand() % 5; 
    } while (sel_idx == sel_rotors[0]);
    sel_rotors[1] = sel_idx;

    do {
        sel_idx = rand() % 5;
    } while (sel_idx == sel_rotors[0] || sel_idx == sel_rotors[1]);
    sel_rotors[2] = sel_idx;

    // select index in rotors
    idx_rotors[0] = (rand() % 26) + 1; 
    idx_rotors[1] = (rand() % 26) + 1;
    idx_rotors[2] = (rand() % 26) + 1;
    
    printf("(Rotors-index)\n\n");
    printf("ex) rotor(n) : version(index)\n");
    printf("rotor(1) : %d(%d) / ", sel_rotors[0], idx_rotors[0]);
    printf("rotor(2) : %d(%d) / ", sel_rotors[1], idx_rotors[1]);
    printf("rotor(3) : %d(%d)\n", sel_rotors[2], idx_rotors[2]);
}

void setting_plugboard(char arr_plugboard[27][3]){
    int plug_idx; 
    int plug_val; 
    char tmp[3];

    // Initialize the plugboard
    for (int i = 0; i < 27; i++) {
        strcpy(arr_plugboard[i], "#");
    }

    plugboard_cable = (rand() % 11) + 1; 

    if (plugboard_cable < 6){
        plugboard_cable = 6;
    }

    for (int i = 1; i < plugboard_cable; i++) {
        while (1) {
            plug_idx = (rand() % 26) + 1;
            if (strcmp(arr_plugboard[plug_idx], "#") == 0) {
                break;
            }
        }

        while (1) {
            plug_val = (rand() % 26) + 1;
            if (plug_idx == plug_val || strcmp(arr_plugboard[plug_val], "#") != 0) {
                continue;
            }

            sprintf(arr_plugboard[plug_idx], "%d", plug_val);
            sprintf(arr_plugboard[plug_val], "%d", plug_idx);
            break;
        }
    }
}

void print_title(){
    printf("[Enigma]\n\n");
}

void print_plugboard(){
    int arr_plugboard_check[27];

    printf("(PlugBoard)\n\n");

    for (int i = 0; i < 27; i++) {
        arr_plugboard_check[i] = -1;
    }

    printf("| ");
    for (int j = 1; j < 27; j++) {
        if (strcmp(arr_plugboard[j], "#") != 0 && arr_plugboard_check[j] == -1) {
            int plug_num = atoi(arr_plugboard[j]);
            printf("%c - %c", (char)(j + 64), (char)(plug_num + 64));
            arr_plugboard_check[j] = 1;
            arr_plugboard_check[plug_num] = 1;
            printf(" | ");
        }
    }
    printf("\n\n\n");
}

int main(void) {
    /*
    """
    1. setting()진행
    - plugboard 셋팅
    - 3개의 rotor 및 index 설정
    - 셋팅한 값들 사전에 화면 출력
    => 여기까지 완료
    2. 사용자의 문자 입력 (최대 200자))
    3. plugboard()
    4. rotors() - 1,2,3 거침
    5. reflector()
    6. rotors_reverse() - 3,2,1거침
    7. plugboard()
    8. 화면 출력
    """
    */

    srand(time(NULL));  // Initialize random seed once

    print_title();
    printf("\n= = = = = = = = = = = =\n\n");

    setting_plugboard(arr_plugboard);
    print_plugboard();

    setting_rotors();

    printf("\n= = = = = = = = = = = =\n\n");

    return 0;
}
