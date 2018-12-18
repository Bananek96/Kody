/*
 * sortowanie.cpp
 */

#include <iostream>
#include <cstdlib>

using namespace std;

void los(int tab[], int rozmiar)
{
    srand(time(NULL));  // inicjacja generatoraliczb pseudolosowych
    for(int i = 0; i < rozmiar; i++)
    {
        tab[i] = rand() % 101;
    }
}

void drukuj(int tab[], int rozmiar)
{
    for(int i = 0; i < rozmiar; i++)
    {
        cout << tab[i] << ' ';
    }
}

//~ void zamien(int &a, int &b)
//~ {
    //~ int tmp; //zmienna pomocnicza
    //~ tmp = a;
    //~ a = b;
    //~ b = tmp;
//~ }

void zamien(int tab[], int i)
{
    int tmp = tab[i];
    tab[i] = tab[i+1];
    tab[i+1] = tmp;
}

void sort_bubble1(int tab[],int n)
{
    cout << "\nSortowanie bąbelkowe rosnące" << endl;
    int licz = 0;
    for(int j = n - 1; j > 0; j--)
    {
        for(int i = 0; i <  j; i++)  // pętla wewnętrzna
        {
            licz++;
            if(tab[i] > tab[i+1])
            {
                // zamiana miejscami
                zamien(tab, i);
            }
        }
    }
    cout << "Powtórzenia: " << licz << endl;
}

void sort_bubble2(int tab[],int n)
{
    cout << "\nSortowanie bąbelkowe malejące" << endl;
    int licz = 0;
    for(int j = n - 1; j > 0; j--)
    {
        for(int i = 0; i <  j; i++)  // pętla wewnętrzna
        {
            licz++;
            if(tab[i] < tab[i+1])
            {
                // zamiana miejscami
                zamien(tab, i);
            }
        }
    }
    cout << "Powtórzenia: " << licz << endl;
}

void sort_insert(int tab[], int n)
{
    cout << "\nSortowanie przez wstawianie" << endl;
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

int main(int argc, char **argv)
{
    int rozmiar = 20;
    int tablica[rozmiar];  // statyczna deklaracja tablicy
    los(tablica, rozmiar);
    drukuj(tablica, rozmiar);
    cout << endl;
    sort_bubble1(tablica, rozmiar);  // sortowanie rosnąco
    drukuj(tablica, rozmiar);
    sort_bubble2(tablica, rozmiar);  // sortowanie malejąco
    drukuj(tablica, rozmiar);
    sort_insert(tablica, rozmiar);
    drukuj(tablica, rozmiar);
    
    return 0;
}

