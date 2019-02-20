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
    int ile = strlen(tb);
    cout << ile << endl;
    int r = ile % k;

    if (r > 0)
    {
        for(int i = ile; i < ile + k - r; i++)
        {
            tb[i]= '.';
        }
        tab[i]=
    }
}




int main(int argc, char **argv)
{
    char tekst[MAKS];
    int klucz = 0;
    
    cout << "Podaj tekst: " << endl;
    cin.getline(tekst, MAKS);
    
    cout << "Podaj klucz: ";
    cin >> klucz;
    
    
    szyfruj(tekst, klucz);
    return 0;
}
