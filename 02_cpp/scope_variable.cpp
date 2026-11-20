#include <iostream>
#include <string>

using namespace std;
const int z = 809;
// z = 88;  // global variable scopewise

int funcx(int a,int &x)  
{
    cout << a << endl << z  << endl << x;
    cout << &a << endl << &z  << endl << &x << endl;

}

int main()

{
    int x = 99;  // local var scope
    funcx(x,x);  // to pass arguments to function
    return 0;

}