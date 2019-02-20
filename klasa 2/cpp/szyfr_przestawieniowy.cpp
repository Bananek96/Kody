/*
 * szyfr_cezara.cpp
 */

#include <iostream>
#include <string.h>

using namespace std;

#define MAKS 100

void deszyfruj(char tb[], int k)
{
    ;
}

void szyfruj(char tb[], int k)
{
    for(int i = 0; i < ilosc; i++)
    {
        kod = (int)tekst[i] + klucz;
        kod = (int)tekst[i];
        if (tekst[i] == ' ')
            kod -= klucz;
        else if(kod > 122)
            kod -= 26;
        else if (kod < 91)
        {
            kod += klucz;
            if (kod > 90) kod -= 26;
        } 
        else 
        {
            kod += klucz;
            if (kod > 122) kod =-26;
        }

        tekst[i] = char(kod);
        cout << tekst[i];
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
