/*
 * wej-wyj.cpp
 */

#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    const int rozmiar = 25;
    char a[rozmiar];
    char b[rozmiar];
	cout << "Podaj imię: ";
    cin.getline(a, rozmiar);
	cout << "Podaj nazwisko: ";
    cin.getline(b, rozmiar);
    
    cout << endl << "WITAJ: " << a << " " << b;
    
	return 0;
}

