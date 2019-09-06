/*
 * petla.cpp
 * 
 */


#include <iostream>
#include <cstdlib>

using namespace std;

void los(int tab[], int rozmiar)
{
    srand(time(NULL)); //inicjacja generatoraliczb pseudolosowych
    for(int i = 0; i < rozmiar; i++)
    {
        tab[i] = rand() % 31;
    }
}

void drukuj(int tab[], int rozmiar)
{
    for(int i = 0; i < rozmiar; i++)
    {
        cout << tab[i] << ' ';
    }
}

int main(int argc, char **argv)
{
    int rozmiar = 5;
    int tablica[rozmiar];  // statyczna deklaracja tablicy
    los(tablica, rozmiar);
    drukuj(tablica, rozmiar);
	
	return 0;
}

