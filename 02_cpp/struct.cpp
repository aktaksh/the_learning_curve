// #include <iostream>
// #include <string>
#include <bits/stdc++.h>

using namespace std ;

struct inventory { // struct is used to make datatype, inventory is userdefined dtype here
        int hostnum = 1000;
        string procname = "xeon";
        int ram =  256;
};

int main() {
    inventory desktop; // desktop is var name here
    desktop.hostnum = 1000999;
    desktop.ram = 512;
    
    cout << desktop.hostnum  << " ---  " << desktop.ram  << " ---  "  << desktop.procname << endl;
    return 0;
};




