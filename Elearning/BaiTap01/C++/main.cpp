#include <iostream>
#include "Bai05.h"
using namespace std;

int main(){
    int a;

    cout<<"Nhap so: ";
    cin>> a;

    if(SoNguyenTo(a)){
        cout<<"La so nguyen to"<<endl;
    }
    else{
        cout<<"Khon la so nguyen to"<<endl;
    }
    return 0;
}