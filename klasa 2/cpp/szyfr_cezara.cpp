/*
 * szyfr_cezara.cpp
 */


#include <iostream>
#include <stdio.h>
#include <string.h>

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
        kod = (int)tb[i] + k;
        cout << (char)kod;
        i++;
    }
    
    if (tekst[i] == ' ')
    { 
        kod -= klucz;
    }
    
    else if(kod > 122)
    {
        kod -= 26;
    }
    tekst[i] = char(kod);
    cout << tekst[i];
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
