#include <iostream>
#include "Bai05.h"

using namespace std;

bool SoNguyenTo(int a){
    if (a < 2){
        return false;
    }
    else{
        for (int  i = 2; i*i <= a ; i++){
            if(a % i == 0){
                return false;
            }
        }
        return true;
    }
}