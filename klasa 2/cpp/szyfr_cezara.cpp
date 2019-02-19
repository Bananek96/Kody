/*
 * szyfr_cezara.cpp
 */


#include <iostream>

using namespace std;

#define MAKS 100

void deszyfruj(char tb[], int k)
{
    ;
}

void szyfruj(char tb[], int k)
{
    k = k % 26;
    int i = 0;
    int kod = 0;
    while(tb[i] != '\0')
    {
        if(tb[i] = ' ' || tb[i] = 'x' || tb[i] = 'y' || tb[i] = 'z' || tb[i] = 'X' || tb[i] = 'Y' || tb[i] = 'Z')continue;
        kod = (int)tb[i] + k;
        cout << (char)kod;
        i++;
    }
}


int main(int argc, char **argv)
{
    char tekst[MAKS];
	int klucz = 0;

    cout << "Podaj tekst: " << endl;
    cin.getline(tekst, MAKS);

    cout << "Podaj klucz: " << endl;
    cin >> klucz;

    szyfruj(tekst, klucz);
	return 0;
}
