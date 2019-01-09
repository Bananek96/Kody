/*
 * Banasiak_alg1.cpp
 */

#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int a = 0;
    while (a <= 0 || a >= 100)
    {
        cout << "Podaj a: ";
        cin >> a;
    }
    int i = 2;
    
    for (int j = 1; j != 100; j++)
    {
        if (a == i)
        {
            cout << "a jest liczbą parzystą";
            break;
        }
        else
        {
            i = i + 2;
            if (i == 100)
            {
                cout << "a nie jest liczbą parzystą";
                break;
            }
        }
    }
    return 0;
}

