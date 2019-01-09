/*
 * Banasiak_alg1.cpp
 */

#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
    int a;
    cout << "Podaj a: ";
    cin >> a;
    if(a > 0 and a < 100) continue;
    int i = 2;
    while(a != i and i <= 100)
    {
        i = i + 2;
        cout << "a to liczba nieparzysta" << endl;
    }
    
    return 0;
}

