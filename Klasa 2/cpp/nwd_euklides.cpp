/*
 * nwd_euklides.cpp
 */


#include <iostream>
using namespace std;
 
int main()
{
    int a,b;
        cout << "Podaj a: ";
        cin >> a;
        cout << "Podaj b: ";
        cin >> b;
        cout << "NWD(" << a << " i " << b << ") = ";
    while (a != b)
    {   
        if (a > b)
            a = a - b;
        else
            b = b - a;
    }
    cout << a << endl;
    
    return 0;
}
