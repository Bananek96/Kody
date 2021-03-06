/*
 * wyszukaj.cpp
 */


#include <iostream>
#include <cstdlib>
using namespace std;

void los(int tab[], int rozmiar)
{
    srand(time(NULL));  // inicjacja generatoraliczb pseudolosowych
    for(int i = 0; i < rozmiar; i++)
    {
        tab[i] = rand() % 21;
    }
}

void drukuj(int tab[], int rozmiar)
{
    for(int i = 0; i < rozmiar; i++)
    {
        cout << tab[i] << ' ';
    }
}

void sort_insert(int tab[], int n)
{
    int i, j, tmp;
    for(i = 1; i < n; i++)  // pętla wybiera elementy zaczynając od drugiego
    {
        tmp = tab[i];
        j = i - 1;
        while(j >= 0 && tab[j] >tmp)
        {
            tab[j+1] = tab[j];
            j--;
        }
        tab[j+1] = tmp;
    }
}

int szukaj_bin_it(int tab[], int roz, int szuk)
{
    int p, k, s;
    p = 0;
    k = roz - 1;
    while(p <= k)
    {
        s = (p + k) / 2;
        if (tab[s] == szuk) return s;
        else if (szuk < tab[s]) k = s - 1;
        else p = s + 1;
    }
    return -1;
}

int szukaj_bin_re(int tab[], int szuk, int p, int k)
{
    if(p <= k)
    {
        int s = (p + k) / 2;
        if (tab[s] == szuk) return s;
        if (szuk < tab[s]) return szukaj_bin_re(tab, szuk, p, s-1);
        else return szukaj_bin_re(tab, szuk, s+1, k);
    }
    return -1;
}

int main(int argc, char **argv)
{
	int rozmiar = 20;
    int tablica[rozmiar];  // statyczna deklaracja tablicy
    los(tablica, rozmiar);
    drukuj(tablica, rozmiar);
    cout << endl;
    int szukane = 0;
    cout << "Podaj liczbe: ";
    cin >> szukane;
    cout << endl;
    sort_insert(tablica, rozmiar);
    drukuj(tablica, rozmiar);
    //~ int indeks = szukaj_bin_it(tablica, rozmiar, szukane);
    int indeks = szukaj_bin_re(tablica, szukane, 0, rozmiar - 1);
    cout << endl;
    if (indeks >= 0)
        {
            cout << "\nZnaleziona na indeksie! " << indeks << endl;
        }
    else
        {
            cout << "\nNie Znaleziona! " << indeks << endl;
        }
    
    
	return 0;
}

