#include <bits/stdc++.h>

using namespace std;
int main()
{    
    int x = 0, y = 0, z = 0 ;
    int forces;
    int a,b,c;
    cin >> forces;
    for (int i=1 ; i <= forces ; i++)
    {
        cin >> a >> b >> c;
        
        x += a; y+=b; z +=c  ; 
        cout << x << ":" << y <<":" << z << endl;
    }
    if (x == 0 && y == 0 && z == 0)
    {
        cout << "YES";
    }
    else 
        cout << "NO";
    return 0;
    
}

