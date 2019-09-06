/*
 * warunek.cpp
 */

#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
	int a, b, c;
    int x = 0;
    cout << "Podaj pierwszą liczbę: ";
    cin >> a;
    cout << "Podaj drugą liczbę: ";
    cin >> b;
    cout << "Podaj trzecią liczbę: ";
    cin >> c;
    
    cout << a << " " << b << " " << c << endl;
    if(a > b && a > c){
        x = a;
    }
    else if(b > a && b > c){
        x = b;
    }
    else if(c > a && c > b){
        x = c;
    }
    cout << "Największa liczba: " << x;
    
    
	return 0;
}

