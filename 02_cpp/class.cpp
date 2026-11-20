#include <iostream>
#include <string>
using namespace std ;

class fruits {  // class will not accept arguments as its not a function
    public :
        int fruitno = 0;
        string hname;
        
    void fruitcolor (int x) {
            if (x == 5)
                        cout << "green" << endl;
            else 
                        cout << "red" << endl;


    }


};

int main () {
    fruits apple;
    apple.fruitno = 23;
    apple.hname = "seb";

    cout << apple.fruitno << endl << apple.hname << endl;
    apple.fruitcolor(5);
    return 0;

}