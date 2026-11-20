#include <bits/stdc++.h>

using namespace std ;

union fruit
{
    int count;
    float sizex;

    
};

int main() {
    fruit samosa;
    samosa.count = 420;
   // cout << samosa.count << endl;
    cout << "memory location: " << &samosa.count << endl ;

    samosa.sizex = 3.999;
    cout << samosa.count << endl << samosa.sizex << endl;
    cout << "memory location: " << &samosa.count << endl << &samosa.sizex ;


    return 0;


};
