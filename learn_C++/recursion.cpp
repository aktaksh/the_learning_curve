// #include <iostream>
// #include <math.h>

// using namespace std;

// int recurse(int x)
// {
//     // base condition
//     if (x == 1)
//         {
//             return 1;
//         }
    
//     x *= recurse(x-1);  // x = 6 ; x = 6*5
//     cout << "iteration "<< x << endl; 

//     cout << "output "<< x << endl; 

//     return x;

// }

// int main()
// {

//     int x;
//     cout << "Input for factorial:" << endl;
//     cin >> x ;
//     cout << recurse(x) << endl;
//     return 0;

    
// }


#include <iostream>
using namespace std;

int main() {
    int arr[5] ;  // Empty array values defaults to ZERO
    for(int i = 0; i < 5; i++)
        cout << arr[i] << " ";
    return 0;
}

// array is called by call by reference