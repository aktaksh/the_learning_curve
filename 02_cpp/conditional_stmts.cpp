#include <iostream>
#include <math.h>

using namespace std;

// int main() {
//     int a = 10, b = 20, c = 100;
//     if (a < b)
//         {
//             c++;
//             cout << c << endl;

//         }
//     if ( a > b)
//         {
//           cout << "a > b" << endl;
//         }

//         else 
//         cout << "a = b" << "equal value" << endl;

//     return 0;
// }



// int main() {
//     int a = 14, b = 13;
//         switch (a == b) // exit value will be give to case statement.
//         {
//             case 0: 
//                 cout << "a = 5" << endl;
//                 break;
//             case 1:  //this is reading the exit value
//                 cout << "a = 10" << endl;
//                 break;
//             case 15: 
//                 cout << "a = 15" << endl;
//                 break;
//             default:
//                 cout << "a is bigger than 5, 10 , 15" << endl;
//         }
//         return 0;

// }


int main()
    {
        
        for (int a = 1 ; a < 10 ; a++ )
            if ( a == 1 )
                {
                                        continue; // this take us back to the loop and exclude further lines of code

                    cout << "This a is 1" << endl;
                }

            else if (a == 4)
                { 
                    cout << " A is four" << endl;
                    break; 

                }
            else 
                {
                    cout << a << endl;
                }
    }


    // -->  Do while goto nested for
    //ascii bitwise
